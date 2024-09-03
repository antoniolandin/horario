import itertools

from lecture import Lecture
from read import read
from render import save_schedule_img


# dividir las clases de un grupo en bloques de clases por asignatura
def subject_block(lectures: list[Lecture], subject: str):

    block = []

    for lecture in lectures:
        if lecture.subject == subject:
            block.append(lecture)

    return block


# devuelve una lista de blocks de clases por asignatura
def subject_lecture_blocks(my_subjects, group_lectures):
    subject_lecture_block = []

    for subject in my_subjects:
        blocks = []

        for lectures in group_lectures.values():
            block = subject_block(lectures, subject)

            # como hay grupos que no tienen subjects no se añaden
            if len(block) > 0:
                blocks.append(block)

        if len(blocks) > 0:
            subject_lecture_block.append(blocks)
        else:
            print(f"No se ha encontrado la asignatura {subject}")

    return subject_lecture_block


# generar todos los horarios posibles válidos
def generate_schedules(subject_lecture_blocks):

    # generar todos los horarios posibles
    unvalidated_shedules = list(itertools.product(*subject_lecture_blocks))

    # lista de horarios validos
    schedules = []

    # pasar los bloques a clases sueltas
    for schedule in unvalidated_shedules:
        schedule_lectures = []

        for block in schedule:
            for lecture in block:
                schedule_lectures.append(lecture)

        if valid_schedule(schedule_lectures):
            schedules.append(schedule_lectures)

    return schedules


def valid_schedule(lectures):
    for l1 in lectures:
        for l2 in lectures:
            if l1 != l2 and l1.day == l2.day and l1.hour == l2.hour:
                return False

    return True


def schedule_to_map(schedule):
    schedule_map = [[False for _ in range(6)] for _ in range(5)]

    for lecture in schedule:
        schedule_map[lecture.day][lecture.hour] = True

    return schedule_map


def filter_schedule(mapa_horario, max_clases_dia=3, max_espacios=1):

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
    # asignaturas que quiero cursar
    my_subjects = [
        "Fund. Des. Web", "Lab. Red. Sist. Op", "Pensa. Creativo",
        "Proyectos 1", "Fund. Comp. Vis", "Prob. Estadist",
        "Redes Ordenadores", "Proyectos 2"
    ]

    # leer las clases de los grupos
    group_lectures = read("data/lectures.json")

    # dividir las clases de un grupo en bloques de clases por asignatura
    subject_lecture_blocks = subject_lecture_blocks(my_subjects,
                                                    group_lectures)

    # comprobar que se han encontrado todas las asignaturas
    assert len(my_subjects) == len(
        subject_lecture_blocks), "No se han encontrado todas las asignaturas"

    # generar todos los horarios posibles válidos
    schedules = generate_schedules(subject_lecture_blocks)

    # filtrar horarios
    for schedule in schedules:
        if filter_schedule(schedule_to_map(schedule), max_clases_dia=4):
            save_schedule_img(schedule)
