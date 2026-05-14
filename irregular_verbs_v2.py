import streamlit as st
import random
import pandas as pd

verbos = ["be","bear","beat","become","begin","bite","blow","break","bring","build","burn","burst","buy","can",
          "catch","choose","come","cost","cut","deal","dig", "drink", "eat", "fall", "forget","give", "get", "go",
          "know", "leave", "lose", "make", "pay", "read", "say", "see", "sell", "sleep", "speak", "take", "tell",
          "think", "write"]
Pasado = ["was","bore","beat","became","began", "bit","blew","broke","brought","built","burnt","burst","bought",
          "could","caught","chose","came","cost","cut","dealt","dug", "drank", "ate", "fell", "forgot", "gave", "got", "went",
          "knew", "left", "lost", "made", "paid", "read", "said", "saw", "sold", "slept", "spoke", "took", "told",
          "thought", "wrote"]
Traducción = ["ser","soportar","latir","convertirse","comenzar","morder","soplar","romper","traer algo","construir",
              "quemar","explotar","comprar","poder","pillar","elegir","venir","costar","cortar","negociar","cavar", "beber",
              "comer", "caer", "olvidar", "dar algo", "obtener", "ir", "conocer", "salir", "perder", "hacer (fabricar)", "pagar",
              "leer", "decir", "ver", "vender", "dormir", "hablar", "tomar", "contar, decir", "pensar", "escribir"]

st.set_page_config(page_title="Past Simple - Group 1. ", page_icon="📖")
st.title("U.M.R.P.S.F.X.CH. - CARRERA DE IDIOMAS - ICT's - Proffesor Mike Ticona)
st.subheader("Students:")
st.markdown("### Hugo Alconini")
if 'indice' not in st.session_state:
    st.session_state.indice = random.randint(0, len(verbos)-1)
if 'aciertos' not in st.session_state:
    st.session_state.aciertos = 0
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0
if 'finalizado' not in st.session_state:
    st.session_state.finalizado = False
st.sidebar.title("Settings")
cantidad_objetivo = st.sidebar.slider("How many verbs would you like to practise?", 5, len(verbos), 10)
if st.sidebar.button("Reset Progress"):
    st.session_state.aciertos = 0
    st.session_state.intentos = 0
    st.session_state.finalizado = False
    st.rerun()
tab1, tab2 = st.tabs(["📚 Study List", "Take the Test"])
with tab1:
    st.header("Irregular Verbs List")
    st.write("Please revise the verbs below before starting your assessment.")
    df = pd.DataFrame({
        "Infinitive": verbos, 
        "Past Simple": Pasado, 
        "Translation (ES)": Traducción})
    st.dataframe(df, use_container_width=True)
with tab2:
    if st.session_state.intentos >= cantidad_objetivo:
        st.session_state.finalizado = True
    if st.session_state.finalizado:
        st.header("🎊 Test Completed!")
        nota = (st.session_state.aciertos / cantidad_objetivo) * 100
        st.metric("Your Mark", f"{nota:.1f}%")
        
        if nota == 100:
            st.balloons()
            st.success("Splendid! You are an expert.")
        elif nota >= 70:
            st.info("Well done! Keep practising to achieve perfection.")
        else:
            st.warning("You might want to revise the list again. Keep at it!")
            
        st.write(f"Score: {st.session_state.aciertos} out of {cantidad_objetivo}")
    else:
        idx = st.session_state.indice
        st.subheader(f"Question {st.session_state.intentos + 1} of {cantidad_objetivo}")
        st.write(f"What is the past simple of: **{verbos[idx]}**?")
        st.caption(f"Meaning in Spanish: {Traducción[idx]}")
        respuesta = st.text_input("Enter your answer here:", key=f"input_{st.session_state.intentos}").lower().strip()

        if st.button("Submit"):
            if respuesta == Pasado[idx]:
                st.success("Correct!")
                st.session_state.aciertos += 1
            else:
                st.error(f"Incorrect. The answer was: {Pasado[idx]}")
            st.session_state.intentos += 1
            st.session_state.indice = random.randint(0, len(verbos)-1)
            st.button("Next Question")
