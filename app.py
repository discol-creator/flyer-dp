import streamlit as st

# Configuración de estética profesional
st.set_page_config(
    page_title="Información Oficial | Derechos de Petición",
    page_icon="⚖️",
    layout="centered"
)

# Aplicar un estilo minimalista y limpio
st.markdown("""
    <style>
    /* Ocultar menús innecesarios */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Contenedor principal */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* Ajuste de fuentes y espaciado */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        color: #0F172A;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO IMPACTANTE ---
st.write("---")
st.title("📩 ¿Necesitas información oficial para fortalecer tu proyecto?")
st.subheader("Diseñamos Derechos de Petición Estratégicos")
st.markdown("**Convierte preguntas en información clave. Convierte información en ventaja.**")

# --- CUERPO DEL FLYER (Columnas para mejor distribución) ---
col1, col2 = st.columns(2)

with col1:
    st.info("### 🎯 ¿Qué hacemos?")
    st.write("""
    Diseñamos y redactamos derechos de petición inteligentes para obtener:
    - **Datos** que no están publicados.
    - **Información técnica** de entidades públicas.
    - **Respuestas formales** y verificables.
    - **Insumos** para fortalecer propuestas y reformas.
    """)

with col2:
    st.success("### 🚀 ¿Para qué te sirve?")
    st.write("""
    - Sustentar proyectos sociales.
    - Respaldar iniciativas legislativas.
    - Medir brechas reales.
    - Identificar vacíos institucionales.
    - Tomar decisiones con información oficial.
    """)

# --- SECCIÓN DE VALOR ---
st.divider()
st.warning("⚖️ **Servicio técnico – administrativo**\n\nNo incluye representación jurídica.")

st.markdown("""
    > *“La información correcta cambia el rumbo de un proyecto.”*
""")

# --- BOTÓN DE ACCIÓN PROFESIONAL ---
st.write(" ")
if st.button("📲 AGENDA TU ASESORÍA AHORA", use_container_width=True, type="primary"):
    st.balloons()
    st.success("Redirigiendo a asesoría... (Aquí puedes poner tu link de WhatsApp)")

# --- FOOTER ---
st.caption("© 2026 | Consultoría Estratégica en Información Pública")
