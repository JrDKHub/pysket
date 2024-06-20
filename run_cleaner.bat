@echo off
REM Activating Conda
CALL C:\Users\your-username\anaconda3\Scripts\activate.bat conda_env_name

REM checking activation
IF ERRORLEVEL 1 (
    echo custom error message.
    pause
    exit /b 1
) ELSE (
    echo custom success message.
)

REM python script execution
python path-to-this-file

REM stop closing
pause
