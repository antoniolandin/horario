from asignatura import lab_redes, web, pensamiento_creativo, programacion
from asignatura import sistemas_operativos, proyectos_1, matematica_discreta
from asignatura import programacion_objetos, estadistica, redes_ordenadores
from asignatura import composicion_visual, proyectos_2

from profesor import miguel_fernandez, ramona, bernardo, sergio, luis, ana, elena
from profesor import rodrigo, jorge, barbara, alfonso, hector, miguel_mesas
from profesor import carlos_gordon, carlos_vallez, constantino, ruben, eduardo, javier
from profesor import carlos_mora

from clase import Clase

from render import pintar_clase

from PIL import Image
from PIL import ImageDraw


class Horario:
    def __init__(self, nombre, clases):
        self.nombre = nombre
        self.clases = clases

    def pintar(self):
        horario = Image.open("horario_base.png")
        draw = ImageDraw.Draw(horario)

        for clase in self.clases:
            pintar_clase(
                clase,
                draw=draw
            )

        # horario.save(f"{self.nombre}.png")
        horario.show()


clases_INSOA = [
    Clase(
        dia=0,
        hora=0,
        asignatura=lab_redes,
        profesor=miguel_fernandez,
        grupo=0
    ),
    Clase(
        dia=0,
        hora=1,
        asignatura=web,
        profesor=ramona,
        grupo=0
    ),
    Clase(
        dia=1,
        hora=1,
        asignatura=pensamiento_creativo,
        profesor=bernardo,
        grupo=0
    ),
    Clase(
        dia=1,
        hora=2,
        asignatura=programacion,
        profesor=sergio,
        grupo=0
    ),
    Clase(
        dia=2,
        hora=0,
        asignatura=proyectos_1,
        profesor=luis,
        grupo=0
    ),
    Clase(
        dia=2,
        hora=1,
        asignatura=matematica_discreta,
        profesor=ana,
        grupo=0
    ),
    Clase(
        dia=3,
        hora=0,
        asignatura=lab_redes,
        profesor=miguel_fernandez,
        grupo=0
    ),
    Clase(
        dia=3,
        hora=1,
        asignatura=matematica_discreta,
        profesor=ana,
        grupo=0
    ),
    Clase(
        dia=4,
        hora=1,
        asignatura=web,
        profesor=ramona,
        grupo=0
    ),
    Clase(
        dia=4,
        hora=2,
        asignatura=programacion,
        profesor=sergio,
        grupo=0
    ),
]

clases_INSOB = [
    Clase(
        dia=0,
        hora=1,
        asignatura=programacion,
        profesor=alfonso,
        grupo=1
    ),
    Clase(
        dia=0,
        hora=2,
        asignatura=lab_redes,
        profesor=hector,
        grupo=1
    ),
    Clase(
        dia=1,
        hora=1,
        asignatura=programacion,
        profesor=alfonso,
        grupo=1
    ),
    Clase(
        dia=1,
        hora=2,
        asignatura=web,
        profesor=ramona,
        grupo=1
    ),
    Clase(
        dia=2,
        hora=0,
        asignatura=web,
        profesor=ramona,
        grupo=1
    ),
    Clase(
        dia=2,
        hora=1,
        asignatura=matematica_discreta,
        profesor=jorge,
        grupo=1
    ),
    Clase(
        dia=3,
        hora=1,
        asignatura=pensamiento_creativo,
        profesor=barbara,
        grupo=1
    ),
    Clase(
        dia=3,
        hora=2,
        asignatura=lab_redes,
        profesor=hector,
        grupo=1
    ),
    Clase(
        dia=4,
        hora=0,
        asignatura=proyectos_1,
        profesor=luis,
        grupo=1
    ),
    Clase(
        dia=4,
        hora=1,
        asignatura=matematica_discreta,
        profesor=jorge,
        grupo=1
    )
]

clases_INSO1C = [
    Clase(
        dia=0,
        hora=1,
        asignatura=proyectos_1,
        profesor=luis,
        grupo=2
    ),
    Clase(
        dia=0,
        hora=2,
        asignatura=web,
        profesor=ramona,
        grupo=2
    ),
    Clase(
        dia=1,
        hora=1,
        asignatura=lab_redes,
        profesor=elena,
        grupo=2
    ),
    Clase(
        dia=1,
        hora=2,
        asignatura=programacion,
        profesor=rodrigo,
        grupo=2
    ),
    Clase(
        dia=2,
        hora=0,
        asignatura=matematica_discreta,
        profesor=jorge,
        grupo=2
    ),
    Clase(
        dia=2,
        hora=1,
        asignatura=lab_redes,
        profesor=elena,
        grupo=2
    ),
    Clase(
        dia=3,
        hora=1,
        asignatura=web,
        profesor=ramona,
        grupo=2
    ),
    Clase(
        dia=3,
        hora=2,
        asignatura=programacion,
        profesor=rodrigo,
        grupo=2
    ),
    Clase(
        dia=4,
        hora=0,
        asignatura=matematica_discreta,
        profesor=jorge,
        grupo=2
    ),
    Clase(
        dia=4,
        hora=1,
        asignatura=pensamiento_creativo,
        profesor=barbara,
        grupo=2
    )
]

clases_INSO2A = [
    Clase(
        dia=0,
        hora=4,
        asignatura=sistemas_operativos,
        profesor=carlos_vallez,
        grupo=3
    ),
    Clase(
        dia=0,
        hora=5,
        asignatura=programacion_objetos,
        profesor=miguel_mesas,
        grupo=3
    ),
    Clase(
        dia=1,
        hora=4,
        asignatura=estadistica,
        profesor=carlos_gordon,
        grupo=3
    ),
    Clase(
        dia=1,
        hora=5,
        asignatura=sistemas_operativos,
        profesor=carlos_vallez,
        grupo=3
    ),
    Clase(
        dia=2,
        hora=4,
        asignatura=redes_ordenadores,
        profesor=constantino,
        grupo=3
    ),
    Clase(
        dia=2,
        hora=5,
        asignatura=programacion_objetos,
        profesor=miguel_mesas,
        grupo=3
    ),
    Clase(
        dia=3,
        hora=3,
        asignatura=proyectos_2,
        profesor=eduardo,
        grupo=3
    ),
    Clase(
        dia=3,
        hora=4,
        asignatura=estadistica,
        profesor=carlos_gordon,
        grupo=3
    ),
    Clase(
        dia=4,
        hora=3,
        asignatura=composicion_visual,
        profesor=ruben,
        grupo=3
    ),
    Clase(
        dia=4,
        hora=4,
        asignatura=redes_ordenadores,
        profesor=constantino,
        grupo=3
    )
]

clases_INSO2B = [
    Clase(
        dia=0,
        hora=3,
        asignatura=sistemas_operativos,
        profesor=carlos_vallez,
        grupo=4
    ),
    Clase(
        dia=0,
        hora=4,
        asignatura=redes_ordenadores,
        profesor=constantino,
        grupo=4
    ),
    Clase(
        dia=1,
        hora=3,
        asignatura=sistemas_operativos,
        profesor=carlos_vallez,
        grupo=4
    ),
    Clase(
        dia=1,
        hora=4,
        asignatura=programacion_objetos,
        profesor=javier,
        grupo=4
    ),
    Clase(
        dia=2,
        hora=3,
        asignatura=estadistica,
        profesor=carlos_mora,
        grupo=4
    ),
    Clase(
        dia=2,
        hora=4,
        asignatura=programacion_objetos,
        profesor=javier,
        grupo=4
    ),
    Clase(
        dia=3,
        hora=3,
        asignatura=estadistica,
        profesor=carlos_mora,
        grupo=4
    ),
    Clase(
        dia=3,
        hora=4,
        asignatura=proyectos_2,
        profesor=eduardo,
        grupo=4
    ),
    Clase(
        dia=4,
        hora=3,
        asignatura=redes_ordenadores,
        profesor=constantino,
        grupo=4
    ),
    Clase(
        dia=4,
        hora=4,
        asignatura=composicion_visual,
        profesor=ruben,
        grupo=4
    )
]

clases_INSO2C = [
    Clase(
        dia=0,
        hora=3,
        asignatura=redes_ordenadores,
        profesor=constantino,
        grupo=5
    ),
    Clase(
        dia=0,
        hora=4,
        asignatura=sistemas_operativos,
        profesor=sergio,
        grupo=5
    ),
    Clase(
        dia=1,
        hora=3,
        asignatura=estadistica,
        profesor=carlos_mora,
        grupo=5
    ),
    Clase(
        dia=1,
        hora=4,
        asignatura=programacion_objetos,
        profesor=rodrigo,
        grupo=5
    ),
    Clase(
        dia=2,
        hora=3,
        asignatura=redes_ordenadores,
        profesor=constantino,
        grupo=5
    ),
    Clase(
        dia=2,
        hora=4,
        asignatura=estadistica,
        profesor=carlos_mora,
        grupo=5
    ),
    Clase(
        dia=3,
        hora=4,
        asignatura=programacion_objetos,
        profesor=rodrigo,
        grupo=5
    ),
    Clase(
        dia=3,
        hora=5,
        asignatura=proyectos_2,
        profesor=eduardo,
        grupo=5
    ),
    Clase(
        dia=4,
        hora=4,
        asignatura=sistemas_operativos,
        profesor=sergio,
        grupo=5
    ),
    Clase(
        dia=4,
        hora=5,
        asignatura=composicion_visual,
        profesor=ruben,
        grupo=5
    )
]

clases_INSO2D = [
    Clase(
        dia=1,
        hora=3,
        asignatura=estadistica,
        profesor=carlos_gordon,
        grupo=6
    ),
    Clase(
        dia=3,
        hora=3,
        asignatura=estadistica,
        profesor=carlos_gordon,
        grupo=6
        )
]

horario_INSO1A = Horario("INSO1A", clases_INSOA)
horario_INSO1B = Horario("INSO1B", clases_INSOB)
horario_INSO1C = Horario("INSO1C", clases_INSO1C)
horario_INSO2A = Horario("INSO2A", clases_INSO2A)
horario_INSO2B = Horario("INSO2B", clases_INSO2B)
horario_INSO2C = Horario("INSO2C", clases_INSO2C)
horario_INSO2D = Horario("INSO2D", clases_INSO2D)
