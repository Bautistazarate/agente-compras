import streamlit as st
from crew import shopping_crew

st.set_page_config(
    page_title="Agente de Compras Inteligente",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Agente de Compras Inteligente")
st.markdown("Usá IA para encontrar la mejor compra según tu presupuesto.")
st.divider()

with st.form("formulario"):
    producto = st.text_input(
        "¿Qué querés comprar?",
        placeholder="Ej: auriculares bluetooth inalámbricos"
    )
    presupuesto = st.text_input(
        "¿Cuál es tu presupuesto máximo?",
        placeholder="Ej: 50000 pesos argentinos"
    )
    buscar = st.form_submit_button("🔍 Analizar opciones", use_container_width=True)

if buscar:
    if not producto or not presupuesto:
        st.warning("Por favor completá los dos campos.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Producto", producto[:20] + "..." if len(producto) > 20 else producto)
        col2.metric("Presupuesto", presupuesto)
        col3.metric("Agentes activos", "3")

        st.divider()

        with st.status("Los agentes están trabajando...", expanded=True) as status:
            st.write("🔍 Agente 1: buscando productos y precios...")
            st.write("⭐ Agente 2: analizando reseñas de usuarios...")
            st.write("🏆 Agente 3: preparando recomendación final...")

            resultado = shopping_crew.kickoff(inputs={
                "producto": producto,
                "presupuesto": presupuesto
            })

            status.update(label="¡Análisis completado!", state="complete")

        st.divider()
        st.markdown("## 📊 Informe de Compra")
        st.markdown(str(resultado))

        st.divider()
        st.download_button(
            label="⬇️ Descargar informe completo",
            data=str(resultado),
            file_name=f"informe_{producto[:20].replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True
        )