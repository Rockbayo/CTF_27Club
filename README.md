# 🎸 The 27 Club CTF - Universidad de Cundinamarca

[![Security Lab](https://img.shields.io/badge/Security-CTF%20Challenge-red.svg)](https://unicundinamarca.edu.co/)
[![OWASP Top 10](https://img.shields.io/badge/OWASP-A03%3A2021-orange.svg)](https://owasp.org/)
[![Docker](https://img.shields.io/badge/Docker-Turnkey%20Deploy-blue.svg)](https://www.docker.com/)

Proyecto Final de Laboratorio para la **Línea de Profundización I: Seguridad de Aplicaciones y Hacking Ético**, Facultad de Ingeniería, Universidad de Cundinamarca.
**Estudiante:** Óscar Robayo  
**Entorno de Auditoría:** Kali Linux vs Docker Target (`192.168.56.1` / `127.0.0.1`)

---

## 📻 Descripción del Reto
**"The 27 Club"** es un laboratorio CTF (*Capture The Flag*) gamificado con temática de rock clásico, diseñado para completarse en **60 minutos**. El ejercicio simula un entorno realista de auditoría web y análisis forense que exige tanto la explotación de vulnerabilidades críticas como la **discriminación activa de falsos positivos (*Rabbit Holes*)**.

### Las 5 Habitaciones de las Leyendas:
1. **Jimi Hendrix (Forense de Red y Criptografía):** Inspección profunda de paquetes (PCAP) y descifrado de cabecera `User-Agent` (ROT13) -> `FLAG{Purple_Haze_Network}` (+150 pts).
2. **Janis Joplin (Exposición Web y Esteganografía):** Auditoría de `robots.txt`, discriminación del señuelo `/admin_trampa/` y extracción de datos ocultos al final del archivo (EOF) con `strings` -> `FLAG{Cry_Baby_Hidden_Data}` (+200 pts).
3. **Jim Morrison (Inyección SQL - CWE-89):** Explotación basada en errores y técnica `UNION SELECT` en `/doors/?id=1`, discriminando la tabla trampa `doors_trap` -> `FLAG{Light_My_Fire_SQLi}` (+250 pts).
4. **Amy Winehouse (Cross-Site Scripting Almacenado - CWE-79):** Inyección de script arbitrario en el libro de firmas en `/winehouse/` y secuestro de cookie de sesión (`admintoken`) -> `FLAG{Back_To_Black_XSS}` (+200 pts).
5. **Kurt Cobain (Autenticación Débil y Escalada Root - CWE-250):** Acceso por consola con el usuario `kurt:nirvana`, auditoría de permisos especiales SUID en `/usr/bin/find` y lectura de la bandera de administración -> `FLAG{Smells_Like_Root_Spirit}` (+200 pts).

---

## 🚀 Despliegue Rápido en Cualquier Equipo (*One-Command Deploy*)

### Requisitos Previos:
- Docker y Docker Desktop (Windows, macOS o Linux)
- Git

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/CTF_27Club.git
cd CTF_27Club
```

### Paso 2: Levantar el Servidor Objetivo con Docker
```bash
docker compose up -d --build
```
*El servidor vulnerable quedará expuesto inmediatamente en el puerto `80` (accesible en `http://localhost/` o en la IP de red del host `192.168.56.1`).*

### Paso 3: Abrir el Tablero Interactivo
Abre el archivo `dashboard_27club.html` en tu navegador para interactuar con el temporizador de 60:00, reproducir la música real de los artistas y validar las banderas en tiempo real.

---

## 🎯 Tabla Resumen de Banderas y Trampas (Writeup)

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

---

## 📄 Documentación Oficial de Entrega
El informe formal completo para la sustentación se encuentra en la carpeta institucional:
- `Laboratorios/RUBRICALABORATORIOS.docx`: Estructurado bajo la plantilla de evaluación oficial de la Universidad de Cundinamarca, con los 22 pasos del laboratorio, 29 capturas de evidencia de alta resolución, objetivos, conclusiones institucionales y referencias en norma IEEE.
