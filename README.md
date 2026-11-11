# 🎸 The 27 Club CTF — Universidad de Cundinamarca

[![Security Lab](https://img.shields.io/badge/Security-CTF%20Challenge-red.svg)](https://unicundinamarca.edu.co/)
[![OWASP Top 10](https://img.shields.io/badge/OWASP-A03%3A2021-orange.svg)](https://owasp.org/)
[![Docker](https://img.shields.io/badge/Docker-Turnkey%20Deploy-blue.svg)](https://www.docker.com/)

Laboratorio de Ciberseguridad Ofensiva y Forense para la **Línea de Profundización I: Seguridad de Aplicaciones y Hacking Ético**, Facultad de Ingeniería, Universidad de Cundinamarca.  
**Auditor / Autor:** Óscar Robayo  
**Tiempo Límite Estimado:** 60:00 minutos  
**Formato de Bandera Oficial:** `27C{...}`

---

## 🎯 Descripción del Reto
**"The 27 Club"** es un entorno interactivo y gamificado de auditoría de seguridad informática y análisis forense inspirado en leyendas del rock. El laboratorio exige la explotación metódica de vulnerabilidades críticas y la **discriminación activa de señuelos y falsos positivos (*Rabbit Holes*)**, simulando un escenario real de auditoría en caja negra.

> [!IMPORTANT]
> **Anti-Spoiler / Integridad de la Prueba:** Las cadenas exactas de las banderas y señuelos están protegidas criptográficamente con hashes SHA-256 en el tablero web. Para completar el reto, cada participante debe descubrirlas ejecutando las técnicas de auditoría en el entorno de laboratorio.

### Las 6 Fases del Reto (1.000 Puntos Oficiales):
0. **Robert Johnson (Barrido de Red & Enumeración de Cabeceras - Traste 3):** Descubrimiento de host y enumeración de cabeceras de respuesta HTTP (`X-Discovery-Token`) (+100 pts).
1. **Jimi Hendrix (Forense de Red y Criptografía - Traste 6):** Inspección de captura de paquetes (PCAP), análisis de baliza C&C y descifrado de algoritmos de sustitución ROT13 (+150 pts).
2. **Janis Joplin (Exposición de Información y Esteganografía - Traste 11):** Auditoría de directivas en `robots.txt`, detección de directorios señuelo y extracción de artefactos ocultos al final de archivos multimedia (EOF) (+150 pts).
3. **Jim Morrison (Inyección SQL - CWE-89 - Traste 16):** Explotación basada en errores y técnica `UNION SELECT` en catálogo dinámico, discriminando tablas trampa (`doors_trap`) (+200 pts).
4. **Amy Winehouse (Cross-Site Scripting Almacenado - CWE-79 - Traste 21):** Inyección de script arbitrario en el libro de visitas y secuestro de tokens de sesión autenticados (`admintoken`) (+200 pts).
5. **Kurt Cobain (Autenticación Débil y Escalada de Privilegios Root - CWE-250 - Traste 27):** Acceso por consola con credenciales débiles (`kurt:nirvana`), auditoría de permisos especiales SUID y obtención de shell administrativa (`root`) (+200 pts).

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

### 2. Levantar el Servidor Vulnerable
```bash
docker compose up -d --build
```
*El servidor de la víctima se iniciará en el puerto `80` (accesible en `http://localhost/` o en la IP del host).*

### 3. Iniciar el Tablero de Juego
Abre el archivo `index.html (o tablero3d_27club.html)` en tu navegador. El tablero incluye:
- Cronómetro regresivo oficial de 60:00 minutos con alertas sonoras.
- Reproductor de audio y memorabilia icónica de las leyendas del rock.
- Validador interactivo con verificación criptográfica SHA-256 (sin exposición de respuestas).
- Sistema de detección de señuelos con retroalimentación pedagógica.

---

## 🛡️ Matriz de Vulnerabilidades y Controles Defensivos

| Fase / Artista | Vulnerabilidad Estándar | Impacto Técnico | Control de Mitigación Recomendado |
|---|---|---|---|
| **Fase 0: Johnson** | CWE-200 (Exposure of Sensitive Information) | Fuga de identificadores y cabeceras técnicas | Ocultación de tokens y hardening de directivas `ServerTokens Prod` |
| **Fase 1: Hendrix** | CWE-311 (Missing Encryption of Sensitive Data) | Exposición de tráfico C&C en texto plano | Cifrado obligatorio TLS/HTTPS e inspección IDS/IPS |
| **Fase 2: Joplin** | CWE-200 (Exposure of Sensitive Information) | Metadatos y archivos no enlazados expuestos | Depuración de metadatos y control estricto de acceso |
| **Fase 3: Morrison** | CWE-89 (SQL Injection) | Lectura y manipulación de bases de datos | Consultas Preparadas con PDO / ORM parametrizado |
| **Fase 4: Winehouse** | CWE-79 (Stored Cross-Site Scripting) | Secuestro de sesiones y robo de credenciales | Codificación contextual en salida y flag `HttpOnly` en cookies |
| **Fase 5: Cobain** | CWE-250 / CWE-307 (Privilege Escalation & Brute Force) | Compromiso total del sistema (Root) | Principio de mínimo privilegio, contraseñas robustas y remoción de bits SUID |

---

## 🛡️ Enfoque Defensivo (Blue Team & Hardening Institucional)

Para enriquecer la perspectiva de seguridad defensiva, el proyecto incluye artefactos formales de detección y remediación:

### 1. Reglas de Detección Snort IDS (
ules/27club_snort.rules)
Conjunto de firmas y reglas en Capa 7 para sistemas de detección de intrusos (Snort/Suricata), diseñadas para alertar y registrar en tiempo real cada vector de ataque del reto:
- **SID 2700001**: Detección de tráfico C&C y cabecera User-Agent con carga ofuscada ROT13 (Fase Hendrix).
- **SID 2700002 / 2700003**: Alerta de reconocimiento en 
obots.txt y acceso a directorios restringidos (Fase Joplin).
- **SID 2700004 / 2700005**: Detección de inyección SQL basada en comillas y cláusulas UNION SELECT en /doors/ (Fase Morrison).
- **SID 2700006 / 2700007**: Detección de inyecciones XSS (<script>, eventos DOM, exfiltración document.cookie) en /winehouse/ (Fase Winehouse).
- **SID 2700008**: Auditoría de intentos de conexión administrativa por SSH (Fase Cobain).

### 2. Script de Remediación Defensiva (hardening_remediacion.sh)
Script automatizado que aplica los controles de seguridad y mejores prácticas de la industria (OWASP / MITRE) para mitigar las 5 vulnerabilidades en el servidor objetivo:
`ash
# Ejecutar remediación completa dentro del contenedor
docker exec 27club_ctf /tmp/hardening_remediacion.sh
`
- **CWE-89 (SQLi):** Refactoriza el backend de Jim Morrison implementando **Consultas Preparadas con PDO** y validación de tipos enteros.
- **CWE-79 (XSS):** Implementa escape contextual de caracteres mediante htmlspecialchars() y asegura las cookies de sesión con el atributo **HttpOnly**.
- **CWE-250 (SUID):** Revoca el bit Setuid en /usr/bin/find (chmod u-s) y bloquea logins interactivos no autorizados.
