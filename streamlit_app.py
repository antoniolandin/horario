import streamlit as st
import os

st.title("Calcular horario")

clase_page = st.Page(
    page="pages/clase_page.py",
    title="Añadir clase",
    icon=":material/school:",
    default=True,
)

asignatura_page = st.Page(
    page="pages/asignatura_page.py",
    title="Añadir asignatura",
    icon=":material/square_foot:",
)

grupo_page = st.Page(
    page="pages/grupo_page.py",
    title="Añadir grupo",
    icon=":material/groups:",
)

profesor_page = st.Page(
    page="pages/profesor_page.py",
    title="Añadir profesor",
    icon=":material/face:",
)

st.session_state.asignaturas = []
st.session_state.grupos = []
st.session_state.profesores = []

# crear los archivos de texto si no existen
if not os.path.exists("cache"):
    os.makedirs("cache")
if not os.path.exists("cache/asignaturas.txt"):
    os.mknod("cache/asignaturas.txt")
if not os.path.exists("cache/grupos.txt"):
    os.mknod("cache/grupos.txt")
if not os.path.exists("cache/profesores.txt"):
    os.mknod("cache/profesores.txt")

# obtener las asignaturas y los grupos de los archivos de texto
with open("cache/asignaturas.txt") as f:
    asignaturas = f.read().splitlines()
    st.session_state.asignaturas.extend(asignaturas)

with open("cache/grupos.txt") as f:
    grupos = f.read().splitlines()
    st.session_state.grupos.extend(grupos)

with open("cache/profesores.txt") as f:
    profesores = f.read().splitlines()
    st.session_state.profesores.extend(profesores)


pg = st.navigation(pages=[clase_page, asignatura_page, grupo_page, profesor_page])
pg.run()
