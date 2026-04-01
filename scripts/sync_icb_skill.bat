@echo off
setlocal

set "PYTHON_EXE=py -3"
set "SCRIPT_PATH=%~dp0sync_icb_skill.py"

%PYTHON_EXE% "%SCRIPT_PATH%"

if errorlevel 1 (
    echo.
    echo Sync failed.
    exit /b %errorlevel%
)

echo.
echo Sync completed.
