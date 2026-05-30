@echo off
title Capitan Alaskin Bot
echo Iniciando Capitán Alaskin...
cd /d "%~dp0"
echo Instalando actualizaciones de IA...
python -m pip install -r requirements.txt --quiet

python bot.py
pause
