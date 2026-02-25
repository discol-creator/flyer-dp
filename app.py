import streamlit as st

# Configuración de página
st.set_page_config(page_title="Información Estratégica", layout="centered")

# Estilo CSS Personalizado (Fuerza colores y diseño de agencia)
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background-color: #0F172A;
    }
    
    /* Contenedor del Flyer */
    .flyer-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid #334155;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    .gold-text {
        color: #FACC15;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 20px;
        color: #FFFFFF;
    }
    
    .section-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }
    
    .cta-button {
        background-color: #FACC15;
        color: #0F172A !important;
        text-align: center;
        padding: 18px;
        border-radius: 10px;
        display: block;
        text-decoration: none;
        font-weight: 900;
        font-size: 1.2rem;
        margin-top: 40px;
        transition: 0.3s;
    }
    
    .cta-button:hover {
        background-color: #EAB308;
        transform: scale(1.02);
    }

    .footer-legal {
        font-size: 0.8rem;
        color: #94a3b8;
        text-align: center;
        margin-top: 30px;
        border-top: 1px solid #334155;
        padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Renderizado del Flyer
st.markdown(f"""
    <div class="flyer-card">
        <p class="gold-text">Gestión Estratégica</p>
        <h1 class="main-title">📩 ¿Necesitas información oficial para fortalecer tu proyecto?</h1>
        
        <p style="font-size: 1.2rem; color: #cbd5e1;">
            <b>Diseñamos Derechos de Petición Inteligentes.</b><br>
            Convierte preguntas en información clave. Convierte información en ventaja.
        </p>

        <div class="section-box">
            <h3 style="color: #FACC15; margin-top:0;">🎯 ¿Qué hacemos?</h3>
            <p style="color: #e2e8f0;">Redactamos peticiones estratégicas para obtener:</p>
            <ul style="color: #94a3b8;">
                <li>Datos no publicados y técnicos.</li>
                <li>Respuestas formales de entidades públicas.</li>
                <li>Insumos para propuestas y reformas.</li>
            </ul>
        </div>

        <div class="section-box">
            <h3 style="color: #FACC15; margin-top:0;">🚀 ¿Para qué te sirve?</h3>
            <ul style="color: #e2e8f0; list-style-type: '✔  ';">
                <li>Sustentar proyectos sociales.</li>
                <li>Respaldar iniciativas legislativas.</li>
                <li>Medir brechas y vacíos institucionales.</li>
                <li>Tomar decisiones basadas en datos oficiales.</li>
            </ul>
        </div>

        <p style="text-align: center; margin-top: 30px; font-style: italic; color: #94a3b8;">
            "La información correcta cambia el rumbo de un proyecto."
        </p>

        <a href="https://wa.me/TU_NUMERO" class="cta-button">📲 AGENDA TU ASESORÍA</a>

        <div class="footer-legal">
            ⚖ Servicio técnico – administrativo. No incluye representación jurídica.
        </div>
    </div>
    """, unsafe_allow_html=True)
