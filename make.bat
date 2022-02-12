@echo off

if [%1] == [] goto help

if exist "%~dp0.venv\" (
    set "VENV_PYTHON=%~dp0.venv\Scripts\python"
) else (
    set VENV_PYTHON=python
)

goto %1

:reformat
"%VENV_PYTHON%" -m black "%~dp0."
"%VENV_PYTHON%" -m isort "%~dp0."
goto:eof

:black
"%VENV_PYTHON%" -m black "%~dp0."
goto:eof

:isort
"%VENV_PYTHON%" -m isort "%~dp0."
goto:eof

:stylecheck
"%VENV_PYTHON%" -m black --check "%~dp0."
goto:eof

:stylediff
"%VENV_PYTHON%" -m black --check --diff "%~dp0."
goto:eof

:newenv
py -3.9 -m venv --clear .venv
"%~dp0.venv\Scripts\python" -m pip install -U pip setuptools wheel
goto syncenv

:activateenv
CALL "%~dp0.venv\Scripts\activate.bat"
goto:eof
