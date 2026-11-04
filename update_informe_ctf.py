#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Actualización Automatizada del Informe de Laboratorio CTF "The 27 Club"
Universidad de Cundinamarca - Seguridad de Aplicaciones y Hacking Ético
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

DOC_PATH = "Informe CTF_The27Club.docx"
BACKUP_PATH = "Informe CTF_The27Club_backup.docx"
CAPTURAS_DIR = "capturas"

def create_backup():
    if os.path.exists(DOC_PATH) and not os.path.exists(BACKUP_PATH):
        import shutil
        shutil.copyfile(DOC_PATH, BACKUP_PATH)
        print(f"[+] Respaldo de seguridad creado: {BACKUP_PATH}")

def add_step(doc, step_num, title, action_cmd, img_filename, justification_text):
    """
    Agrega un nuevo paso al informe respetando la estructura de los Pasos 1 al 12:
    1. Párrafo con Título en negrita + Acción + Comando
    2. Párrafo con la imagen centrada (si existe en capturas/)
    3. Párrafo con la Justificación técnica y forense profunda (CWE/OWASP)
    """
    print(f"[*] Procesando Paso {step_num}: {title}...")

    # 1. Párrafo de Acción
    p_header = doc.add_paragraph()
    r_step = p_header.add_run(f"Paso {step_num}: {title} ")
    r_step.bold = True
    r_step.font.size = Pt(11)

    r_action = p_header.add_run(f"{action_cmd}\n")
    r_action.font.size = Pt(11)

    # 2. Párrafo de Imagen
    img_path = os.path.join(CAPTURAS_DIR, img_filename)
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if os.path.exists(img_path):
        try:
            p_img.add_run().add_picture(img_path, width=Inches(6.2))
            print(f"    [+] Imagen incrustada: {img_path}")
        except Exception as e:
            print(f"    [!] Error al incrustar {img_path}: {e}")
            r_ph = p_img.add_run(f"[Captura de Evidencia: {img_filename}]")
            r_ph.italic = True
    else:
        r_ph = p_img.add_run(f"[Pendiente de captura en: capturas/{img_filename}]")
        r_ph.italic = True
        r_ph.font.color.rgb = RGBColor(180, 50, 50)

    # 3. Párrafo de Justificación Técnica
    p_just = doc.add_paragraph()
    p_just.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_just = p_just.add_run(justification_text)
    r_just.font.size = Pt(11)

    # Espacio separador
    doc.add_paragraph()

def add_ctf_summary_table(doc):
    """
    Agrega la tabla resumen de banderas capturadas y señuelos discriminados.
    """
    p_title = doc.add_paragraph()
    r = p_title.add_run("\nTabla Resumen de Artefactos, Banderas y Mitigaciones - The 27 Club CTF")
    r.bold = True
    r.font.size = Pt(12)

    table = doc.add_table(rows=1, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'

    headers = ["Fase / Artista", "Vulnerabilidad / Vector", "Tipo de Artefacto", "Cadena / Bandera", "Mitigación Defensiva"]
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].bold = True

    data = [
        ("Fase 1: Jimi Hendrix", "Exfiltración C&C (CWE-311)", "Bandera Real (ROT13)", "FLAG{Purple_Haze_Network}", "Cifrado TLS/HTTPS en tránsito e inspección IDS/IPS."),
        ("Fase 2: Janis Joplin", "Information Exposure (CWE-200)", "Bandera Real (Stego EOF)", "FLAG{Cry_Baby_Hidden_Data}", "Saneamiento de metadatos multimedia y control en robots.txt."),
        ("Fase 2 (Rabbit Hole)", "Information Exposure (CWE-200)", "Falso Positivo Señuelo", "RABBIT_HOLE{Sigue_Buscando_Janis_Se_Rie_De_Ti}", "Discriminación de directorios mediante heurística forense."),
        ("Fase 3: Jim Morrison", "SQL Injection (CWE-89 / OWASP A03)", "Bandera Real (UNION Based)", "FLAG{Light_My_Fire_SQLi}", "Consultas parametrizadas (Prepared Statements) y principio de menor privilegio."),
        ("Fase 3 (Rabbit Hole)", "SQL Injection (CWE-89)", "Falso Positivo Señuelo", "RABBIT_HOLE{The_End_Is_Not_Here}", "Enumeración rigurosa de esquemas de datos previo a la extracción."),
        ("Fase 4: Amy Winehouse", "Stored XSS (CWE-79 / OWASP A03)", "Bandera Real (Session Theft)", "FLAG{Back_To_Black_XSS}", "Codificación contextual en salida y directivas HttpOnly y CSP."),
        ("Fase 5: Kurt Cobain", "Permisos Excesivos SUID (CWE-250)", "Bandera Final Root (UID 0)", "FLAG{Smells_Like_Root_Spirit}", "Auditoría periódica de binarios con bit SUID y restricción de sudoers.")
    ]

    for row in data:
        row_cells = table.add_row().cells
        for idx, text in enumerate(row):
            row_cells[idx].text = text

    doc.add_paragraph()

if __name__ == "__main__":
    print("[*] Módulo de gestión documental para Informe CTF cargado.")

