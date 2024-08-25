import streamlit as st


def guardar_profesores():
    with open("cache/profesores.txt", "w") as f:
        for profesor in st.session_state.profesores:
            f.write(f"{profesor}\n")


st.session_state.profesores = st.session_state.get("profesores", [])

st.subheader("Añadir profesor")

nombre_profesor = st.text_input("Nombre del profesor")


if st.button("Añadir"):
    if nombre_profesor == "":
        st.error("Falta el nombre del profesor")
    elif nombre_profesor in st.session_state.profesores:
        st.error("El profesor ya existe")
    else:
        st.session_state.profesores.append(nombre_profesor)
        guardar_profesores()
        st.success("Profesor añadido")

st.write(st.session_state.profesores)
