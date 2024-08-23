from clase import clases_INSOA, clases_INSOB, clases_INSO1C, clases_INSO2A
from clase import clases_INSO2B, clases_INSO2C, clases_INSO2D

from render import pintar_clase

from PIL import Image
from PIL import ImageDraw

import random
import string


class Horario:
    def __init__(self, clases):
        self.clases = clases
        self.img = Image.open("horario_base.png")

    def cargar_imagen(self):
        draw = ImageDraw.Draw(self.img)

        for clase in self.clases:
            pintar_clase(
                clase,
                draw=draw
            )

    def mostrar(self):
        self.img.show()

    def guardar(self):
        random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.img.save(f"horarios/{random_name}.png")


horario_INSO1A = Horario(clases_INSOA)
horario_INSO1B = Horario(clases_INSOB)
horario_INSO1C = Horario(clases_INSO1C)
horario_INSO2A = Horario(clases_INSO2A)
horario_INSO2B = Horario(clases_INSO2B)
horario_INSO2C = Horario(clases_INSO2C)
horario_INSO2D = Horario(clases_INSO2D)
