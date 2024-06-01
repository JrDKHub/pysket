import streamlit as st
import subprocess
from datetime import datetime


if 'last_pressed_1' not in st.session_state:
    st.session_state['last_pressed_1'] = "Never"


if st.button('Executer le scrappeur'):
    # date de l'operation
    st.session_state['last_pressed_1'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # execution du script
    result = subprocess.run(['python', '../scrap.py'], capture_output=True, text=True)
    st.text("Scraper:")
    st.code(result.stdout)  #  output du script

    
    result2 = subprocess.run(['python','../cleaner.py'])
    st.text("Cleaner:")
    st.code(result.stdout)
    
    st.text(f"Dernière execution: {st.session_state['last_pressed_1']}")