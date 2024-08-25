import streamlit as st

st.subheader("Añadir asignatura")
st.session_state.asignaturas = st.session_state.get("asignaturas", [])

nombre_asignatura = st.text_input("Nombre de la asignatura")


def guardar_asignaturas():
    with open("cache/asignaturas.txt", "w") as f:
        for asignatura in st.session_state.asignaturas:
            f.write(f"{asignatura}\n")


if st.button("Añadir"):
    if nombre_asignatura == "":
        st.error("Falta el nombre de la asignatura")
    elif nombre_asignatura in st.session_state.asignaturas:
        st.error("La asignatura ya existe")
    else:
        st.session_state.asignaturas.append(nombre_asignatura)
        guardar_asignaturas()
        st.success("Asignatura añadida")

st.write(st.session_state.asignaturas)
