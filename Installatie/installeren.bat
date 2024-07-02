START /WAIT python-3.8.2.exe
START /WAIT VSCodeUserSetup-x64-1.90.2.exe
pip install -r requirements.txt

cd ../
code .

pause