# Script PowerShell para subir CTF 27 Club a GitHub
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "  🎸 SUBIENDO THE 27 CLUB CTF A GITHUB (@rockbayo)" -ForegroundColor Yellow
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

git status
Write-Host "`nSubiendo a origin (https://github.com/rockbayo/CTF_27Club.git)..." -ForegroundColor Green
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[OK] ¡Proyecto subido exitosamente a GitHub!" -ForegroundColor Green
    Write-Host "URL: https://github.com/rockbayo/CTF_27Club" -ForegroundColor Cyan
} else {
    Write-Host "`n[AVISO] Si recibes 'Repository not found':" -ForegroundColor Yellow
    Write-Host "1. Abre tu navegador en: https://github.com/new" -ForegroundColor White
    Write-Host "2. Crea el repositorio con el nombre: CTF_27Club (público o privado, sin inicializar README ni .gitignore)" -ForegroundColor White
    Write-Host "3. Vuelve a ejecutar este script o corre: git push -u origin main" -ForegroundColor White
}
