@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo ===================================================
echo   🎸 SUBIENDO THE 27 CLUB CTF A GITHUB (@Rockbayo)
echo ===================================================
echo.
echo Conectando con https://github.com/Rockbayo/CTF_27Club.git ...
git push -u origin main
echo.
if %ERRORLEVEL% equ 0 (
    echo ===================================================
    echo  [OK] ¡PROYECTO SUBIDO EXITOSAMENTE A GITHUB!
    echo  URL: https://github.com/Rockbayo/CTF_27Club
    echo ===================================================
) else (
    echo [ERROR] Hubo un problema al subir. Revisa la autorizacion de GitHub.
)
echo.
pause
