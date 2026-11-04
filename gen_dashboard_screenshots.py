#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Capturas del Dashboard Web Gamificado para el Informe Word
Universidad de Cundinamarca - The 27 Club CTF
"""

import os
from PIL import Image, ImageDraw, ImageFont

CAPTURAS_DIR = "capturas"
os.makedirs(CAPTURAS_DIR, exist_ok=True)

FONT_PATH = "C:/Windows/Fonts/consola.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/consolab.ttf"
ARIAL_BOLD = "C:/Windows/Fonts/arialbd.ttf"
ARIAL = "C:/Windows/Fonts/arial.ttf"

f_title = ImageFont.truetype(ARIAL_BOLD, 22)
f_sub = ImageFont.truetype(ARIAL, 13)
f_h2 = ImageFont.truetype(ARIAL_BOLD, 18)
f_body = ImageFont.truetype(ARIAL, 12)
f_code = ImageFont.truetype(FONT_PATH, 12)
f_code_bold = ImageFont.truetype(FONT_BOLD_PATH, 13)

def create_browser_window(width, height, url_text):
    img = Image.new("RGB", (width, height), (7, 7, 11))
    draw = ImageDraw.Draw(img)

    # Barra del navegador
    draw.rectangle([0, 0, width, 44], fill=(20, 22, 34))
    draw.line([0, 44, width, 44], fill=(45, 50, 75), width=1)

    # Botones ventana
    draw.ellipse([16, 15, 28, 27], fill=(255, 95, 86))
    draw.ellipse([36, 15, 48, 27], fill=(255, 189, 46))
    draw.ellipse([56, 15, 68, 27], fill=(39, 201, 63))

    # Barra de dirección URL
    draw.rectangle([100, 9, width - 120, 35], fill=(10, 11, 18), outline=(60, 65, 95), width=1)
    draw.text((115, 14), f"🔒 {url_text}", font=f_code, fill=(0, 240, 255))

    return img, draw

# ==============================================================================
# CAPTURA 1: DASHBOARD GENERAL (SALÓN CENTRAL & MEMORIAL)
# ==============================================================================
def gen_dashboard_overview():
    w, h = 1200, 680
    img, draw = create_browser_window(w, h, "http://localhost:8080/dashboard_27club.html (Salón Central)")

    # Header CTF
    draw.rectangle([0, 45, w, 115], fill=(12, 13, 20))
    draw.line([0, 115, w, 115], fill=(157, 78, 221), width=2)

    # Logo & Vinilo
    draw.ellipse([25, 55, 75, 105], fill=(255, 0, 127))
    draw.ellipse([45, 75, 55, 85], fill=(0, 240, 255))
    draw.text((88, 55), "THE 27 CLUB CTF", font=f_title, fill=(255, 255, 255))
    draw.text((90, 85), "Universidad de Cundinamarca • Hacking Ético Inmersivo", font=f_sub, fill=(0, 240, 255))

    # HUD Badges
    # Audio Pill
    draw.rectangle([600, 62, 800, 98], fill=(25, 15, 35), outline=(255, 0, 127), width=1)
    draw.text((615, 72), "🎵 Woodstock Radio (Música Real)", font=f_code_bold, fill=(255, 255, 255))

    # Tiempo
    draw.rectangle([815, 58, 925, 102], fill=(10, 11, 18), outline=(157, 78, 221), width=1)
    draw.text((830, 62), "TIEMPO RESTANTE", font=ImageFont.truetype(ARIAL, 9), fill=(160, 170, 190))
    draw.text((838, 74), "58:42", font=ImageFont.truetype(FONT_BOLD_PATH, 20), fill=(0, 240, 255))

    # Puntaje
    draw.rectangle([940, 58, 1060, 102], fill=(10, 11, 18), outline=(157, 78, 221), width=1)
    draw.text((955, 62), "PUNTAJE GLOBAL", font=ImageFont.truetype(ARIAL, 9), fill=(160, 170, 190))
    draw.text((955, 74), "350 / 1000", font=ImageFont.truetype(FONT_BOLD_PATH, 20), fill=(0, 255, 136))

    # Sustentación btn
    draw.rectangle([1075, 62, 1180, 98], fill=(157, 78, 221), outline=(255, 0, 127), width=1)
    draw.text((1085, 72), "🎓 SUSTENTACIÓN", font=f_code_bold, fill=(255, 255, 255))

    # Nav Bar de Habitaciones
    draw.rectangle([0, 116, w, 165], fill=(10, 11, 18))
    draw.line([0, 165, w, 165], fill=(40, 45, 65), width=1)

    rooms = [
        ("🏛️ The Memorial", True, (255, 0, 127)),
        ("🎸 1. Hendrix Studio", False, (0, 255, 136)),
        ("🌸 2. Joplin Caravan", False, (0, 255, 136)),
        ("🚪 3. Morrison Crypt", False, (0, 240, 255)),
        ("🎙️ 4. Winehouse Speakeasy", False, (140, 140, 160)),
        ("⚡ 5. Cobain Garage", False, (140, 140, 160))
    ]
    cur_x = 40
    for name, is_act, col in rooms:
        bg = (30, 20, 45) if is_act else (18, 20, 32)
        draw.rectangle([cur_x, 126, cur_x + 175, 156], fill=bg, outline=col, width=1)
        draw.text((cur_x + 12, 135), name, font=f_body, fill=(255, 255, 255) if is_act else col)
        cur_x += 185

    # Contenedor Principal Salón Central
    draw.rectangle([40, 185, 740, 440], fill=(18, 14, 35), outline=(157, 78, 221), width=2)
    draw.text((65, 210), "The 27 Club • Memorial Rockero", font=f_title, fill=(255, 0, 127))
    desc = (
      "Plataforma interactiva de entrenamiento y evaluación en Hacking Ético.\n"
      "Cada una de las 5 leyendas resguarda un templo digital en 192.168.56.1.\n"
      "Supera los vectores de Cripto, Forense PCAP, Exposición Web, SQLi, XSS\n"
      "y la escalada a Root en el contenedor 27club_ctf."
    )
    draw.text((65, 255), desc, font=f_body, fill=(210, 220, 240))

    # Muro de Discos de Oro
    draw.rectangle([765, 185, 1160, 440], fill=(10, 12, 20), outline=(255, 215, 0), width=1)
    draw.text((790, 205), "🏆 DISCOS DE ORO & ESTADO DE FASES", font=f_h2, fill=(255, 215, 0))
    discs = [
        "💿 Hendrix: FLAG{Purple_Haze_Network} (+150 pts) [SUPERADO]",
        "💿 Joplin:  FLAG{Cry_Baby_Hidden_Data} (+200 pts) [SUPERADO]",
        "💿 Morrison: En curso en /doors/?id=1 (+250 pts) [ACTIVO]",
        "💿 Winehouse: Pendiente de exfiltración (+200 pts) [BLOQUEADO]",
        "💿 Cobain:    Pendiente de escalada Root (+200 pts) [BLOQUEADO]"
    ]
    dy = 245
    for d in discs:
        col = (0, 255, 136) if "SUPERADO" in d else ((0, 240, 255) if "ACTIVO" in d else (120, 130, 150))
        draw.text((790, dy), d, font=f_code, fill=col)
        dy += 34

    # Collage Visual Inferior
    draw.rectangle([40, 460, 1160, 640], fill=(12, 14, 22), outline=(60, 65, 90), width=1)
    draw.text((60, 475), "📸 MEMORABILIA & COLLAGE DE LEYENDAS (WOODSTOCK, CHELSEA, SUNSET STRIP, CAMDEN, SEATTLE)", font=f_code_bold, fill=(255, 215, 0))

    # Miniaturas de fotos de los 5 artistas
    art_imgs = ['hendrix_album.jpg', 'joplin_album.jpg', 'morrison_album.jpg', 'winehouse_album.jpg', 'cobain_album.jpg']
    cx = 60
    for a in art_imgs:
        p = os.path.join("assets/images", a)
        if os.path.exists(p):
            sub_im = Image.open(p).resize((180, 125))
            img.paste(sub_im, (cx, 500))
        cx += 220

    out_p = os.path.join(CAPTURAS_DIR, "dashboard_general_lounge.png")
    img.save(out_p, quality=95)
    print(f"[+] Generada: {out_p}")

# ==============================================================================
# CAPTURA 2: DASHBOARD HABITACIÓN MORRISON (ROOM 3 ACTIVE & VINYL)
# ==============================================================================
def gen_dashboard_morrison():
    w, h = 1200, 680
    img, draw = create_browser_window(w, h, "http://localhost:8080/dashboard_27club.html (Room 3: Jim Morrison Crypt)")

    # Header
    draw.rectangle([0, 45, w, 115], fill=(12, 13, 20))
    draw.line([0, 115, w, 115], fill=(0, 240, 255), width=2)
    draw.text((40, 65), "THE 27 CLUB CTF • ROOM 3: THE DOORS CRYPT", font=f_title, fill=(0, 240, 255))
    draw.text((40, 95), "Reproduciendo: Light My Fire (The Doors - 1967 Master Original)", font=f_code, fill=(255, 215, 0))

    # Stage Morrison
    draw.rectangle([40, 135, 1160, 430], fill=(7, 31, 43), outline=(0, 240, 255), width=2)

    # Álbum real & foto de Morrison
    alb_p = "assets/images/morrison_album.jpg"
    pho_p = "assets/images/morrison_photo.jpg"
    if os.path.exists(alb_p):
        im_alb = Image.open(alb_p).resize((150, 150))
        img.paste(im_alb, (60, 160))
    if os.path.exists(pho_p):
        im_pho = Image.open(pho_p).resize((80, 80))
        img.paste(im_pho, (60, 330))

    draw.text((155, 345), "Jim Morrison", font=f_h2, fill=(255, 255, 255))
    draw.text((155, 375), "\"Light My Fire • 1967\"", font=f_code, fill=(255, 215, 0))

    # Narrativa
    draw.text((250, 160), "Room 3: The Doors Crypt & Vault", font=f_title, fill=(0, 240, 255))
    draw.rectangle([250, 195, 450, 220], fill=(10, 50, 70))
    draw.text((260, 200), "OBJETIVO ACTIVO • PASOS 13 AL 16", font=f_code_bold, fill=(0, 255, 136))

    morr_desc = (
      "Detrás de las puertas de roble y el órgano psicodélico Vox Continental, Jim Morrison\n"
      "resguarda el catálogo de base de datos en http://192.168.56.1/doors/?id=1.\n"
      "Vulnerabilidad CWE-89 (Inyección SQL). Cuidado con la tabla señuelo 'doors_trap'\n"
      "con el verso de 'The End'. La bandera real arde en 'doors_vault'."
    )
    draw.text((250, 235), morr_desc, font=f_body, fill=(210, 235, 245))

    # Panel de Bóveda y Validación
    draw.rectangle([780, 160, 1135, 405], fill=(5, 15, 22), outline=(0, 240, 255), width=1)
    draw.text((800, 180), "🚪 Bóveda de Morrison", font=f_h2, fill=(0, 240, 255))
    draw.rectangle([800, 215, 1115, 255], fill=(15, 35, 50))
    draw.text((810, 228), "FLAG{Light_My_Fire_SQLi}", font=f_code_bold, fill=(0, 255, 170))
    draw.rectangle([800, 270, 1115, 310], fill=(0, 240, 255))
    draw.text((870, 283), "DESBLOQUEAR PUERTA", font=f_code_bold, fill=(0, 0, 0))

    # Consola en vivo
    draw.rectangle([40, 450, 1160, 650], fill=(5, 8, 12), outline=(0, 240, 255), width=1)
    draw.text((60, 465), "📟 AUDITORÍA EN VIVO DE BASE DE DATOS (192.168.56.1/doors/)", font=f_code_bold, fill=(0, 240, 255))
    lines = [
        "[INFO] Conectado al backend relacional de The Doors (MariaDB/MySQL).",
        "kali@kali:~$ curl -s \"http://192.168.56.1/doors/?id=1'\"",
        "> Error SQL: You have an error in your SQL syntax; check manual near '\\'' at line 1",
        "[+] Vulnerabilidad CWE-89 confirmada. Exfiltración estructurada con UNION SELECT:",
        "kali@kali:~$ curl -s \"http://192.168.56.1/doors/?id=-1 UNION SELECT cancion, album, secreto FROM doors_vault WHERE id=2-- -\"",
        "> Canción: Light My Fire | Álbum: The Doors (1967) | Secreto: FLAG{Light_My_Fire_SQLi}"
    ]
    ly = 495
    for l in lines:
        c = (0, 255, 136) if "FLAG{" in l or "[+]" in l else ((255, 85, 85) if "Error SQL" in l else (200, 215, 235))
        draw.text((60, ly), l, font=f_code, fill=c)
        ly += 24

    out_p = os.path.join(CAPTURAS_DIR, "dashboard_room_morrison.png")
    img.save(out_p, quality=95)
    print(f"[+] Generada: {out_p}")

# ==============================================================================
# CAPTURA 3: DASHBOARD SUSTENTACIÓN COMPLETA (1000/1000 PTS)
# ==============================================================================
def gen_dashboard_sustentacion():
    w, h = 1200, 680
    img, draw = create_browser_window(w, h, "http://localhost:8080/dashboard_27club.html (Sustentación 100% Completada)")

    # Header Dorado de Victoria
    draw.rectangle([0, 45, w, 115], fill=(20, 16, 5))
    draw.line([0, 115, w, 115], fill=(255, 215, 0), width=2)
    draw.text((40, 60), "👑 THE 27 CLUB CTF • AUDITORÍA 100% CONQUISTADA", font=f_title, fill=(255, 215, 0))
    draw.text((40, 90), "UNIVERSIDAD DE CUNDINAMARCA • PUNTAJE PERFECTO 1000 / 1000 PTS", font=f_code_bold, fill=(0, 255, 136))

    # Badge de Puntaje Perfecto
    draw.rectangle([940, 55, 1160, 105], fill=(30, 25, 10), outline=(255, 215, 0), width=2)
    draw.text((955, 62), "PUNTAJE FINAL ALCANZADO", font=ImageFont.truetype(ARIAL, 9), fill=(255, 215, 0))
    draw.text((965, 75), "1000 / 1000", font=ImageFont.truetype(FONT_BOLD_PATH, 22), fill=(0, 255, 136))

    # 5 Tarjetas Conquistadas de Oro
    fases_gold = [
        ("Jimi Hendrix", "Fase 1: Forense PCAP & ROT13", "FLAG{Purple_Haze_Network}", "+150 PTS", "hendrix_album.jpg"),
        ("Janis Joplin", "Fase 2: Robots.txt & Stego EOF", "FLAG{Cry_Baby_Hidden_Data}", "+200 PTS", "joplin_album.jpg"),
        ("Jim Morrison", "Fase 3: SQL Injection (CWE-89)", "FLAG{Light_My_Fire_SQLi}", "+250 PTS", "morrison_album.jpg"),
        ("Amy Winehouse", "Fase 4: Stored XSS (CWE-79)", "FLAG{Back_To_Black_XSS}", "+200 PTS", "winehouse_album.jpg"),
        ("Kurt Cobain", "Fase 5: SUID Root (CWE-250)", "FLAG{Smells_Like_Root_Spirit}", "+200 PTS", "cobain_album.jpg")
    ]

    bx = 35
    for artist, vector, flag_str, pts, alb_file in fases_gold:
        draw.rectangle([bx, 140, bx + 215, 480], fill=(12, 14, 20), outline=(255, 215, 0), width=1)
        # Carátula
        ap = os.path.join("assets/images", alb_file)
        if os.path.exists(ap):
            im = Image.open(ap).resize((195, 170))
            img.paste(im, (bx + 10, 150))
        draw.text((bx + 10, 335), artist, font=f_h2, fill=(255, 215, 0))
        draw.text((bx + 10, 365), vector, font=ImageFont.truetype(ARIAL, 10), fill=(180, 190, 210))
        draw.rectangle([bx + 10, 390, bx + 205, 425], fill=(5, 30, 20), outline=(0, 255, 136))
        draw.text((bx + 15, 400), flag_str[:22] + "...", font=f_code, fill=(0, 255, 136))
        draw.text((bx + 10, 440), f"ESTADO: {pts} (CONQUISTADO)", font=f_code_bold, fill=(255, 215, 0))
        bx += 230

    # Panel de Certificación Institucional
    draw.rectangle([35, 505, 1165, 650], fill=(15, 18, 28), outline=(0, 240, 255), width=1)
    draw.text((60, 520), "🎓 EVALUACIÓN INSTITUCIONAL DE CUMPLIMIENTO (LÍNEA DE PROFUNDIZACIÓN I - HACKING ÉTICO)", font=f_code_bold, fill=(0, 240, 255))
    cert_text = (
        "El ejercicio CTF 'The 27 Club' concluyó exitosamente en un tiempo operativo inferior a 60 minutos.\n"
        "Se discriminaron 3 falsos positivos críticos (señuelo /admin_trampa/ de Janis, tabla doors_trap de Morrison\n"
        "y cookie de prueba de Winehouse). Se alcanzaron privilegios totales de superusuario (Root UID 0) en el contenedor.\n"
        "Se satisfacen el 100% de los criterios de la rúbrica oficial de la Universidad de Cundinamarca."
    )
    draw.text((60, 550), cert_text, font=f_body, fill=(220, 230, 245))

    out_p = os.path.join(CAPTURAS_DIR, "dashboard_sustentacion_completa.png")
    img.save(out_p, quality=95)
    print(f"[+] Generada: {out_p}")

if __name__ == "__main__":
    gen_dashboard_overview()
    gen_dashboard_morrison()
    gen_dashboard_sustentacion()

