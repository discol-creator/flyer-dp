import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def generate_flyer(logo_file):
    # Configuración de lienzo (A4 proporcional - 1240x1754 px)
    width, height = 1240, 1754
    canvas = Image.new('RGB', (width, height), color='#FFFFFF')
    draw = ImageDraw.Draw(canvas)

    # Colores
    primary_color = "#1A237E"  # Azul Marino Profundo
    accent_color = "#00C853"   # Verde Éxito (para los checks)
    text_color = "#333333"
    bg_light = "#F5F7F9"

    # --- DISEÑO DE FONDO ---
    # Franja superior estética
    draw.rectangle([0, 0, width, 400], fill=primary_color)
    # Bloque inferior de contacto
    draw.rectangle([0, height-250, width, height], fill=bg_light)

    # --- LOGO ---
    if logo_file:
        logo = Image.open(logo_file).convert("RGBA")
        # Redimensionar logo proporcionalmente
        logo.thumbnail((300, 150))
        canvas.paste(logo, (width//2 - logo.size[0]//2, 50), logo)

    # --- TEXTOS (Fuentes) ---
    # Nota: Asegúrate de tener archivos .ttf o usa los por defecto del sistema
    try:
        font_title = ImageFont.truetype("arial.ttf", 80)
        font_subtitle = ImageFont.truetype("arial.ttf", 55)
        font_body = ImageFont.truetype("arial.ttf", 40)
        font_footer = ImageFont.truetype("arial.ttf", 45)
    except:
        font_title = font_subtitle = font_body = font_footer = ImageFont.load_default()

    # --- CONTENIDO ---
    # Título Principal
    title_text = "¿NECESITAS INFORMACIÓN OFICIAL\nPARA TU PROYECTO?"
    draw.multiline_text((width//2, 520), title_text, fill=primary_color, font=font_title, anchor="mm", align="center")

    # Propuesta de Valor
    draw.text((width//2, 680), "Diseñamos Derechos de Petición Estratégicos", fill=text_color, font=font_subtitle, anchor="mm")
    
    # Separador
    draw.line([300, 750, 940, 750], fill=primary_color, width=5)

    # Sección "¿Qué hacemos?"
    y_pos = 850
    draw.text((100, y_pos), "🎯 ¿Qué hacemos?", fill=primary_color, font=font_subtitle)
    
    items = [
        "✔ Datos no publicados",
        "✔ Información técnica de entidades públicas",
        "✔ Respuestas formales y verificables",
        "✔ Insumos para propuestas y reformas"
    ]
    
    y_pos += 80
    for item in items:
        draw.text((130, y_pos), item, fill=text_color, font=font_body)
        y_pos += 60

    # Sección "¿Para qué sirve?"
    y_pos += 80
    draw.text((100, y_pos), "🚀 Potencia tus resultados:", fill=primary_color, font=font_subtitle)
    
    benefits = [
        "• Sustentar proyectos sociales",
        "• Respaldar iniciativas legislativas",
        "• Medir brechas reales y vacíos institucionales",
        "• Tomar decisiones basadas en datos oficiales"
    ]
    
    y_pos += 80
    for benefit in benefits:
        draw.text((130, y_pos), benefit, fill=text_color, font=font_body)
        y_pos += 60

    # Descargo de responsabilidad
    draw.rectangle([100, y_pos + 50, 1140, y_pos + 130], outline=primary_color, width=2)
    draw.text((width//2, y_pos + 90), "⚖ Servicio técnico-administrativo (No incluye representación jurídica)", 
              fill=text_color, font=ImageFont.truetype("arial.ttf", 30) if font_body else font_body, anchor="mm")

    # Footer / CTA
    draw.text((width//2, height-150), "La información correcta cambia el rumbo.", fill=primary_color, font=font_footer, anchor="mm")
    draw.text((width//2, height-80), "📲 AGENDA TU ASESORÍA", fill="#E91E63", font=font_title, anchor="mm")

    return canvas

# --- INTERFAZ STREAMLIT ---
st.set_page_config(page_title="Generador de Flyers Estratégicos", layout="centered")
st.title("🎨 Creador de Flyers Profesionales")
st.write("Sube tu logo y descarga el diseño final para tu servicio de Derechos de Petición.")

uploaded_logo = st.file_uploader("Carga el logo de tu proyecto (PNG recomendado)", type=["png", "jpg", "jpeg"])

if st.button("Generar Flyer"):
    result_img = generate_flyer(uploaded_logo)
    
    # Mostrar vista previa
    st.image(result_img, caption="Vista previa del Flyer", use_container_width=True)
    
    # Botón de descarga
    buf = io.BytesIO()
    result_img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Descargar Flyer en Alta Resolución",
        data=byte_im,
        file_name="flyer_derechos_peticion.png",
        mime="image/png"
    )