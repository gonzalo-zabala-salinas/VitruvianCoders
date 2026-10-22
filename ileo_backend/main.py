import sqlite3
import json
import io
import os
from fastapi import FastAPI, HTTPException, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import google.generativeai as genai
import uvicorn
import PyPDF2
import time

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Falta la variable de entorno GEMINI_API_KEY.")
genai.configure(api_key=API_KEY)

modelo_ia = genai.GenerativeModel('gemini-3.8-flash')

app = FastAPI(title="iLEO 360 API")

def conectar_db():
    conn = sqlite3.connect('ileo_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.post("/api/analizar")
async def analizar_proyecto(
    nombre_cliente: str = Form(...),
    modo: str = Form(...),
    idea_texto: str = Form(""),
    archivo: UploadFile = File(None)
):
    try:
        texto_a_analizar = ""

        if modo == 'texto':
            texto_a_analizar = idea_texto
        elif modo == 'archivo' and archivo is not None:
            contenido = await archivo.read()
            if archivo.filename.endswith('.pdf'):
                lector_pdf = PyPDF2.PdfReader(io.BytesIO(contenido))
                texto_extraido = ""
                for pagina in lector_pdf.pages:
                    texto_extraido += pagina.extract_text()
                texto_a_analizar = texto_extraido
            else:
                texto_a_analizar = contenido.decode('utf-8')
        else:
            return {"estado": "error", "mensaje": "No se recibió texto ni archivo."}

        # FASE 1: Extraer estructura
        prompt_1 = f"""
        Actúa como un experto consultor. Analiza esta idea: "{texto_a_analizar[:1000]}"
        Devuelve ÚNICAMENTE un JSON con:
        - "sector": El sector principal.
        - "tecnologias": Lista de 2 o 3 palabras clave cortas (ej. "Drones", "IA").
        - "madurez_trl": TRL estimado del 1 al 9.
        - "resumen_ejecutivo": Un resumen de 1 frase.
        """
        res_1 = modelo_ia.generate_content(prompt_1).text.strip()
        if res_1.startswith("```json"): res_1 = res_1[7:-3]
        idea_estructurada = json.loads(res_1)
        tecnologias = idea_estructurada.get("tecnologias", [])
        sector = idea_estructurada.get("sector", "")
        
        conn = conectar_db()
        cursor = conn.cursor()
        
        # Búsqueda en BBDD
        socios_match = []
        if tecnologias:
            cursor.execute("SELECT nombre_empresa, capacidades_tecnicas FROM empresas WHERE capacidades_tecnicas LIKE ? OR intereses_innovacion LIKE ?", (f"%{tecnologias[0]}%", f"%{tecnologias[0]}%"))
            socios_match = [dict(row) for row in cursor.fetchall()]

        subvenciones_match = []
        if tecnologias:
            cursor.execute("SELECT titulo_convocatoria, presupuesto FROM subvenciones WHERE descripcion LIKE ? OR requisitos LIKE ? LIMIT 4", (f"%{tecnologias[0]}%", f"%{tecnologias[0]}%"))
            subvenciones_match = [dict(row) for row in cursor.fetchall()]
        if not subvenciones_match:
            cursor.execute("SELECT titulo_convocatoria, presupuesto FROM subvenciones WHERE descripcion LIKE ? OR sectores_objetivo LIKE ? LIMIT 4", (f"%{sector}%", f"%{sector}%"))
            subvenciones_match = [dict(row) for row in cursor.fetchall()]

        conn.close()
        

        # --- AÑADE ESTA LÍNEA PARA EVITAR EL ERROR 429 ---
        time.sleep(4) 
    

        # FASE 2: Explicabilidad y Ponderación con Gemini
        prompt_2 = f"""
        Proyecto del cliente: "{texto_a_analizar[:800]}"
        
        Empresas encontradas en BBDD: {json.dumps(socios_match)}
        Subvenciones encontradas en BBDD: {json.dumps(subvenciones_match)}
        
        Evalúa estos resultados. Devuelve ÚNICAMENTE un JSON con esta estructura exacta:
        {{
            "socios_evaluados": [
                {{
                    "nombre": "Nombre de la empresa",
                    "explicacion": "Una frase corta justificando por qué es el socio ideal para este proyecto.",
                    "es_mejor_opcion": true/false
                }}
            ],
            "subvenciones_evaluadas": [
                {{
                    "titulo": "Titulo de subvencion",
                    "presupuesto": "importe",
                    "explicacion": "Una frase corta explicando por qué el proyecto encaja en esta ayuda.",
                    "es_mejor_opcion": true/false
                }}
            ]
        }}
        Importante: Marca "es_mejor_opcion": true SOLO en UNA empresa y en UNA subvención (la que tenga más sentido).
        """
        
        res_2 = modelo_ia.generate_content(prompt_2).text.strip()
        if res_2.startswith("```json"): res_2 = res_2[7:-3]
        evaluacion_final = json.loads(res_2)

        return {
            "estado": "exito",
            "analisis_ia": idea_estructurada,
            "socios": evaluacion_final.get("socios_evaluados", []),
            "subvenciones": evaluacion_final.get("subvenciones_evaluadas", [])
        }

    except Exception as e:
        return {"estado": "error", "mensaje": str(e)}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def leer_index():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)