# 🎸 The 27 Club CTF — Universidad de Cundinamarca

[![Security Lab](https://img.shields.io/badge/Security-CTF%20Challenge-red.svg)](https://unicundinamarca.edu.co/)
[![OWASP Top 10](https://img.shields.io/badge/OWASP-A03%3A2021-orange.svg)](https://owasp.org/)
[![Docker](https://img.shields.io/badge/Docker-Turnkey%20Deploy-blue.svg)](https://www.docker.com/)

Laboratorio de Ciberseguridad Ofensiva y Forense para la **Línea de Profundización I: Seguridad de Aplicaciones y Hacking Ético**, Facultad de Ingeniería, Universidad de Cundinamarca.  
**Auditor / Autor:** Óscar Robayo  
**Tiempo Estimado:** 60 minutos

---

## 🎯 Descripción del Ejercicio
**"The 27 Club"** es un entorno interactivo y gamificado de auditoría de seguridad y análisis forense inspirado en leyendas del rock. El laboratorio exige tanto la explotación metódica de vulnerabilidades críticas como la **discriminación activa de falsos positivos (*Rabbit Holes*)**.

### Las 5 Habitaciones del Reto:
1. **Jimi Hendrix (Forense de Red y Criptografía):** Inspección de paquetes (PCAP) y descifrado de cabecera `User-Agent` (ROT13) -> `FLAG{Purple_Haze_Network}` (+150 pts).
2. **Janis Joplin (Exposición de Información y Esteganografía):** Auditoría de `robots.txt`, evasión del señuelo `/admin_trampa/` y extracción de datos ocultos al final del archivo (EOF) en `janis.jpg` con `strings` -> `FLAG{Cry_Baby_Hidden_Data}` (+200 pts).
3. **Jim Morrison (Inyección SQL - CWE-89):** Explotación basada en errores y técnica `UNION SELECT` en `/doors/?id=1`, discriminando la tabla señuelo `doors_trap` -> `FLAG{Light_My_Fire_SQLi}` (+250 pts).
4. **Amy Winehouse (Cross-Site Scripting Almacenado - CWE-79):** Inyección de script arbitrario en el libro de firmas en `/winehouse/` y secuestro de cookie de sesión (`admintoken`) -> `FLAG{Back_To_Black_XSS}` (+200 pts).
5. **Kurt Cobain (Autenticación Débil y Escalada de Privilegios Root - CWE-250):** Acceso por consola con el usuario `kurt:nirvana`, auditoría de permisos especiales SUID en `/usr/bin/find` y lectura de la bandera de administración -> `FLAG{Smells_Like_Root_Spirit}` (+200 pts).

---

## 🚀 Despliegue Rápido (Un Solo Comando)

### Requisitos Previos:
- Docker y Docker Desktop (Windows, macOS o Linux)
- Git

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Rockbayo/CTF_27Club.git
cd CTF_27Club
```

### 2. Levantar el Laboratorio en Docker
```bash
docker compose up -d --build
```
*El servidor vulnerable quedará expuesto inmediatamente en el puerto `80` (accesible en `http://localhost/` o en la IP de red del host).*

### 3. Abrir el Tablero Gamificado
Abre el archivo `dashboard_27club.html` en cualquier navegador web. Cuenta con:
- Cronómetro regresivo oficial de 60:00 minutos.
- Música y memorabilia real de cada artista.
- Validador interactivo de banderas oficiales y detección pedagógica de trampas (*Rabbit Holes*).

---

## 🏆 Matriz de Banderas y Trampas (Writeup / Solucionario)

| Fase / Artista | Vulnerabilidad (CWE) | Tipo de Artefacto | Cadena de Bandera | Mitigación |
|---|---|---|---|---|
| **Fase 1: Hendrix** | C&C / Cripto Débil (CWE-311) | Bandera Oficial | `FLAG{Purple_Haze_Network}` | Cifrado TLS/HTTPS e inspección IDS |
| **Fase 2: Joplin** | Information Exposure (CWE-200) | Bandera Oficial | `FLAG{Cry_Baby_Hidden_Data}` | Saneamiento de metadatos multimedia |
| **Fase 2 (Trampa)** | Information Exposure (CWE-200) | Falso Positivo | `RABBIT_HOLE{Sigue_Buscando_Janis_Se_Rie_De_Ti}` | Heurística y verificación de firmas |
| **Fase 3: Morrison** | SQL Injection (CWE-89) | Bandera Oficial | `FLAG{Light_My_Fire_SQLi}` | Consultas Preparadas (PDO) |
| **Fase 3 (Trampa)** | SQL Injection (CWE-89) | Falso Positivo | `RABBIT_HOLE{The_End_Is_Not_Here}` | Enumeración rigurosa de esquemas |
| **Fase 4: Winehouse** | Stored XSS (CWE-79) | Bandera Oficial | `FLAG{Back_To_Black_XSS}` | Codificación en salida y HttpOnly |
| **Fase 4 (Trampa)** | Stored XSS (CWE-79) | Falso Positivo | `RABBIT_HOLE{Rehab_Was_A_Lie}` | Validación de atributos de cookies |
| **Fase 5: Cobain** | SUID Privileges (CWE-250) | Bandera Root Final | `FLAG{Smells_Like_Root_Spirit}` | Retirar bit SUID (`chmod u-s`) |
