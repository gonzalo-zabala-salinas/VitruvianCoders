import sqlite3

# Lista de subvenciones ficticias pero realistas para enriquecer la demo
subvenciones_mock = [
    # Inteligencia Artificial y Datos
    ("Ayudas CDTI a la I+D+i en Inteligencia Artificial", "Apoyo a proyectos de desarrollo de algoritmos de Deep Learning, Machine Learning y Visión Artificial.", "https://cdti.es/bases-ia", "Inteligencia Artificial, Datos", 250000.0),
    ("Kit Digital Avanzado: IA y Automatización", "Bonos para la adopción de asistentes virtuales corporativos, RPA y análisis predictivo en PYMES.", "https://acelerapyme.es/kit-digital-ia", "Digitalización, IA", 25000.0),
    
    # Salud y MedTech
    ("Programa NEOTEC - Tecnologías de la Salud", "Subvenciones para startups que desarrollen robótica médica, telemedicina, señales EMG o biotecnología.", "https://cdti.es/neotec-salud", "Salud, MedTech", 300000.0),
    
    # Sostenibilidad y Medio Ambiente
    ("Fondos Next Generation - Descarbonización Industrial", "Ayudas para la integración de energías renovables, smart grids y reducción de huella de carbono.", "https://mincotur.gob.es/descarbonizacion", "Sostenibilidad, Industria", 500000.0),
    ("Fondo de Innovación en Economía Circular", "Ayudas para proyectos de tratamiento de aguas, nanomateriales y reducción de residuos industriales.", "https://miteco.gob.es/economia-circular", "Medio Ambiente, Sostenibilidad", 350000.0),
    
    # Movilidad Inteligente
    ("Misiones Ciencia e Innovación - Movilidad Sostenible", "Financiación para sistemas de conducción autónoma, sensores LiDAR, V2X y optimización de flotas logísticas.", "https://ciencia.gob.es/misiones-movilidad", "Movilidad, Logística", 800000.0),
    
    # FinTech y Ciberseguridad
    ("Ayudas ENISA Emprendedores Digitales", "Préstamos participativos para proyectos de FinTech, blockchain, smart contracts y ciberseguridad.", "https://enisa.es/emprendedores-digitales", "FinTech, Ciberseguridad", 150000.0),
    
    # Industria 4.0 e IoT
    ("Convocatoria Retos I+D - Industria 4.0", "Proyectos colaborativos para gemelos digitales, sensores IoT y robótica industrial colaborativa.", "https://aei.gob.es/retos-industria", "Industria 4.0, IoT", 400000.0),
    
    # Educación (EdTech)
    ("Programa EduTech Avanza", "Subvenciones para plataformas LMS, Realidad Virtual inmersiva educativa y gamificación en el aula.", "https://educacion.gob.es/edutech", "EdTech, Educación", 100000.0),
    
    # Deep Tech / General
    ("Horizonte Europa - Deep Tech y Computación", "Consorcios europeos para investigación en nuevos modelos computacionales, NLP avanzado y tecnologías disruptivas.", "https://ec.europa.eu/horizon-deeptech", "Deep Tech, NLP", 1200000.0)
]

def poblar_subvenciones():
    print("Conectando a la base de datos ileo_data.db...")
    try:
        conn = sqlite3.connect('ileo_data.db')
        cursor = conn.cursor()
        
        # Insertar todas las subvenciones de golpe
        cursor.executemany('''
            INSERT INTO subvenciones (titulo_convocatoria, descripcion, requisitos, sectores_objetivo, presupuesto)
            VALUES (?, ?, ?, ?, ?)
        ''', subvenciones_mock)
        
        conn.commit()
        conn.close()
        print(f"✅ Éxito: Se han añadido {len(subvenciones_mock)} convocatorias nuevas a la base de datos.")
    except Exception as e:
        print(f"❌ Error al insertar datos: {e}")

if __name__ == "__main__":
    poblar_subvenciones()