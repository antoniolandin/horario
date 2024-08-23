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
