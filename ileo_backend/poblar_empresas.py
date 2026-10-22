import sqlite3

# Lista de empresas ficticias variadas para el ecosistema de innovación
empresas_mock = [
    # --- Salud / MedTech ---
    ("NeuroHealth AI", "Procesamiento de señales neuronales, IA médica, algoritmos de diagnóstico", "Buscan startups para detección temprana de enfermedades neurológicas o mentales"),
    ("MedRobotics Europe", "Robótica quirúrgica, mecatrónica, exoesqueletos", "Interesados en TRL 5-7 para automatización en quirófanos y rehabilitación"),
    ("GenoTech Solutions", "Secuenciación genómica, biotecnología, CRISPR", "Buscamos investigaciones sobre terapias génicas personalizadas"),

    # --- Inteligencia Artificial / Datos ---
    ("DataMind Analytics", "Big Data, Machine Learning, Análisis predictivo", "Buscamos proyectos de IA aplicada a la predicción de demanda y comportamiento de usuario"),
    ("Visionary AI", "Visión artificial, reconocimiento de imágenes, Deep Learning", "Proyectos de control de calidad industrial, detección de defectos y seguridad automatizada"),
    ("NLP Dynamics", "Procesamiento de Lenguaje Natural, LLMs, Chatbots", "Interesados en asistentes virtuales corporativos y análisis de sentimiento multilingüe"),

    # --- Sostenibilidad / Medio Ambiente ---
    ("GreenGrid Dynamics", "Smart grids, almacenamiento de energía, IoT", "Optimización de redes eléctricas y baterías de estado sólido"),
    ("AquaClean Tech", "Tratamiento de aguas, desalinización, nanomateriales", "Proyectos de purificación de agua con bajo coste energético"),
    ("CarbonZero Industries", "Captura de carbono, economía circular, nuevos materiales", "Innovación en materiales biodegradables y procesos industriales sin emisiones"),

    # --- Industria 4.0 / Robótica ---
    ("FactoryBotics", "Brazos robóticos, automatización de líneas, gemelos digitales", "Colaboración en gemelos digitales para mantenimiento predictivo en fábricas"),
    ("IoT Industrial Sensors", "Sensores IoT, redes 5G privadas, edge computing", "Buscamos hardware de sensorización para ambientes industriales extremos"),

    # --- Movilidad / Transporte ---
    ("AutoDrive Systems", "Conducción autónoma, LiDAR, V2X (Vehicle-to-Everything)", "Startups desarrollando algoritmos de fusión de sensores para vehículos autónomos"),
    ("AeroDrone Logistics", "Drones de carga, control de flotas, aeronáutica", "Optimización de rutas de reparto de última milla mediante vehículos aéreos no tripulados"),
    ("UrbanTransit Solutions", "Micromovilidad, smart cities, planificación urbana", "Plataformas SaaS para la gestión del tráfico y sistemas de aparcamiento inteligente"),

    # --- FinTech / Ciberseguridad ---
    ("SecurePay Blockchain", "Blockchain, smart contracts, criptografía", "Integración de pagos descentralizados y trazabilidad financiera"),
    ("CyberShield Ops", "Ciberseguridad, pruebas de penetración, Zero Trust", "Detección de anomalías en redes corporativas mediante Inteligencia Artificial"),

    # --- EdTech / Educación ---
    ("SmartLearn VR", "Realidad Virtual, Realidad Aumentada, Metaverso", "Entornos inmersivos para formación médica e industrial"),
    ("EduCode Platforms", "Plataformas LMS, analítica de aprendizaje, gamificación", "Adaptación de currículos educativos mediante algoritmos de recomendación")
]

def poblar_db():
    print("Conectando a la base de datos ileo_data.db...")
    try:
        conn = sqlite3.connect('ileo_data.db')
        cursor = conn.cursor()
        
        # Insertar todas las empresas de golpe
        cursor.executemany('''
            INSERT INTO empresas (nombre_empresa, capacidades_tecnicas, intereses_innovacion)
            VALUES (?, ?, ?)
        ''', empresas_mock)
        
        conn.commit()
        conn.close()
        print(f"✅ Éxito: Se han añadido {len(empresas_mock)} empresas nuevas a la base de datos.")
    except Exception as e:
        print(f"❌ Error al insertar datos: {e}")

if __name__ == "__main__":
    poblar_db()