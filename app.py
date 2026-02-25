import streamlit as st

# Configuración de la página para que parezca un flyer vertical
st.set_page_config(
    page_title="Información Oficial para tu Proyecto",
    page_icon="📩",
    layout="centered"
)

# Estilo CSS para dar apariencia de Flyer Profesional
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .flyer-container {
        background-color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-top: 10px solid #1E3A8A;
        max-width: 700px;
        margin: auto;
    }
    .header-title {
        color: #1E3A8A;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }
    .highlight-box {
        background-color: #EBF1FF;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        border-left: 5px solid #1E3A8A;
    }
    .cta-button {
        background-color: #1E3A8A;
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 8px;
        display: block;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.2rem;
        margin-top: 30px;
    }
    .footer-text {
        font-size: 0.8rem;
        color: #6B7280;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Contenedor principal del Flyer
with st.container():
    st.markdown(f"""
    <div class="flyer-container">
        <h1 class="header-title">📩 ¿NECESITAS INFORMACIÓN OFICIAL PARA FORTALECER TU PROYECTO?</h1>
        <p style="text-align: center; font-size: 1.3rem; color: #374151; font-weight: 500;">
            Diseñamos Derechos de Petición Estratégicos
        </p>
        <p style="text-align: center; color: #1E3A8A; font-weight: bold;">
            Convierte preguntas en información clave. Convierte información en ventaja.
        </p>

        <hr>

        <h3 style="color: #1E3A8A;">🎯 ¿Qué hacemos?</h3>
        <p>Diseñamos y redactamos derechos de petición inteligentes para obtener:</p>
        <ul style="list-style-type: none; padding-left: 10px;">
            <li>✅ <b>Datos</b> que no están publicados</li>
            <li>✅ <b>Información técnica</b> de entidades públicas</li>
            <li>✅ <b>Respuestas formales</b> y verificables</li>
            <li>✅ <b>Insumos</b> para fortalecer propuestas y reformas</li>
        </ul>

        <div class="highlight-box">
            <h3 style="margin-top: 0; color: #1E3A8A;">🚀 ¿Para qué te sirve?</h3>
            <ul style="margin-bottom: 0;">
                <li>Sustentar proyectos sociales</li>
                <li>Respaldar iniciativas legislativas</li>
                <li>Medir brechas reales e identificar vacíos</li>
                <li>Tomar decisiones con información oficial</li>
            </ul>
        </div>

        <p style="text-align: center; font-style: italic; color: #4B5563;">
            "La información correcta cambia el rumbo de un proyecto."
        </p>
        
        <a href="#" class="cta-button">📲 AGENDA TU ASESORÍA</a>

        <div class="footer-text">
            ⚖ Servicio técnico – administrativo. <br>
            No incluye representación jurídica.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Nota para el usuario en la barra lateral
with st.sidebar:
    st.title("Panel de Control")
    st.write("Esta es la vista previa de tu flyer publicitario digital.")
    st.info("Diseño optimizado para lectura clara y profesional.")
