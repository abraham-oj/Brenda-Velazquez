import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont

# --- CONFIGURACIÓN A PRUEBA DE ERRORES ---
# Esto hace que el script funcione sin importar desde dónde lo ejecutes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = BASE_DIR
OUTPUT_DIR = os.path.join(BASE_DIR, "../images/noticias_generadas")

# Paleta Brenda
COLOR_VERDE_CLARO = (118, 188, 33)
COLOR_BLANCO = (255, 255, 255)
COLOR_TEXTO_SECUNDARIO = (240, 240, 240)

# Datos de las noticias
DATOS_NOTICIAS = {
    "noticia_1.jpg": {
        "titulo": "JUSTICIA A TU LEALTAD",
        "cuerpo": "Recuperaremos la Prima de Antigüedad calculada legalmente para retribuir tus años de servicio.",
        "tag": "DERECHO"
    },
    "noticia_2.jpg": {
        "titulo": "MÉRITO, NO DEDAZO",
        "cuerpo": "Escalafón transparente basado en capacidad y preparación. Cero favoritismos en los ascensos.",
        "tag": "TRANSPARENCIA"
    },
    "noticia_3.jpg": {
        "titulo": "MÁS OPORTUNIDADES",
        "cuerpo": "Creación de nuevas plazas formales para atender las necesidades reales de las dependencias.",
        "tag": "CRECIMIENTO"
    }
}

def garantizar_entorno():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    font_path = os.path.join(BASE_DIR, "Montserrat-Bold.ttf")
    if not os.path.exists(font_path):
        print("⬇️ Descargando fuente Montserrat...")
        url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/ttf/Montserrat-Bold.ttf"
        try:
            urllib.request.urlretrieve(url, font_path)
        except:
            pass

def crear_gradiente_elegante(size):
    width, height = size
    overlay = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    start_y = int(height * 0.4)
    for y in range(start_y, height):
        progress = (y - start_y) / (height - start_y)
        alpha = int(240 * (progress ** 2))
        draw.line([(0, y), (width, y)], fill=(0, 20, 10, alpha))
    return overlay

def envolver_texto(text, font, max_width, draw):
    lines = []
    words = text.split()
    current_line = words[0]
    for word in words[1:]:
        bbox = draw.textbbox((0, 0), current_line + " " + word, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

def main():
    garantizar_entorno()
    font_path = os.path.join(BASE_DIR, "Montserrat-Bold.ttf")

    try:
        font_tag = ImageFont.truetype(font_path, 35)
        font_titulo = ImageFont.truetype(font_path, 90)
        font_cuerpo = ImageFont.truetype(font_path, 45)
    except:
        font_tag = ImageFont.load_default()
        font_titulo = ImageFont.load_default()
        font_cuerpo = ImageFont.load_default()

    print(f"🎨 Buscando fotos en: {INPUT_DIR}")

    for archivo, info in DATOS_NOTICIAS.items():
        ruta_origen = os.path.join(INPUT_DIR, archivo)

        if not os.path.exists(ruta_origen):
            print(f"❌ ERROR: Aún no has puesto '{archivo}' en la carpeta public/fotos_noticias")
            continue

        img = Image.open(ruta_origen).convert('RGB')

        # Crop cuadrado
        target = 1080
        aspect = img.width / img.height
        if aspect > 1:
            new_w = int(target * aspect)
            new_h = target
        else:
            new_w = target
            new_h = int(target / aspect)

        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        left = (new_w - target)/2
        top = (new_h - target)/2
        img = img.crop((left, top, left+target, top+target))

        # Magia
        gradiente = crear_gradiente_elegante(img.size)
        img.paste(gradiente, (0,0), gradiente)

        draw = ImageDraw.Draw(img)

        # Textos
        margin_left = 60
        tag_y = 680

        # Tag
        bbox_tag = draw.textbbox((0,0), info['tag'], font=font_tag)
        tag_w = bbox_tag[2] - bbox_tag[0]
        draw.rectangle([(margin_left, tag_y), (margin_left + tag_w + 40, tag_y + 50)], fill=COLOR_VERDE_CLARO)
        draw.text((margin_left + 20, tag_y + 5), info['tag'], font=font_tag, fill=COLOR_BLANCO)

        # Título y Cuerpo
        draw.text((margin_left, tag_y + 70), info['titulo'], font=font_titulo, fill=COLOR_BLANCO)

        body_y = tag_y + 180
        wrapped = envolver_texto(info['cuerpo'], font_cuerpo, 960, draw)
        for line in wrapped:
            draw.text((margin_left, body_y), line, font=font_cuerpo, fill=COLOR_TEXTO_SECUNDARIO)
            body_y += 55

        out_name = f"Post_{info['tag']}.png"
        img.save(os.path.join(OUTPUT_DIR, out_name))
        print(f"✅ Generado: {out_name}")

if __name__ == "__main__":
    main()