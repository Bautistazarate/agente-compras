from crewai import Crew, Process
from agents import buscador, analista, recomendador
from tasks import tarea_busqueda, tarea_analisis, tarea_recomendacion

shopping_crew = Crew(
    agents=[buscador, analista, recomendador],
    tasks=[tarea_busqueda, tarea_analisis, tarea_recomendacion],
    process=Process.sequential,
    verbose=True
)