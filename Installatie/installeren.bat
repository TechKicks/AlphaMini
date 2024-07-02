@echo off

REM Python aan het installeren
START /WAIT python-3.8.2.exe
if %errorlevel% neq 0 (
    echo Kan Python niet installeren
    pause
)


REM VSCode aan het installeren
START /WAIT VSCodeUserSetup-x64-1.90.2.exe
if %errorlevel% neq 0 (
    echo Kan VSCode niet installeren
    pause
)

start modules.bat