@echo off
setlocal EnableDelayedExpansion
cd /d "%~dp0"
title Bug Miku - Launcher

cls
echo.
echo   Bug - Kairiki Bear feat. Hatsune Miku
echo   Code Animation by Nuthfih
echo   ----------------------------------------
echo.

:: Pilih Python: utamakan venv
if exist ".venv\Scripts\python.exe" (
    set "PYTHON=.venv\Scripts\python.exe"
    echo   [OK] Python : .venv
) else (
    set "PYTHON=python"
    echo   [OK] Python : system
)

:: Cek pygame, install jika belum ada
%PYTHON% -c "import pygame" 2>nul
if errorlevel 1 (
    echo   [!!] pygame not found, installing...
    echo.
    %PYTHON% -m pip install pygame
    if errorlevel 1 (
        echo.
        echo   [ERROR] Failed to install pygame!
        pause
        exit /b 1
    )
    echo   [OK] pygame has been installed
)

:: Cek file musik
if not exist "music\bugmiku.mp3" (
    echo   [WARN] music\bugmiku.mp3 not found!
)

echo   [OK] Ready - opening...
echo.
timeout /t 2 /nobreak >nul

:: Buka terminal baru - Windows Terminal jika ada, fallback ke cmd
where wt.exe >nul 2>&1
if not errorlevel 1 (
    wt new-tab --title "Bug Miku" --startingDirectory "%~dp0" -- cmd /c "chcp 65001 >nul && %PYTHON% BugAnimation.py"
) else (
    start "Bug Miku" /max cmd /c "chcp 65001 >nul && cd /d %~dp0 && %PYTHON% BugAnimation.py"
)

exit /b 0
