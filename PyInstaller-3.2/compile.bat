@echo off
python pyinstaller.py -i ..\res\icon.ico --clean --windowed --paths ..\modules ..\hotspot.py
pause