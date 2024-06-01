import streamlit as st
import pandas as pd

df = pd.read_csv("../src/assets/data.csv")

if 'last_pressed_1' not in st.session_state:
    st.session_state['last_pressed_1'] = "Never"

st.info(f"le classement date de {st.session_state['last_pressed_1']}")

st.data_editor(df[["Rk","Team","W","L","Arena"]], hide_index=True, disabled=True,use_container_width=True,height=1000)

