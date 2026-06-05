@echo off
cd /d "%~dp0"
py -3 start_viewer.py
if errorlevel 1 python start_viewer.py
pause
