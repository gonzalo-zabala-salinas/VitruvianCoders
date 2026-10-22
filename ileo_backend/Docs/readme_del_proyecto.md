# iLEO 360° - Copiloto de Innovación 🚀

**iLEO 360** es una plataforma SaaS impulsada por IA (Google Gemini) que actúa como un copiloto para el ecosistema de innovación. Transforma ideas en crudo o documentos ejecutivos en hojas de ruta estructuradas, conectando proyectos con los socios estratégicos y las subvenciones públicas más adecuadas.

*Desarrollado para el Hackathon.*

## ✨ Características Principales
*   **Análisis Multimodal:** Soporta entrada de texto libre o subida de documentos (PDF, TXT).
*   **Extracción Automática:** Identifica el Sector, Tecnologías Clave y estima el nivel de madurez TRL.
*   **Matchmaking Inteligente:** Cruza la idea con una base de datos local de socios y convocatorias públicas.
*   **Explicabilidad Total:** No es una caja negra. La IA explica exactamente *por qué* recomienda a cada socio y destaca la mejor opción.
*   **UI Moderna:** Interfaz *Glassmorphism* optimizada para velocidad y experiencia de usuario.

## 🛠️ Stack Tecnológico
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Backend:** Python 3, FastAPI, Uvicorn
*   **IA:** Google Generative AI (Gemini 1.5 Flash)
*   **Base de Datos:** SQLite

## 🚀 Guía de Instalación y Despliegue Local

Sigue estos pasos para ejecutar el MVP en tu ordenador:

**1. Clonar el repositorio y acceder a la carpeta**
```bash
git clone <tu-repositorio>
cd ileo_backend
```

**2. Instalar dependencias**
Asegúrate de tener Python instalado. Se recomienda usar un entorno virtual.
```bash
pip install fastapi uvicorn google-generativeai pydantic python-multipart pypdf2
```

**3. Configurar variables de entorno**
Define tu clave de Google Gemini como variable de entorno. No la guardes en el código ni la subas a GitHub.

En PowerShell:
```powershell
$env:GEMINI_API_KEY = "TU_API_KEY_DE_GEMINI"
```

En Linux/macOS:
```bash
export GEMINI_API_KEY="TU_API_KEY_DE_GEMINI"
```

**4. Poblar la Base de Datos (Solo la primera vez)**
Si no tienes el archivo `ileo_data.db`, ejecuta estos scripts para generar los datos ficticios del ecosistema:
```bash
python setup_db.py
python poblar_empresas.py
python poblar_subvenciones.py
```

**5. Arrancar el Servidor**
```bash
python main.py
```

**6. Uso**
Abre tu navegador web y dirígete a `http://127.0.0.1:8000/`. ¡La plataforma está lista!