@echo off
REM activate conda env
CALL C:\Users\your-username\anaconda3\Scripts\activate.bat conda_env_name

REM check activation
IF ERRORLEVEL 1 (
    echo custom error message.
    pause
    exit /b 1
) ELSE (
    echo custom success message.
)

REM python script
python path-to-your-script

REM stop closing
pause
