# ==============================================================================
# SCRIPT DE APLICACIÓN EN WINDOWS / POWERSHELL PARA CONTENEDOR DOCKER
# ==============================================================================

Write-Host "[*] Verificando contenedor '27club_ctf'..." -ForegroundColor Cyan

$containerRunning = docker ps --filter "name=27club_ctf" --format "{{.Names}}"

if (-not $containerRunning) {
    Write-Host "[!] El contenedor '27club_ctf' no esta activo." -ForegroundColor Yellow
    Write-Host "[*] Iniciando contenedor '27club_ctf'..." -ForegroundColor Cyan
    docker start 27club_ctf
}

Write-Host "[*] Copiando script de aprovisionamiento de Fase 3..." -ForegroundColor Cyan
docker cp setup_fase3.sh 27club_ctf:/tmp/setup_fase3.sh

Write-Host "[*] Ejecutando configuracion en el contenedor..." -ForegroundColor Cyan
docker exec -i 27club_ctf bash /tmp/setup_fase3.sh

Write-Host "`n[+] Fase 3 lista para auditar en: http://192.168.56.1/doors/?id=1" -ForegroundColor Green

