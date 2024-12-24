@echo off
cls
echo Checking libraries...

timeout /t 2 /nobreak >nul

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

pip show requests >nul 2>nul || (echo requests library is not installed. Installing... && pip install requests)
pip show colorama >nul 2>nul || (echo colorama library is not installed. Installing... && pip install colorama)
pip show PySocks >nul 2>nul || (echo PySocks library is not installed. Installing... && pip install PySocks)
pip show charset-normalizer >nul 2>nul || (echo charset-normalizer library is not installed. Installing... && pip install charset-normalizer)
pip show idna >nul 2>nul || (echo idna library is not installed. Installing... && pip install idna)
pip show urllib3 >nul 2>nul || (echo urllib3 library is not installed. Installing... && pip install urllib3)
pip show certifi >nul 2>nul || (echo certifi library is not installed. Installing... && pip install certifi)

cls

echo Running EventSpammer...
cls
python main.py


pause
