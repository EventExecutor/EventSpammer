@echo off
echo -------------------------------
echo Installing dependencies
echo -------------------------------

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Download it from https://www.python.org/downloads/
    pause
    exit /b
)

set /a progress=0
set /a steps=20
set bar=

:loading
set bar=%bar%#
set /a progress+=100/%steps%
cls
echo Installation in progress: [%bar%] %progress%%% completed
timeout /t 1 >nul
if %progress% lss 100 goto loading

pip install requests colorama >nul 2>&1

if %errorlevel% neq 0 (
    echo Error during the installation of dependencies. Make sure pip is configured correctly.
    pause
    exit /b
)

cls
echo -------------------------------
echo Installation complete!
echo -------------------------------
pause
