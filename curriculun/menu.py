import streamlit as st
import curriculo, projetos

def menu_inicial():
    pg = st.navigation([
        st.Page("curriculo.py", title="Curriculo Vitor Rafael", icon="📝"),
        # st.Page("projetos.py", title="Projetos", icon="✅"),
        st.Page("portifolio.py", title="Portifólio", icon="📊"),
        # st.Page("chatbot - IA.py", title="ChatBot - IA", icon="👻")
    ],
        position="sidebar",
        expanded=True
    )
    pg.run()

menu_inicial()
