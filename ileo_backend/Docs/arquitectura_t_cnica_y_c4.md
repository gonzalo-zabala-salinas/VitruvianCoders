# 🏗️ Arquitectura Técnica y Diagramas C4

iLEO 360 sigue una arquitectura ligera, modular y preparada para escalar. Combina tecnologías tradicionales de bases de datos con Inteligencia Artificial generativa.

## Stack Tecnológico Actual (MVP)
*   **Frontend:** HTML5, CSS3 (Glassmorphism), Vanilla JS (Fetch API).
*   **Backend:** Python 3, FastAPI.
*   **Base de Datos:** SQLite (Migrable a PostgreSQL).
*   **Inteligencia Artificial:** Google Gemini 1.5 Flash (via API).

---

## Diagramas C4 (Mermaid)

### Nivel 1: Contexto del Sistema (System Context)
Muestra cómo iLEO 360 interactúa con los usuarios y los sistemas externos.

```mermaid
graph TD
    User([Consultor / Empresa]) -->|Sube PDF o Texto| iLEO[iLEO 360 Platform]
    iLEO -->|Envía prompts y contexto| Gemini[Google Gemini API]
    Gemini -->|Devuelve JSON estructurado| iLEO
```

### Nivel 2: Contenedores (Containers)
Desglose interno de la aplicación en sus principales contenedores ejecutables.

```mermaid
graph TD
    User([Usuario Final]) -->|HTTPS| WebApp[Frontend Web App\nHTML/JS/CSS]
    WebApp -->|REST API Calls| API[Backend API\nFastAPI - Python]
    
    API -->|SQL Queries| DB[(Database\nSQLite)]
    API -->|gRPC/REST| Gemini[Google Gemini\nLLM Service]
```

### Nivel 3: Componentes del Backend (Components)
Detalle del flujo interno dentro de la API de FastAPI durante una petición.

```mermaid
graph TD
    Router[FastAPI Router\n/api/analizar] --> Parser[File/Text Parser\nPyPDF2]
    Parser --> Agent1[Extractor Agent\nPhase 1 Prompt]
    Agent1 --> GeminiAPI[Gemini API]
    Agent1 --> DBClient[SQLite Client\nSQL Matcher]
    DBClient --> Agent2[Evaluator Agent\nPhase 2 Prompt]
    Agent2 --> GeminiAPI
    Agent2 --> ResponseFormatter[JSON Formatter]
    ResponseFormatter --> Router
```