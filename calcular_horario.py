from clase import clases_INSOA, clases_INSOB, clases_INSO1C, clases_INSO2A
from clase import clases_INSO2B, clases_INSO2C, clases_INSO2D

from asignatura import web, lab_redes, pensamiento_creativo, composicion_visual
from asignatura import estadistica, redes_ordenadores, proyectos_2, proyectos_1

from horario import Horario

import random

import time

import math

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


def generar_horario(bloques_por_asignatura):
    clases_horario = []
    mapa_horario = []

    for _ in range(5):
        mapa_horario.append([False] * 6)

    for asignatura in range(len(asignaturas_cuatrimestre)):
        bloques = bloques_por_asignatura[asignatura].copy()

        encontrado = False

        while len(bloques) > 0 and not encontrado:
            bloque = random.choice(bloques)

            seleccionado = True

            # comprobar que no se superponga con las clases ya añadidas
            for clase in bloque:

                # si es la primera clase añadida
                if len(clases_horario) == 0:
                    seleccionado = True

                for clase_horario in clases_horario:
                    # si no se superpone
                    if clase.dia == clase_horario.dia and clase.hora == clase_horario.hora:
                        seleccionado = False

            # si no se ha encontrado un bloque que no se superponga
            if seleccionado:
                for clase in bloque:
                    mapa_horario[clase.dia][clase.hora] = True
                    clases_horario.append(clase)

                encontrado = True
            else:
                bloques.remove(bloque)

    return mapa_horario, clases_horario


def puntuar_horario(mapa_horario):
    puntuacion = 0

    for dia in mapa_horario:
        num_clases = sum(dia)
        clase_actual = 0

        for hora in dia:

            if hora:
                clase_actual += 1
            else:
                if clase_actual > 0 and clase_actual < num_clases:
                    puntuacion -= 1

    return puntuacion


if __name__ == '__main__':

    bloques_por_asignatura = []

    for asignatura in asignaturas_cuatrimestre:

        bloques = []

        for grupo in range(len(clases)):
            bloque = bloque_clase(asignatura, grupo)

            # como hay grupos que no tienen asignaturas no se añaden
            if len(bloque) > 0:
                bloques.append(bloque)

        bloques_por_asignatura.append(bloques)

    while True:
        mapa_horario, clases_horario = generar_horario(bloques_por_asignatura)
        best_puntuacion = puntuar_horario(mapa_horario)
        best_horario = clases_horario

        while best_puntuacion < -1:
            mapa_horario, clases_horario = generar_horario(bloques_por_asignatura)
            puntuacion = puntuar_horario(mapa_horario)

            if puntuacion > best_puntuacion:
                best_puntuacion = puntuacion
                best_horario = clases_horario

            horario = Horario(best_horario)

        print("Guardado horario. Puntuacion: ", best_puntuacion)

        # mostrara y guardar el mejor horario
        horario.cargar_imagen()
        horario.guardar()
