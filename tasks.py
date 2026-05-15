from crewai import Task
from agents import buscador, analista, recomendador

tarea_busqueda = Task(
    description="""
    Buscá opciones de compra para: {producto}
    Presupuesto máximo: {presupuesto}

    Para cada opción encontrá:
    - Nombre exacto del producto y modelo
    - Precio actual
    - Tienda donde está disponible
    - Características principales (mínimo 3)

    Devolvé mínimo 10 opciones ordenadas por precio.
    """,
    expected_output="Lista de 10 productos con nombre, precio, tienda y características principales.",
    agent=buscador
)

tarea_analisis = Task(
    description="""
    Analizá cada producto de la lista anterior.
    Para cada uno buscá reseñas reales de usuarios.

    Evaluá y puntuá del 1 al 10:
    - Calidad de construcción
    - Relación precio/calidad
    - Problemas frecuentes reportados
    - Satisfacción general

    Descartá productos con problemas graves reportados consistentemente.
    """,
    expected_output="Tabla de análisis con puntaje por producto, pros, contras y alertas.",
    agent=analista,
    context=[tarea_busqueda]
)

tarea_recomendacion = tarea_recomendacion = Task(
    description="""
    Con toda la información recopilada, generá el informe final.

    El informe debe incluir:
    1. GANADOR: el producto que más conviene y por qué
    2. ALTERNATIVA: segunda opción si el ganador no está disponible
    3. EVITAR: productos que NO recomendar y por qué
    4. CONSEJO FINAL: tip práctico para esta compra
    """,
    expected_output="""
    Un informe en formato Markdown con estas secciones exactas:

    ## 🏆 Ganador
    **Nombre del producto** — precio
    Explicación de por qué es la mejor opción en 2-3 oraciones.
    - ✅ Pro 1
    - ✅ Pro 2
    - ✅ Pro 3

    ## 🥈 Alternativa
    **Nombre del producto** — precio
    Breve explicación de cuándo elegir esta opción.

    ## ❌ Evitar
    - **Producto X**: razón concreta
    - **Producto Y**: razón concreta

    ## 💡 Consejo final
    Tip práctico en 2-3 oraciones para esta compra específica.
    """,
    agent=recomendador,
    context=[tarea_busqueda, tarea_analisis]
)