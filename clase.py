class Clase:
    def __init__(self, dia, hora, asignatura, profesor, grupo):
        self.hora = hora
        self.dia = dia
        self.asignatura = asignatura
        self.profesor = profesor
        self.grupo = grupo

    def get_nombre_grupo(self):
        grupos = ["INSO1A", "INSO1B", "INSO1C", "INSO2A", "INSO2B", "INSO2C", "INSO2D"]
        return grupos[self.grupo]

    def __str__(self):
        hora_inicio_clase = 9 + self.hora * 2
        hora_fin_clase = hora_inicio_clase + 2

        return f"{hora_inicio_clase}:00 - {hora_fin_clase}:00 - {self.asignatura} - {self.profesor} - {self.grupo}"
