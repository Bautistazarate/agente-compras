from crewai import Agent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

search_tool = SerperDevTool()

buscador = Agent(
    role="Buscador de productos y precios",
    goal="Encontrar al menos 5 opciones reales de {producto} dentro del presupuesto de {presupuesto}",
    backstory="Sos un experto en encontrar las mejores ofertas online. Conocés los principales e-commerce y sabés cómo comparar precios reales.",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

analista = Agent(
    role="Analista de calidad y reseñas",
    goal="Evaluar la calidad real de cada producto basándote en reseñas de usuarios y expertos",
    backstory="Sos un consumidor experto que lee cientos de reseñas y puede detectar cuándo un producto tiene problemas reales vs cuando es simplemente marketing.",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

recomendador = Agent(
    role="Asesor de compras personal",
    goal="Generar una recomendación clara, justificada y accionable para la mejor compra posible",
    backstory="Sos un asesor de confianza que resume toda la información disponible y da una recomendación honesta, sin rodeos, pensando en el bolsillo y las necesidades reales del usuario.",
    verbose=True,
    allow_delegation=False
)