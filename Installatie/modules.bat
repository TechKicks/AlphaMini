REM Python requirements aan het installeren
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Kan python requirements niet installeren
    pause
)


REM Jupyter extension aan het installeren
call code --install-extension ms-toolsai.jupyter --force
if %errorlevel% neq 0 (
    echo Kan Jupyter extentie van VSCode niet downloaden
    pause
)

REM Python extension aan het installeren
call code --install-extension ms-python.python --force
if %errorlevel% neq 0 (
    echo Kan Python extentie van VSCode niet downloaden
    pause
)

cd ../code

REM Open VSCode
code .
if %errorlevel% neq 0 (
    echo Kan VSCode niet openen
    pause
    :: exit /b %errorlevel%
)

pause