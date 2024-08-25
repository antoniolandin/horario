import streamlit as st
from PIL import Image

from clase import Clase
from render import get_img_horario

st.subheader("Añadir una clase")

st.session_state.clases = st.session_state.get("clases", [])

img = Image.open("horario_base.png")
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
asignaturas = st.session_state.get("asignaturas", [])
horas = ["9:00-11:00",
         "11:00-13:00",
         "13:00-15:00",
         "15:00-17:00",
         "17:00-19:00",
         "19:00-21:00"]

grupos = st.session_state.get("grupos", [])
profesores = st.session_state.get("profesores", [])


def añadir_clase():
    asignatura = st.selectbox("Asignatura", st.session_state.asignaturas)

    dia_str = st.selectbox("Día de la semana", dias_semana)
    dia = dias_semana.index(dia_str)

    profesor = st.selectbox("Profesor (opcional)", profesores)

    hora_str = st.selectbox("Hora", horas)
    hora = horas.index(hora_str)

    grupo = st.selectbox("Grupo", grupos)
    clase = Clase(dia, hora, asignatura, profesor, grupo)

    if st.button("Añadir"):
        if clase in st.session_state.clases:
            st.error("La clase ya existe")
        else:
            st.session_state.clases.append(clase)
            st.success("Clase añadida")
            st.write(get_img_horario([clase]))


if not asignaturas:
    st.error("Primero añade una asignatura")
elif not grupos:
    st.error("Primero añade un grupo")
else:
    añadir_clase()
