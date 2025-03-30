import streamlit as st

st.title("🎮 Trivia de Cultura General - LaProfeVivy")

nombre = st.text_input("👤 Escribe tu nombre:")

if nombre:
    st.write(f"¡Hola, {nombre}! Responde las siguientes preguntas:")

    puntaje = 0

    respuesta1 = st.radio("1. ¿Cuál es el océano más grande del mundo?",
                          ("a) Atlántico", "b) Índico", "c) Pacífico"))
    if respuesta1 == "c) Pacífico":
        puntaje += 1

    respuesta2 = st.radio("2. ¿Quién escribió 'Cien años de soledad'?",
                          ("a) Gabriel García Márquez", "b) Mario Vargas Llosa", "c) Isabel Allende"))
    if respuesta2 == "a) Gabriel García Márquez":
        puntaje += 1

    respuesta3 = st.radio("3. ¿Cuál es el planeta más cercano al Sol?",
                          ("a) Venus", "b) Mercurio", "c) Marte"))
    if respuesta3 == "b) Mercurio":
        puntaje += 1

    if st.button("Enviar respuestas"):
        st.subheader(f"🎯 {nombre}, tu puntaje es: {puntaje}/3")
        if puntaje == 3:
            st.success("🏆 ¡Excelente, lo sabes todo!")
        elif puntaje == 2:
            st.info("👍 ¡Muy bien!")
        elif puntaje == 1:
            st.warning("😊 Puedes mejorar.")
        else:
            st.error("😅 ¡Sigue estudiando!")
