class Asignatura:
    def __init__(self, id, nombre, numero_clases_semana, curso):
        self.id = id
        self.nombre = nombre
        self.numero_clases_semana = numero_clases_semana

    def __str__(self):
        return f"{self.nombre}"


lab_redes = Asignatura(
    id=1,
    nombre="Laboratorio de Redes y Sistemas Operativos",
    numero_clases_semana=2,
    curso=1
)

web = Asignatura(
    id=2,
    nombre="Fundamentos del Desarrollo Web",
    numero_clases_semana=2,
    curso=1
)


pensamiento_creativo = Asignatura(
    id=3,
    nombre="Pensamiento Creativo",
    numero_clases_semana=1,
    curso=1
)

programacion = Asignatura(
    id=4,
    nombre="Introducción a la Programación 1",
    numero_clases_semana=2,
    curso=1
)


proyectos_1 = Asignatura(
    id=5,
    nombre="Proyectos 1",
    numero_clases_semana=1,
    curso=1
)


matematica_discreta = Asignatura(
    id=6,
    nombre="Lógica y Matemática Discreta",
    numero_clases_semana=2,
    curso=1
)

sistemas_operativos = Asignatura(
    id=7,
    nombre="Sistemas Operativos",
    numero_clases_semana=2,
    curso=2
)


programacion_objetos = Asignatura(
    id=8,
    nombre="Programación Orientada a Objetos",
    numero_clases_semana=2,
    curso=2
)


estadistica = Asignatura(
    id=9,
    nombre="Probabilidad y Estadística",
    numero_clases_semana=2,
    curso=2
)

redes_ordenadores = Asignatura(
    id=10,
    nombre="Redes Ordenadores",
    numero_clases_semana=2,
    curso=2
)

composicion_visual = Asignatura(
    id=11,
    nombre="Fundamentos de la Composición Visual",
    numero_clases_semana=1,
    curso=2
)

proyectos_2 = Asignatura(
    id=12,
    nombre="Proyectos 2",
    numero_clases_semana=1,
    curso=2
)


asignaturas = [
        lab_redes,
        web,
        pensamiento_creativo,
        programacion,
        proyectos_1,
        matematica_discreta,
        sistemas_operativos,
        programacion_objetos,
        estadistica,
        redes_ordenadores,
        composicion_visual
]
