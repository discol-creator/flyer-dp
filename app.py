def generate_flyer(logo_file):
    # Lienzo
    width, height = 1240, 1754
    canvas = Image.new('RGB', (width, height), color='#FFFFFF')
    draw = ImageDraw.Draw(canvas)

    # Colores
    primary_color = "#1A237E"
    text_color = "#333333"

    # --- MANEJO DE FUENTES SEGURO ---
    def get_font(size):
        try:
            # Esta fuente suele estar presente en sistemas Linux de Streamlit
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        except:
            try:
                # Intento alternativo para otros entornos Linux
                return ImageFont.truetype("DejaVuSans.ttf", size)
            except:
                # Si todo falla, usa la fuente básica (se ve simple pero no rompe la app)
                return ImageFont.load_default()

    font_title = get_font(80)
    font_subtitle = get_font(55)
    font_body = get_font(40)
    font_disclaimer = get_font(30)

    # --- DISEÑO ---
    draw.rectangle([0, 0, width, 400], fill=primary_color)

    if logo_file:
        logo = Image.open(logo_file).convert("RGBA")
        logo.thumbnail((300, 150))
        canvas.paste(logo, (width//2 - logo.size[0]//2, 50), logo)

    # Título
    title_text = "¿NECESITAS INFORMACIÓN OFICIAL\nPARA FORTALECER TU PROYECTO?"
    draw.multiline_text((width//2, 550), title_text, fill=primary_color, font=font_title, anchor="mm", align="center")

    # Cuerpo (Ejemplo de uno de los textos que te daba error)
    y_pos = 1400 
    draw.text((width//2, y_pos), "⚖ Servicio técnico – administrativo. No incluye representación jurídica.", 
              fill=text_color, font=font_disclaimer, anchor="mm")

    # ... (El resto de tu lógica de dibujado de texto sigue igual, pero usando get_font)

    return canvas
