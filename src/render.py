from PIL import ImageFont

from PIL import Image
from PIL import ImageDraw

img_base = Image.open("assets/horario_base.png")

ancho = 602
alto = 272

x0 = 267
y0 = 420


def pintar_caja(dia, hora, draw):
    x = x0+(ancho*dia + 6*dia)
    y = y0+(alto*hora + 3*hora)

    draw.rectangle([x, y, x+ancho, y+alto], fill="#cacaca", outline=(0, 0, 0))


def pintar_clase(clase, draw):
    inicio_clase = 9 + clase.hora*2
    fin_clase = inicio_clase + 2

    # ponemos el inicio en formato string
    inicio_clase = str(inicio_clase) + ":00"
    fin_clase = str(fin_clase) + ":00"

    x = x0+(ancho*clase.dia + 6*clase.dia)
    y = y0+(alto*clase.hora + 3*clase.hora)

    # pintar caja
    pintar_caja(clase.dia, clase.hora, draw)

    # pintar hora de inicio y fin
    font_hora = ImageFont.truetype("arial.ttf", 35)
    draw.text((x+10, y+10), inicio_clase, font=font_hora, fill=(0, 0, 0))
    draw.text((x+ancho-100, y+alto-50), fin_clase, font=font_hora, fill=(0, 0, 0))

    # pintar nombre del grupo
    font_grupo = ImageFont.truetype("arial.ttf", 35)
    nombre_grupo = clase.grupo
    _, _, w, h = draw.textbbox((0, 0), nombre_grupo, font=font_grupo)

    draw.text(
        (x+(ancho-w)/2, y+(alto-h)/2 - 30),
        nombre_grupo,
        font=font_grupo,
        fill=(0, 0, 0)
    )

    # pintar nombre de la clase
    font_clase = ImageFont.truetype("arial.ttf", 60)
    _, _, w, h = draw.textbbox((0, 0), clase.asignatura, font=font_clase)
    draw.text(
        (x+(ancho-w)/2, y+(alto-h)/2+15),
        clase.asignatura,
        font=font_clase,
        fill=(0, 0, 0)
    )

    # pintar nombre del profesor
    font_profesor = ImageFont.truetype("arial.ttf", 25)
    _, _, w, h = draw.textbbox((0, 0), clase.profesor, font=font_profesor)
    draw.text(
        (x+(ancho-w)/2, y+(alto-h)/2+60),
        clase.profesor,
        font=font_profesor,
        fill=(0, 0, 0)
    )


def get_img_horario(clases):
    img = img_base.copy()

    draw = ImageDraw.Draw(img)

    for clase in clases:
        pintar_clase(
            clase,
            draw
        )

    return img
