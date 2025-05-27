@echo off
cd /d %~dp0
call venv\Scripts\activate
echo Iniciando API FastAPI com ambiente virtual...
uvicorn app.main:app --reload
pause
