import streamlit as st

# Define the README content as a long multiline string
readme_content = """
# Bienvenue sur PYSKET

![Logo](src/assets/img/pysket.png)

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
Vous souhaitez contribuer au projet ? Super ! Consultez notre dépôt [GitHub](https://github.com/JrDKHub/pysket) pour les problèmes qui ont besoin d'aide.
Les contributions à ce projet sont les bienvenues ! Merci de cloner le référentiel et de soumettre une demande d'extraction avec vos fonctionnalités ou corrections.

# Installation

1. **Installer Python** : Assurez-vous que Python est installé sur votre système. Vous pouvez le télécharger à partir depuis [python.org](https://www.python.org/downloads/).

2. **Créer un environnement virtuel** (recommandé):
   ```bash
   python -m venv streamlit_env
   source streamlit_env/bin/activate  

3. **Installer Streamlit**:
    ```bash
    pip install streamlit
    
4. Exécution de l'application


Pour exécuter votre application Streamlit, accédez au répertoire de votre projet dans le terminal et tapez:

    streamlit run your_script.py


Remplacez votre_script.py par le chemin d'accès à votre script Streamlit.


Voici une structure de projet de base recommandée pour nos applications Streamlit:

    /pysket
        /venv                   # Virtual environment
        /src                    # Source folder
            home.py             # Main Streamlit application script
        /assets                 # Files
            /img                # Images folder
        /pages                  # Differents pages of the application
            README.md




# Resources Additionnelles

- [Streamlit Documentation](https://docs.streamlit.io/get-started)
- [Streamlit Forum](https://discuss.streamlit.io/)


## Bon Stream !!!
"""

st.markdown(readme_content, unsafe_allow_html=True)