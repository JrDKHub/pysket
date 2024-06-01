import streamlit as st

# Define the README content as a long multiline string
readme_content = """
# Bienvenue sur PYSKET

![Logo]("assets/img/pysket.png")

Notre application nous permet de prédire les résultats de matchs de basket (le score des équipes de la franchise NBA si celles ci s'affrontaient).

Nous nous sommes basés sur les formules de [The power rank](https://thepowerrank.com/cbb-analytics/)

# Fonctionnalités

- **Prédiction du score de chaque équipes**

# Technologies Utilisées

- **Python**: langage de programmation principal.
- **Streamlit**: Framework pour creer l'application.
- **Pandas**: pour la manipulation des données.
- **Playwright**: Framework pour faire du scrapping

# Contributions
Vous souhaitez contribuer au projet ? Super ! Consultez notre dépôt [GitHub]() pour les problèmes qui ont besoin d'aide.
Les contributions à ce projet sont les bienvenues ! Merci de cloner le référentiel et de soumettre une demande d'extraction avec vos fonctionnalités ou corrections.


1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv streamlit_env
   source streamlit_env/bin/activate  # On Windows use `streamlit_env\\Scripts\\activate`

3. **Install Streamlit**:
    ```bash
    pip install streamlit
    
Running the Application


To run your Streamlit application, navigate to your project directory in the terminal and type:
    ```bash
        streamlit run your_script.py


Replace your_script.py with the path to your Streamlit script.


Here’s a basic project structure recommended of our Streamlit applications:

    /pysket
        /venv                   # Virtual environment
        /src                    # Source folder
            home.py             # Main Streamlit application script
        /assets                 # Files
        /pages                  # Differents pages of the application
            README.md




# Resources Additionnelles

Streamlit Documentation
Streamlit Forum
License
This project is licensed under the MIT License - see the LICENSE file for details.

## Bon Stream !!!
"""

st.markdown(readme_content, unsafe_allow_html=True)