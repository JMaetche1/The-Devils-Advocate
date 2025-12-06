@echo off
REM Quick launch script for Windows

echo Starting The Devil's Advocate...
echo.

REM Check if virtual environment exists
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Launch Streamlit
streamlit run main.py

pause


