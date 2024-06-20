@echo off
REM activating conda
CALL C:\Users\your-username\anaconda3\Scripts\activate.bat conda_env_name 

REM checking activation
IF ERRORLEVEL 1 (
    echo custom error message
    exit /b 1
) ELSE (
    echo custom success message.
)

REM launch streamlit
streamlit run path-to-streamlit-main-py-file

REM stop it from closing
pause
