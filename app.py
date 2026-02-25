import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Configuración de página
st.set_page_config(page_title="Generador de Flyers Estratégicos", layout="centered")

def get_font(size):
    """Carga una fuente disponible en el servidor o la predeterminada."""
    fonts_to_try = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "DejaVuSans.ttf",
        "Arial.ttf"
    ]
    for font_path in fonts_to_try:
        try:
            return ImageFont.truetype(font_path, size)
        except:
            continue
    return ImageFont.load_default()

def generate_flyer(logo_file):
    # Lienzo A4 proporcional (1240 x 1754)
    width, height = 1240, 1754
    canvas = Image.new('RGB', (width, height), color='#FFFFFF')
    draw = ImageDraw.Draw(canvas)

    # Paleta de Colores
    primary = "#1A237E"  # Azul Oxford
    gold = "#C5A059"     # Dorado Corporativo
    bg_light = "#F4F7F9" # Gris Azulado claro

    # --- DISEÑO ---
    # Encabezado
    draw.rectangle([0, 0, width, 420], fill=primary)
    
    # Fuentes
    font_h1 = get_font(75)
    font_h2 = get_font(50)
    font_p = get_font(38)
    font_cta = get_font(60)

    # Logo
    if logo_file:
        logo = Image.open(logo_file).convert("RGBA")
        logo.thumbnail((350, 180))
        canvas.paste(logo, (width//2 - logo.size[0]//2, 60), logo)

    # Título Principal
    draw.multiline_text((width//2, 580), 
                        "¿NECESITAS INFORMACIÓN OFICIAL\nPARA TU PROYECTO?", 
                        fill=primary, font=font_h1, anchor="mm", align="center")

    # Subtítulo
    draw.text((width//2, 720), "Diseñamos Derechos de Petición Estratégicos", 
              fill=gold, font=font_h2, anchor="mm")

    # Bloque 1: ¿Qué hacemos?
    y = 850
    draw.text((120, y), "🎯 ¿QUÉ HACEMOS?", fill=primary, font=font_h2)
    items = [
        "• Datos que no están publicados",
        "• Información técnica de entidades públicas",
        "• Respuestas formales y verificables",
        "• Insumos para fortalecer propuestas"
    ]
    y += 80
    for item in items:
        draw.text((150, y), item, fill="#333333", font=font_p)
        y += 60

    # Bloque 2: ¿Para qué sirve? (Con fondo sutil)
    y += 60
    draw.rectangle([80, y, width-80, y + 320], fill=bg_light, outline=gold, width=2)
    y_inner = y + 50
    draw.text((120, y_inner), "🚀 ¿PARA QUÉ TE SIRVE?", fill=primary, font=font_h2)
    benefits = [
        "✔ Sustentar proyectos sociales y legislativos",
        "✔ Medir brechas reales y vacíos institucionales",
        "✔ Tomar decisiones con información oficial"
    ]
    y_inner += 80
    for benefit in benefits:
        draw.text((150, y_inner), benefit, fill="#333333", font=font_p)
        y_inner += 60

    # Disclaimer
    draw.text((width//2, 1600), "⚖ Servicio técnico – administrativo. No incluye representación jurídica.", 
              fill="#777777", font=get_font(28), anchor="mm")

    # Footer CTA
    draw.text((width//2, 1680), "📲 AGENDA TU ASESORÍA", fill=primary, font=font_cta, anchor="mm")

    return canvas

# --- INTERFAZ ---
st.title("Flyer Generator 📄")
st.markdown("Genera materiales publicitarios para **Derechos de Petición Estratégicos**.")

uploaded_logo = st.file_uploader("1. Sube tu logo", type=["png", "jpg", "jpeg"])

if st.button("2. Generar Flyer Profesional"):
    with st.spinner("Diseñando..."):
        try:
            result_img = generate_flyer(uploaded_logo)
            st.image(result_img, use_container_width=True)
            
            # Preparar descarga
            buf = io.BytesIO()
            result_img.save(buf, format="PNG")
            st.download_button(
                label="📥 Descargar Flyer en Alta Resolución",
                data=buf.getvalue(),
                file_name="flyer_estrategico.png",
                mime="image/png"
            )
        except Exception as e:
            st.error(f"Ocurrió un error al generar la imagen: {e}")
