import streamlit as st
import streamlit.components.v1 as components

# Configuración de página
st.set_page_config(page_title="Flyer Informativo", layout="centered")

# --- DEFINICIÓN DEL FLYER EN HTML/CSS ---
flyer_html = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 20px;
            background-color: #F3F4F6; /* Gris claro de fondo para contraste */
            font-family: 'Inter', sans-serif;
        }
        .flyer {
            background: #0F172A; /* Azul Marino Profundo */
            color: white;
            max-width: 600px;
            margin: 0 auto;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border: 1px solid #334155;
        }
        .header {
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
            padding: 40px 30px;
            text-align: center;
            border-bottom: 4px solid #FACC15;
        }
        .gold-tag {
            color: #FACC15;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.9rem;
            margin-bottom: 10px;
            display: block;
        }
        h1 {
            font-size: 2rem;
            line-height: 1.2;
            margin: 0;
            font-weight: 800;
        }
        .content {
            padding: 30px;
        }
        .slogan {
            font-size: 1.1rem;
            color: #94A3B8;
            margin-bottom: 30px;
            line-height: 1.5;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }
        .card {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        h3 {
            color: #FACC15;
            margin-top: 0;
            margin-bottom: 10px;
            font-size: 1.2rem;
        }
        ul {
            padding-left: 20px;
            margin: 0;
            color: #CBD5E1;
        }
        li {
            margin-bottom: 8px;
        }
        .cta-btn {
            display: block;
            background: #FACC15;
            color: #0F172A !important;
            text-align: center;
            padding: 18px;
            margin-top: 30px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 800;
            font-size: 1.1rem;
            transition: transform 0.2s;
        }
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 0.75rem;
            color: #64748B;
            border-top: 1px solid #1E293B;
        }
    </style>
</head>
<body>
    <div class="flyer">
        <div class="header">
            <span class="gold-tag">Servicio Estratégico</span>
            <h1>📩 ¿Necesitas información oficial para fortalecer tu proyecto?</h1>
        </div>
        
        <div class="content">
            <p class="slogan">
                <b>Diseñamos Derechos de Petición Inteligentes.</b><br>
                Convierte preguntas en información clave. Convierte información en ventaja.
            </p>

            <div class="grid">
                <div class="card">
                    <h3>🎯 ¿Qué hacemos?</h3>
                    <ul>
                        <li>Datos técnicos y no publicados.</li>
                        <li>Respuestas formales de entidades.</li>
                        <li>Insumos para propuestas y reformas.</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>🚀 ¿Para qué te sirve?</h3>
                    <ul>
                        <li>Sustentar proyectos sociales.</li>
                        <li>Respaldar iniciativas legislativas.</li>
                        <li>Identificar vacíos institucionales.</li>
                    </ul>
                </div>
            </div>

            <a href="#" class="cta-btn">📲 AGENDA TU ASESORÍA</a>
        </div>

        <div class="footer">
            ⚖ Servicio técnico – administrativo. No incluye representación jurídica.<br>
            "La información correcta cambia el rumbo de un proyecto."
        </div>
    </div>
</body>
</html>
"""

# --- RENDERIZADO ---
st.title("Vista Previa del Flyer Publicitario")

# Renderizamos el HTML con una altura fija para evitar scroll innecesario
components.html(flyer_html, height=900, scrolling=True)
