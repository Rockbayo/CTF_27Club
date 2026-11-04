# 🎸 The 27 Club CTF — Universidad de Cundinamarca

[![Security Lab](https://img.shields.io/badge/Security-CTF%20Challenge-red.svg)](https://unicundinamarca.edu.co/)
[![OWASP Top 10](https://img.shields.io/badge/OWASP-A03%3A2021-orange.svg)](https://owasp.org/)
[![Docker](https://img.shields.io/badge/Docker-Turnkey%20Deploy-blue.svg)](https://www.docker.com/)

Laboratorio de Ciberseguridad Ofensiva y Forense para la **Línea de Profundización I: Seguridad de Aplicaciones y Hacking Ético**, Facultad de Ingeniería, Universidad de Cundinamarca.  
**Auditor / Autor:** Óscar Robayo  
**Tiempo Límite Estimado:** 60:00 minutos  
**Formato de Bandera Oficial:** `FLAG{...}`

---

## 🎯 Descripción del Reto
**"The 27 Club"** es un entorno interactivo y gamificado de auditoría de seguridad informática y análisis forense inspirado en leyendas del rock. El laboratorio exige la explotación metódica de vulnerabilidades críticas y la **discriminación activa de señuelos y falsos positivos (*Rabbit Holes*)**, simulando un escenario real de auditoría.

> [!IMPORTANT]
> **Anti-Spoiler / Integridad de la Prueba:** Las cadenas exactas de las banderas y señuelos están protegidas criptográficamente en el tablero web. Para completar el reto, cada participante debe descubrirlas ejecutando las técnicas de auditoría en el entorno de laboratorio.

### Las 5 Habitaciones del Reto:
1. **Jimi Hendrix (Forense de Red y Criptografía):** Inspección de captura de paquetes (PCAP), análisis de cabeceras HTTP anómalas y descifrado de algoritmos de sustitución (+150 pts).
2. **Janis Joplin (Exposición de Información y Esteganografía):** Auditoría de directivas en `robots.txt`, detección de directorios señuelo y extracción de artefactos ocultos al final de archivos multimedia (EOF) (+200 pts).
3. **Jim Morrison (Inyección SQL - CWE-89):** Explotación basada en errores y técnica `UNION SELECT` en catálogo dinámico, discriminando tablas trampa mediante enumeración de esquemas (+250 pts).
4. **Amy Winehouse (Cross-Site Scripting Almacenado - CWE-79):** Inyección de script arbitrario en el libro de visitas y secuestro de tokens de sesión autenticados (+200 pts).
5. **Kurt Cobain (Autenticación Débil y Escalada de Privilegios Root - CWE-250):** Acceso por consola con credenciales por defecto, auditoría de permisos especiales SUID y obtención de shell administrativa (+200 pts).

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
Abre el archivo `dashboard_27club.html` en tu navegador. El tablero incluye:
- Cronómetro regresivo oficial de 60:00 minutos con alertas sonoras.
- Reproductor de audio y memorabilia icónica de las leyendas del rock.
- Validador interactivo con verificación criptográfica SHA-256 (sin exposición de respuestas).
- Sistema de detección de señuelos con retroalimentación pedagógica.

---

## 🛡️ Matriz de Vulnerabilidades y Controles Defensivos

| Fase / Artista | Vulnerabilidad Estándar | Impacto Técnico | Control de Mitigación Recomendado |
|---|---|---|---|
| **Fase 1: Hendrix** | CWE-311 (Missing Encryption of Sensitive Data) | Exposición de tráfico C&C en texto plano | Cifrado obligatorio TLS/HTTPS e inspección IDS/IPS |
| **Fase 2: Joplin** | CWE-200 (Exposure of Sensitive Information) | Metadatos y archivos no enlazados expuestos | Depuración de metadatos y control estricto de acceso |
| **Fase 3: Morrison** | CWE-89 (SQL Injection) | Lectura y manipulación de bases de datos | Consultas Preparadas con PDO / ORM parametrizado |
| **Fase 4: Winehouse** | CWE-79 (Stored Cross-Site Scripting) | Secuestro de sesiones y robo de credenciales | Codificación contextual en salida y flag `HttpOnly` en cookies |
| **Fase 5: Cobain** | CWE-250 (Execution with Unnecessary Privileges) | Compromiso total del sistema (Root) | Principio de mínimo privilegio y remoción de bits SUID |
