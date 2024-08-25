import streamlit as st


def guardar_grupos():
    with open("cache/grupos.txt", "w") as f:
        for grupo in st.session_state.grupos:
            f.write(f"{grupo}\n")


st.subheader("Añadir grupo")

st.session_state.grupos = st.session_state.get("grupos", [])

nombre_grupo = st.text_input("Nombre del grupo")

if st.button("Añadir"):
    if nombre_grupo == "":
        st.error("Falta el nombre del grupo")
    elif nombre_grupo in st.session_state.grupos:
        st.error("El grupo ya existe")
    else:
        st.session_state.grupos.append(nombre_grupo)
        guardar_grupos()
        st.success("Grupo añadido")

st.write(st.session_state.grupos)
