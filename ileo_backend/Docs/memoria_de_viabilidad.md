# 💼 Memoria de Viabilidad (Business Plan) - iLEO 360

## 1. Resumen Ejecutivo
**iLEO 360** es un SaaS B2B impulsado por Inteligencia Artificial que actúa como un "Copiloto de Innovación". Su objetivo es reducir drásticamente el tiempo que las empresas, universidades y consultoras tardan en estructurar proyectos tecnológicos, encontrar socios estratégicos y localizar vías de financiación pública. 

## 2. El Problema y la Solución
**El Problema:** Actualmente, el ecosistema de innovación está fragmentado. Cuando un investigador o empresa tiene una idea, estructurarla para encajarla en niveles TRL, encontrar el partner tecnológico adecuado y cazar la subvención idónea es un proceso manual, lento (semanas de trabajo) y propenso a errores.
**La Solución:** iLEO 360 ingiere una descripción (texto o PDF), utiliza IA generativa para estructurar la información (Sector, Tecnologías, TRL) y cruza estos datos con el ecosistema. Devuelve una "Hoja de Ruta" justificada con la mejor opción de partner y financiación en menos de 10 segundos.

## 3. Viabilidad Técnica
El MVP desarrollado demuestra la viabilidad técnica completa de la solución:
*   **Velocidad y Precisión:** Uso de modelos ultrarrápidos (Gemini 1.5 Flash) que garantizan tiempos de respuesta mínimos.
*   **Arquitectura Desacoplada:** Frontend moderno en HTML/JS servido por un backend robusto en Python (FastAPI).
*   **Lógica en 2 Fases (Explicabilidad):** El sistema no solo busca en bases de datos relacionales (SQLite), sino que utiliza la IA como "juez" en una segunda fase para garantizar que los *matches* tengan sentido y sean explicables para el usuario.

## 4. Viabilidad Económica
El modelo de negocio es altamente escalable y de bajo coste marginal:
*   **Costes variables bajos:** El coste por análisis (tokens de Gemini) es del orden de céntimos, mientras que el valor aportado al cliente B2B (ahorro de días de consultoría) justifica un ticket alto de suscripción.
*   **Estrategia Go-to-Market:** Foco inicial en OTRIs universitarias y pequeñas agencias de consultoría como *early adopters*.

## 5. Roadmap a corto plazo (Próximos 6 meses)
1.  **Mes 1-2:** Migración de la base de datos local (SQLite) a un entorno Cloud (PostgreSQL). Implementación de scrapping automático para mantener actualizadas las convocatorias de ayudas.
2.  **Mes 3-4:** Generación automática de memorias en PDF y exportación de la "Hoja de Ruta".
3.  **Mes 5-6:** Lanzamiento de la API pública para integración B2B y captación de los primeros 10 clientes de pago.