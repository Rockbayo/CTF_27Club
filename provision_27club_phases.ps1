# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN POWERSHELL: DESPLIEGUE CTF THE 27 CLUB
# ==============================================================================

Write-Host "`n[*] Verificando comunicacion con Docker Desktop..." -ForegroundColor Cyan

try {
    $dockerInfo = docker ps --filter "name=27club_ctf" --format "{{.Names}}" 2>$null
} catch {
    $dockerInfo = $null
}

if (-not $dockerInfo) {
    Write-Host "[!] El contenedor '27club_ctf' no responde o Docker Desktop aun esta iniciando." -ForegroundColor Yellow
    Write-Host "[*] Asegurate de abrir Docker Desktop en Windows y ejecuta:" -ForegroundColor Cyan
    Write-Host "    docker start 27club_ctf" -ForegroundColor White
} else {
    Write-Host "[+] Contenedor '27club_ctf' detectado en ejecucion." -ForegroundColor Green
    Write-Host "[*] Inyectando script de aprovisionamiento de Fases 3, 4 y 5..." -ForegroundColor Cyan
    docker cp provision_27club_phases.sh 27club_ctf:/tmp/provision_27club_phases.sh
    docker exec -i 27club_ctf bash /tmp/provision_27club_phases.sh
    Write-Host "`n[+] ¡Todas las fases han sido aprovisionadas satisfactoriamente!" -ForegroundColor Green
}

