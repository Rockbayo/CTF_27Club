@echo off
chcp 65001 > nul
echo ===================================================
echo   🎸 SUBIENDO THE 27 CLUB CTF A GITHUB (@rockbayo)
echo ===================================================
echo.
echo Verificando estado local del repositorio...
git status
echo.
echo Subiendo rama main a origin (https://github.com/rockbayo/CTF_27Club.git)...
git push -u origin main
echo.
if %ERRORLEVEL% equ 0 (
    echo [OK] ¡Proyecto subido exitosamente a GitHub!
    echo Puedes verlo en: https://github.com/rockbayo/CTF_27Club
) else (
    echo.
    echo [AVISO] Si dice "Repository not found":
    echo 1. Ve a https://github.com/new
    echo 2. Crea el repositorio con el nombre exacto: CTF_27Club
    echo    (No agregues README, ni .gitignore, ni licencia; déjalo vacío)
    echo 3. Vuelve a ejecutar este script.
)
echo.
pause
