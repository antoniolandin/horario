from clase import clases_INSOA, clases_INSOB, clases_INSO1C, clases_INSO2A
from clase import clases_INSO2B, clases_INSO2C, clases_INSO2D

from asignatura import web, lab_redes, pensamiento_creativo, composicion_visual
from asignatura import estadistica, redes_ordenadores, proyectos_2, proyectos_1

from horario import Horario

import itertools

clases = [
    clases_INSOA,
    clases_INSOB,
    clases_INSO1C,
    clases_INSO2A,
    clases_INSO2B,
    clases_INSO2C,
    clases_INSO2D
]

asignaturas_cuatrimestre = [
    web,
    lab_redes,
    pensamiento_creativo,
    composicion_visual,
    estadistica,
    redes_ordenadores,
    proyectos_1,
    proyectos_2
]


def bloque_clase(asignatura, grupo):

    bloque = []

    for clase in clases:
        for c in clase:
            if c.asignatura == asignatura and c.grupo == grupo:
                bloque.append(c)

    return bloque


def bloques_por_asignaturas(asignaturas):
    bloques_asignatura = []

    for asignatura in asignaturas_cuatrimestre:

        bloques = []

        for grupo in range(len(clases)):
            bloque = bloque_clase(asignatura, grupo)

            # como hay grupos que no tienen asignaturas no se añaden
            if len(bloque) > 0:
                bloques.append(bloque)

        bloques_asignatura.append(bloques)

    return bloques_asignatura


def generar_horarios(bloques_por_asignatura):
    bloques_asignatura = bloques_por_asignatura(asignaturas_cuatrimestre)
    horarios_bloques = list(itertools.product(*bloques_asignatura))
    horarios = []

    # pasar los bloques a clases sueltas
    for horario in horarios_bloques:
        clases_horario = []

        for bloque in horario:
            for clase in bloque:
                clases_horario.append(clase)

        if horario_valido(clases_horario):
            horarios.append(clases_horario)

    return horarios


def generar_mapa_horario(horario):
    mapa_horario = [[False for _ in range(6)] for _ in range(5)]

    for clase in horario:
        mapa_horario[clase.dia][clase.hora] = True

    return mapa_horario


def horario_valido(clases_horario):
    for c1 in clases_horario:
        for c2 in clases_horario:
            if c1 != c2 and c1.dia == c2.dia and c1.hora == c2.hora:
                return False

    return True


def filtrar_horario(mapa_horario, max_clases_dia=3, max_espacios=1):

    espacios = 0

    for dia in mapa_horario:
        num_clases = sum(dia)
        clase_actual = 0

        if num_clases > max_clases_dia:
            return False

        for hora in dia:
            if hora:
                clase_actual += 1
            else:
                if clase_actual > 0 and clase_actual < num_clases:
                    espacios += 1

    if espacios > max_espacios:
        return False

    return True


if __name__ == '__main__':
    horarios = generar_horarios(bloques_por_asignaturas)

    for horario in horarios:
        mapa_horario = generar_mapa_horario(horario)

        if filtrar_horario(mapa_horario):
            horario_filtrado = Horario(horario)
            horario_filtrado.cargar_imagen()
            horario_filtrado.guardar()
