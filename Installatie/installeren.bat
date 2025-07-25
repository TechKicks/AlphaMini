@echo off

REM Python aan het installeren
START /WAIT python-3.8.2.exe
if %errorlevel% neq 0 (
    echo Kan Python niet installeren
    pause
)


REM VSCode aan het installeren
START /WAIT VSCodeUserSetup-x64-1.90.2.exe /MERGETASKS=!runcode
if %errorlevel% neq 0 (
    echo Kan VSCode niet installeren
    pause
)

REM VSCode afsluiten als het automatisch start
taskkill /IM Code.exe /F >nul 2>&1

start modules.bat