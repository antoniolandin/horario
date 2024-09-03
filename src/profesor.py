from asignatura import lab_redes, web, pensamiento_creativo, programacion
from asignatura import sistemas_operativos, proyectos_1, matematica_discreta
from asignatura import programacion_objetos, estadistica, redes_ordenadores
from asignatura import composicion_visual, proyectos_2


class Profesor:
    def __init__(self, id, nombre, asignaturas_asignadas):
        self.id = id
        self.nombre = nombre
        self.asignaturas = asignaturas_asignadas

    def __str__(self):
        return f"{self.nombre}"


miguel_fernandez = Profesor(
    id=1,
    nombre="Miguel A. Fernández",
    asignaturas_asignadas=[lab_redes.id]
)

ramona = Profesor(
    id=2,
    nombre="Ramona Ruiz",
    asignaturas_asignadas=[web.id]
)

bernardo = Profesor(
    id=3,
    nombre="Bernardo Martínez",
    asignaturas_asignadas=[pensamiento_creativo.id]
)

sergio = Profesor(
        id=4,
        nombre="Sergio Bermúdez",
        asignaturas_asignadas=[programacion.id, sistemas_operativos.id]
)

luis = Profesor(
    id=5,
    nombre="Luis Miguel Campoy",
    asignaturas_asignadas=[proyectos_1.id]
)

ana = Profesor(
    id=6,
    nombre="Ana Isabel Sánchez",
    asignaturas_asignadas=[matematica_discreta.id, proyectos_2.id]
)

elena = Profesor(
    id=7,
    nombre="Elena García",
    asignaturas_asignadas=[lab_redes.id]
)

rodrigo = Profesor(
    id=8,
    nombre="Rodrigo Alonso",
    asignaturas_asignadas=[programacion.id]
)

jorge = Profesor(
    id=9,
    nombre="Jorge Tesch",
    asignaturas_asignadas=[matematica_discreta.id]
)

barbara = Profesor(
    id=10,
    nombre="Bárbara Sainza",
    asignaturas_asignadas=[pensamiento_creativo.id]
)

alfonso = Profesor(
    id=11,
    nombre="Alfonso Castro",
    asignaturas_asignadas=[programacion.id]
)

hector = Profesor(
    id=12,
    nombre="Héctor Paredes",
    asignaturas_asignadas=[lab_redes.id]
)

miguel_mesas = Profesor(
    id=13,
    nombre="Miguel A. Mesas",
    asignaturas_asignadas=[programacion_objetos.id]
)

carlos_gordon = Profesor(
    id=14,
    nombre="Carlos Gordón",
    asignaturas_asignadas=[estadistica.id]
)

carlos_vallez = Profesor(
    id=15,
    nombre="Carlos Vallez",
    asignaturas_asignadas=[sistemas_operativos.id]
)

constantino = Profesor(
    id=16,
    nombre="Constantino Malagón",
    asignaturas_asignadas=[redes_ordenadores.id]
)

ruben = Profesor(
    id=17,
    nombre="Rubén de la Prida",
    asignaturas_asignadas=[composicion_visual.id]
)

eduardo = Profesor(
    id=18,
    nombre="Eduardo Arriols",
    asignaturas_asignadas=[proyectos_2.id]
)

javier = Profesor(
    id=19,
    nombre="Fco. Javier Fernández",
    asignaturas_asignadas=[programacion_objetos.id]
)

carlos_mora = Profesor(
    id=20,
    nombre="Carlos Mora",
    asignaturas_asignadas=[estadistica.id]
)

profesores = [
    miguel_fernandez,
    ramona,
    bernardo,
    sergio,
    luis,
    ana,
    elena,
    rodrigo,
    jorge,
    barbara,
    alfonso,
    hector,
    miguel_mesas,
    carlos_gordon,
    carlos_vallez,
    constantino,
    ruben,
    eduardo,
    javier,
    carlos_mora
]
