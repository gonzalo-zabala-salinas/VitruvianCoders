import json
import sqlite3

# 1. Nombre de tu archivo JSON (asegúrate de que esté en la misma carpeta)
ARCHIVO_JSON = '300349_20261013_203455.json'

def configurar_base_datos():
    # 2. Esto crea el archivo ileo_data.db automáticamente
    print("Creando base de datos y tablas...")
    conn = sqlite3.connect('ileo_data.db')
    cursor = conn.cursor()

    # Tabla Clientes/Ideas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes_ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_cliente TEXT,
        idea_original TEXT,
        idea_estructurada_ia TEXT
    )
    ''')

    # Tabla Empresas (Socios)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_empresa TEXT,
        capacidades_tecnicas TEXT,
        intereses_innovacion TEXT
    )
    ''')

    # Tabla Subvenciones
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subvenciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo_convocatoria TEXT,
        descripcion TEXT,
        requisitos TEXT,
        sectores_objetivo TEXT,
        presupuesto REAL
    )
    ''')

    # 3. Leer e importar el JSON a SQLite
    print("Leyendo archivo JSON...")
    with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    print(f"Insertando {len(datos)} subvenciones...")
    for item in datos:
        cursor.execute('''
            INSERT INTO subvenciones (titulo_convocatoria, descripcion, requisitos, sectores_objetivo, presupuesto)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            item.get('title', 'Sin título'),
            item.get('proyecto_subvencionado', ''),
            item.get('bases_reguladoras', ''), # URL a las bases
            item.get('naturaleza_juridica_title', ''),
            float(item.get('importe', 0.0) if item.get('importe') else 0.0)
        ))

    # Insertar un par de empresas de prueba para el matching
    empresas_prueba = [
        ("TechVision SA", "Visión artificial, IA, robótica industrial", "Buscamos proyectos de detección de defectos en manufactura"),
        ("EcoEnergies", "Energías renovables, optimización de recursos", "Innovación en sostenibilidad y control energético")
    ]
    cursor.executemany('''
        INSERT INTO empresas (nombre_empresa, capacidades_tecnicas, intereses_innovacion)
        VALUES (?, ?, ?)
    ''', empresas_prueba)

    # Guardar cambios y cerrar
    conn.commit()
    conn.close()
    print("✅ Base de datos configurada e importación completada con éxito.")

if __name__ == "__main__":
    configurar_base_datos()