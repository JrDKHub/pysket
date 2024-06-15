@echo off
REM Activation de l'environnement Conda
CALL C:\Users\jrdak\anaconda3\Scripts\activate.bat digi 

REM Vérifier si l'activation a réussi
IF ERRORLEVEL 1 (
    echo Échec de l'activation de l'environnement 'digi'.
    exit /b 1
) ELSE (
    echo Environnement 'digi' activé avec succès.
)

REM Lancer Streamlit
streamlit run "C:\Users\jrdak\Desktop\Digi\Python\2023\ch23-24\pysket\src\Home 🏀.py"

REM Empêcher la fermeture de la fenêtre
pause
