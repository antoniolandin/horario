class Asignatura:
    def __init__(self, id, nombre, numero_clases_semana, curso):
        self.id = id
        self.nombre = nombre
        self.numero_clases_semana = numero_clases_semana

    def __str__(self):
        return f"{self.nombre}"


class Clase:
    def __init__(self, dia, hora, id_asignatura, profesor, grupo):
        self.hora = hora
        self.dia = dia
        self.id_asignatura = id_asignatura
        self.profesor = profesor
        self.grupo = grupo

    def __str__(self):
        hora_inicio_clase = 9 + self.hora * 2
        hora_fin_clase = hora_inicio_clase + 2

        return f"{hora_inicio_clase}:00 - {hora_fin_clase}:00 - {self.id_asignatura} - {self.profesor} - {self.grupo}"


class Profesor:
    def __init__(self, id, nombre, asignaturas_asignadas):
        self.id = id
        self.nombre = nombre
        self.asignaturas = asignaturas_asignadas

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

horario_INSO1A = [
    Clase(
        dia=0,
        hora=0,
        id_asignatura=lab_redes.id,
        profesor=miguel_fernandez.id,
        grupo=0
    ),
    Clase(
        dia=0,
        hora=1,
        id_asignatura=web.id,
        profesor=ramona.id,
        grupo=0
    ),
    Clase(
        dia=1,
        hora=1,
        id_asignatura=pensamiento_creativo.id,
        profesor=bernardo.id,
        grupo=0
    ),
    Clase(
        dia=1,
        hora=2,
        id_asignatura=programacion.id,
        profesor=sergio.id,
        grupo=0
    ),
    Clase(
        dia=2,
        hora=0,
        id_asignatura=proyectos_1.id,
        profesor=luis.id,
        grupo=0
    ),
    Clase(
        dia=2,
        hora=1,
        id_asignatura=matematica_discreta.id,
        profesor=ana.id,
        grupo=0
    ),
    Clase(
        dia=3,
        hora=0,
        id_asignatura=lab_redes.id,
        profesor=miguel_fernandez.id,
        grupo=0
    ),
    Clase(
        dia=3,
        hora=1,
        id_asignatura=matematica_discreta.id,
        profesor=ana.id,
        grupo=0
    ),
    Clase(
        dia=4,
        hora=1,
        id_asignatura=web.id,
        profesor=ramona.id,
        grupo=0
    ),
    Clase(
        dia=4,
        hora=2,
        id_asignatura=programacion.id,
        profesor=sergio.id,
        grupo=0
    ),
]

horario_INSO1B = [
    Clase(
        dia=0,
        hora=1,
        id_asignatura=programacion.id,
        profesor=alfonso.id,
        grupo=1
    ),
    Clase(
        dia=0,
        hora=2,
        id_asignatura=lab_redes.id,
        profesor=hector.id,
        grupo=1
    ),
    Clase(
        dia=1,
        hora=1,
        id_asignatura=programacion.id,
        profesor=alfonso.id,
        grupo=1
    ),
    Clase(
        dia=1,
        hora=2,
        id_asignatura=web.id,
        profesor=ramona.id,
        grupo=1
    ),
    Clase(
        dia=2,
        hora=0,
        id_asignatura=web.id,
        profesor=ramona.id,
        grupo=1
    ),
    Clase(
        dia=2,
        hora=1,
        id_asignatura=matematica_discreta.id,
        profesor=jorge.id,
        grupo=1
    ),
    Clase(
        dia=3,
        hora=1,
        id_asignatura=pensamiento_creativo.id,
        profesor=barbara.id,
        grupo=1
    ),
    Clase(
        dia=3,
        hora=2,
        id_asignatura=lab_redes.id,
        profesor=hector.id,
        grupo=1
    ),
    Clase(
        dia=4,
        hora=0,
        id_asignatura=proyectos_1.id,
        profesor=luis.id,
        grupo=1
    ),
    Clase(
        dia=4,
        hora=1,
        id_asignatura=matematica_discreta.id,
        profesor=jorge.id,
        grupo=1
    )
]

horario_INSO1C = [
    Clase(
        dia=0,
        hora=1,
        id_asignatura=proyectos_1.id,
        profesor=luis.id,
        grupo=2
    ),
    Clase(
        dia=0,
        hora=2,
        id_asignatura=web.id,
        profesor=ramona.id,
        grupo=2
    ),
    Clase(
        dia=1,
        hora=1,
        id_asignatura=lab_redes.id,
        profesor=elena.id,
        grupo=2
    ),
    Clase(
        dia=1,
        hora=2,
        id_asignatura=programacion.id,
        profesor=rodrigo.id,
        grupo=2
    ),
    Clase(
        dia=2,
        hora=0,
        id_asignatura=matematica_discreta.id,
        profesor=jorge.id,
        grupo=2
    ),
    Clase(
        dia=2,
        hora=1,
        id_asignatura=lab_redes.id,
        profesor=elena.id,
        grupo=2
    ),
    Clase(
        dia=3,
        hora=1,
        id_asignatura=web.id,
        profesor=ramona.id,
        grupo=2
    ),
    Clase(
        dia=3,
        hora=2,
        id_asignatura=programacion.id,
        profesor=rodrigo.id,
        grupo=2
    ),
    Clase(
        dia=4,
        hora=0,
        id_asignatura=matematica_discreta.id,
        profesor=jorge.id,
        grupo=2
    ),
    Clase(
        dia=4,
        hora=1,
        id_asignatura=pensamiento_creativo.id,
        profesor=barbara.id,
        grupo=2
    )
]

horario_INSO2A = [
    Clase(
        dia=0,
        hora=4,
        id_asignatura=sistemas_operativos.id,
        profesor=carlos_vallez.id,
        grupo=3
    ),
    Clase(
        dia=0,
        hora=5,
        id_asignatura=programacion_objetos.id,
        profesor=miguel_mesas.id,
        grupo=3
    ),
    Clase(
        dia=1,
        hora=4,
        id_asignatura=estadistica.id,
        profesor=carlos_gordon.id,
        grupo=3
    ),
    Clase(
        dia=1,
        hora=5,
        id_asignatura=sistemas_operativos.id,
        profesor=carlos_vallez.id,
        grupo=3
    ),
    Clase(
        dia=2,
        hora=4,
        id_asignatura=redes_ordenadores.id,
        profesor=constantino.id,
        grupo=3
    ),
    Clase(
        dia=2,
        hora=5,
        asignaturas_asignadas=programacion_objetos.id,
        profesor=miguel_mesas.id,
        grupo=3
    ),
    Clase(
        dia=3,
        hora=3,
        id_asignatura=proyectos_2.id,
        profesor=eduardo.id,
        grupo=3
    ),
    Clase(
        dia=3,
        hora=4,
        id_asignatura=estadistica.id,
        profesor=carlos_gordon.id,
        grupo=3
    ),
    Clase(
        dia=4,
        hora=3,
        id_asignatura=composicion_visual.id,
        profesor=ruben.id,
        grupo=3
    ),
    Clase(
        dia=4,
        hora=4,
        id_asignatura=redes_ordenadores.id,
        profesor=constantino.id,
        grupo=3
    )
]

horario_INSO2B = [
    Clase(
        dia=0,
        hora=3,
        id_asignatura=sistemas_operativos.id,
        profesor=carlos_vallez.id,
        grupo=4
    ),
    Clase(
        dia=0,
        hora=4,
        id_asignatura=redes_ordenadores.id,
        profesor=constantino.id,
        grupo=4
    ),
    Clase(
        dia=1,
        hora=3,
        id_asignatura=sistemas_operativos.id,
        profesor=carlos_vallez.id,
        grupo=4
    ),
    Clase(
        dia=1,
        hora=4,
        id_asignatura=programacion_objetos.id,
        profesor=javier.id,
        grupo=4
    ),
    Clase(
        dia=2,
        hora=3,
        id_asignatura=estadistica.id,
        profesor=carlos_mora.id,
        grupo=4
    ),
    Clase(
        dia=2,
        hora=4,
        id_asignatura=programacion_objetos.id,
        profesor=javier.id,
        grupo=4
    ),
    Clase(
        dia=3,
        hora=3,
        id_asignatura=estadistica.id,
        profesor=carlos_mora.id,
        grupo=4
    ),
    Clase(
        dia=3,
        hora=4,
        id_asignatura=proyectos_2.id,
        profesor=eduardo.id,
        grupo=4
    ),
    Clase(
        dia=4,
        hora=3,
        id_asignatura=redes_ordenadores.id,
        profesor=constantino.id,
        grupo=4
    ),
    Clase(
        dia=4,
        hora=4,
        id_asignatura=composicion_visual.id,
        profesor=ruben.id,
        grupo=4
    )
]

horario_INSO2C = [
    Clase(
        dia=0,
        hora=3,
        id_asignatura=redes_ordenadores.id,
        profesor=constantino.id,
        grupo=5
    ),
    Clase(
        dia=0,
        hora=4,
        id_asignatura=sistemas_operativos.id,
        profesor=sergio.id,
        grupo=5
    ),
    Clase(
        dia=1,
        hora=3,
        id_asignatura=estadistica.id,
        profesor=carlos_mora.id,
        grupo=5
    ),
    Clase(
        dia=1,
        hora=4,
        id_asignatura=programacion_objetos.id,
        profesor=rodrigo.id,
        grupo=5
    ),
    Clase(
        dia=2,
        hora=3,
        id_asignatura=redes_ordenadores.id,
        profesor=constantino.id,
        grupo=5
    ),
    Clase(
        dia=2,
        hora=4,
        id_asignatura=estadistica.id,
        profesor=carlos_mora.id,
        grupo=5
    ),
    Clase(
        dia=3,
        hora=4,
        id_asignatura=programacion_objetos.id,
        profesor=rodrigo.id,
        grupo=5
    ),
    Clase(
        dia=3,
        hora=5,
        id_asignatura=proyectos_2.id,
        profesor=eduardo.id,
        grupo=5
    ),
    Clase(
        dia=4,
        hora=4,
        id_asignatura=sistemas_operativos.id,
        profesor=sergio.id,
        grupo=5
    ),
    Clase(
        dia=4,
        hora=5,
        id_asignatura=composicion_visual.id,
        profesor=ruben.id,
        grupo=5
    )
]

horario_INSO2D = [
    Clase(
        dia=1,
        hora=3,
        id_asignatura=estadistica.id,
        profesor=carlos_gordon.id,
        grupo=6
    ),
    Clase(
        dia=3,
        hora=3,
        id_asignatura=estadistica.id,
        profesor=carlos_gordon.id,
        grupo=6
        )
]
