#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constructor del Informe Final con la Estructura Exacta de la Rúbrica Institucional
Universidad de Cundinamarca - Línea de Profundización I
"""

import os
import io
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

OUT_PATH = "Laboratorios/RUBRICALABORATORIOS.docx"

def create_header_table(doc, number_str, title_str):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    # Celda 0: Número
    c0 = tbl.rows[0].cells[0]
    c0.width = Inches(0.4)
    shd0 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="C6D9F1"/>')
    c0._tc.get_or_add_tcPr().append(shd0)
    bdr0 = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:color="000000"/>\n'
        f'  <w:left w:val="single" w:sz="4" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:color="000000"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:color="000000"/>\n'
        f'</w:tcBorders>'
    )
    c0._tc.get_or_add_tcPr().append(bdr0)
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0 = p0.add_run(number_str)
    r0.bold = True
    r0.font.name = "Arial"
    r0.font.size = Pt(10)

    # Celda 1: Título
    c1 = tbl.rows[0].cells[1]
    c1.width = Inches(6.1)
    shd1 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="C6D9F1"/>')
    c1._tc.get_or_add_tcPr().append(shd1)
    bdr1 = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:color="000000"/>\n'
        f'  <w:left w:val="single" w:sz="4" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:color="000000"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:color="000000"/>\n'
        f'</w:tcBorders>'
    )
    c1._tc.get_or_add_tcPr().append(bdr1)
    p1 = c1.paragraphs[0]
    r1 = p1.add_run(title_str)
    r1.bold = True
    r1.font.name = "Arial"
    r1.font.size = Pt(10)

    doc.add_paragraph()

def style_data_table(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)
    for cell in table.rows[0].cells:
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EAEFF5"/>')
        cell._tc.get_or_add_tcPr().append(shd)

def copy_paragraph_with_images(p_src, doc_dest):
    new_p = doc_dest.add_paragraph()
    new_p.alignment = p_src.alignment

    imgs = p_src._element.xpath('.//a:blip/@r:embed')
    if imgs:
        for rId in imgs:
            img_part = p_src.part.related_parts[rId]
            img_stream = img_part.blob
            new_p.add_run().add_picture(io.BytesIO(img_stream), width=Inches(6.0))
    else:
        for run in p_src.runs:
            new_r = new_p.add_run(run.text)
            new_r.bold = run.bold
            new_r.italic = run.italic
            new_r.font.name = "Arial"
            if run.bold and ("Paso " in run.text or "Evidencia " in run.text):
                new_r.font.size = Pt(10.5)
                new_r.font.color.rgb = RGBColor(20, 40, 80)
            else:
                new_r.font.size = Pt(10)
    return new_p

def build_rubrica_document():
    print("[*] Iniciando construcción integral de Laboratorios/RUBRICALABORATORIOS.docx...")
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # 1. ENCABEZADO INSTITUCIONAL
    p1 = doc.add_paragraph()
    r = p1.add_run("Universidad De Cundinamarca")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(13)

    p2 = doc.add_paragraph()
    r = p2.add_run("Línea de Profundización I")
    r.font.name = "Arial"
    r.font.size = Pt(11)

    p3 = doc.add_paragraph()
    r = p3.add_run("Laboratorio Final CTF: \"The 27 Club\"")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(12)
    r.font.color.rgb = RGBColor(150, 20, 50)

    # 2. TABLA 0: DATOS DE CONTROL Y ESTUDIANTE
    t0 = doc.add_table(rows=2, cols=2)
    t0.alignment = WD_TABLE_ALIGNMENT.CENTER
    style_data_table(t0)
    t0.rows[0].cells[0].text = "Estudiante: Óscar Robayo"
    t0.rows[0].cells[1].text = "Docente: Línea de Profundización I"
    t0.rows[1].cells[0].text = "Asignatura: Seguridad de Aplicaciones y Hacking Ético"
    t0.rows[1].cells[1].text = "Fecha: Noviembre 2026 • Evaluación Institucional"
    for r in t0.rows:
        for c in r.cells:
            c.paragraphs[0].runs[0].font.name = "Arial"
            c.paragraphs[0].runs[0].font.size = Pt(9.5)
            c.paragraphs[0].runs[0].bold = True

    doc.add_paragraph()

    # 3. RESUMEN / INTRODUCCIÓN
    p_res_title = doc.add_paragraph()
    r = p_res_title.add_run("Resumen/introducción")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)

    p_res_body = doc.add_paragraph()
    p_res_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p_res_body.add_run(
        "El presente laboratorio formal documenta el diseño, ejecución y análisis forense del proyecto final de ciberseguridad 'The 27 Club CTF'. La práctica simula una auditoría integral en entorno controlado y aislado sobre contenedores Docker y red Host-Only de VirtualBox (192.168.56.0/24), conectando la máquina auditora Kali Linux con el servidor víctima vulnerable. A través de la narrativa temática de cinco íconos del rock (Jimi Hendrix, Janis Joplin, Jim Morrison, Amy Winehouse y Kurt Cobain), se evaluaron vectores críticos de explotación y análisis defensivo: esteganografía y análisis forense de paquetes PCAP con ROT13 (CWE-311), exposición de directorios web en robots.txt (CWE-200), inyección SQL basada en errores y UNION en MySQL (CWE-89), Cross-Site Scripting almacenado y secuestro de tokens de sesión (CWE-79) y escalación local de privilegios a root mediante el abuso del bit SUID (CWE-250). Adicionalmente, el reto evalúa la capacidad de discriminar falsos positivos (Rabbit Holes) bajo una restricción de tiempo estricta de 60 minutos."
    )
    r.font.name = "Arial"
    r.font.size = Pt(10)

    doc.add_paragraph()

    # 4. TABLA 1: OBJETIVOS
    create_header_table(doc, "1", "OBJETIVOS")

    p_og = doc.add_paragraph()
    r = p_og.add_run("Objetivo General:")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)

    p_og_t = doc.add_paragraph()
    p_og_t.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p_og_t.add_run(
        "Diseñar, implementar, auditar y documentar un entorno gamificado de laboratorio CTF que permita evaluar sistemáticamente las destrezas prácticas en hacking ético ofensivo y defensivo, asegurando la identificación, explotación y propuesta de mitigación de vulnerabilidades de alto impacto según los estándares internacionales OWASP Top 10 y MITRE CWE."
    )
    r.font.name = "Arial"
    r.font.size = Pt(10)

    p_oe = doc.add_paragraph()
    r = p_oe.add_run("Objetivos Específicos:")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)

    objs = [
        "Desplegar un entorno virtualizado aislado y reproducible con Docker y WSL 2 configurado con red Host-Only para pruebas controladas de penetración.",
        "Ejecutar escaneos de puertos y análisis forense de paquetes en Capa 7 (Wireshark/tcpdump) para extraer credenciales e información exfiltrada en cabeceras HTTP.",
        "Auditar mecanismos de indexación web (robots.txt) y extraer artefactos multimedia aplicando técnicas de esteganografía de fin de archivo (EOF).",
        "Identificar y explotar vulnerabilidades de inyección SQL basada en errores y operadores UNION en el backend MySQL, discriminando tablas señuelo de esquemas legítimos.",
        "Explotar vectores de Cross-Site Scripting Almacenado (Stored XSS) y ausencia del atributo HttpOnly para demostrar el secuestro de sesiones administrativas.",
        "Enumerar el sistema de archivos del servidor para identificar binarios con permisos especiales SUID y lograr la escalación local de privilegios a superusuario (root / UID 0).",
        "Formular una matriz integral de mitigaciones técnicas que permita remediar de raíz cada una de las brechas de seguridad identificadas en el laboratorio."
    ]

    for o in objs:
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(o)
        r.font.name = "Arial"
        r.font.size = Pt(10)

    doc.add_paragraph()

    # 5. TABLA 2: DESARROLLO DEL LABORATORIO
    create_header_table(doc, "2", "DESARROLLO DEL LABORATORIO")

    src = docx.Document("Informe_Final_CTF_The27Club_UDEC.docx")

    # A) Recopilar Pasos 1 al 22 (índices 30 al 111 de src.paragraphs)
    print("[*] Copiando Pasos 1 al 22...")
    for idx in range(30, 112):
        if idx < len(src.paragraphs):
            p = src.paragraphs[idx]
            copy_paragraph_with_images(p, doc)

    # B) Recopilar Sección Especial de Gamificación (índices 127 al final de src.paragraphs)
    print("[*] Copiando Sección Especial de Gamificación (Evidencias D-1, D-2, D-3)...")
    for idx in range(127, len(src.paragraphs)):
        p = src.paragraphs[idx]
        copy_paragraph_with_images(p, doc)

    doc.add_paragraph()

    # 6. TABLA 3: CONCLUSIONES
    create_header_table(doc, "3", "CONCLUSIONES")

    print("[*] Copiando Conclusiones...")
    for idx in range(115, 119):
        if idx < len(src.paragraphs):
            p = src.paragraphs[idx]
            copy_paragraph_with_images(p, doc)

    doc.add_paragraph()

    # 7. TABLA 4: TABLA RESUMEN DE BANDERAS Y REFERENCIAS
    create_header_table(doc, "4", "TABLA RESUMEN DE BANDERAS Y REFERENCIAS BIBLIOGRÁFICAS")

    p_t_title = doc.add_paragraph()
    r = p_t_title.add_run("Matriz de Banderas, Señuelos y Mitigaciones - The 27 Club CTF")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10.5)

    table = doc.add_table(rows=1, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    style_data_table(table)

    headers = ["Fase / Artista", "Vulnerabilidad (CWE)", "Tipo de Artefacto", "Cadena / Bandera", "Mitigación Defensiva"]
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.name = "Arial"
        hdr_cells[i].paragraphs[0].runs[0].font.size = Pt(9)

    data = [
        ("Fase 1: Jimi Hendrix", "Exfiltración C&C (CWE-311)", "Bandera Oficial (ROT13)", "FLAG{Purple_Haze_Network}", "Cifrado TLS/HTTPS en tránsito e inspección IDS/IPS."),
        ("Fase 2: Janis Joplin", "Information Exposure (CWE-200)", "Bandera Oficial (Stego EOF)", "FLAG{Cry_Baby_Hidden_Data}", "Saneamiento de metadatos multimedia y control en robots.txt."),
        ("Fase 2 (Rabbit Hole)", "Information Exposure (CWE-200)", "Falso Positivo Señuelo", "RABBIT_HOLE{Sigue_Buscando_Janis_Se_Rie_De_Ti}", "Discriminación de directorios mediante heurística forense."),
        ("Fase 3: Jim Morrison", "SQL Injection (CWE-89 / OWASP A03)", "Bandera Oficial (UNION Based)", "FLAG{Light_My_Fire_SQLi}", "Consultas preparadas (Prepared Statements / PDO) y sanitización."),
        ("Fase 3 (Rabbit Hole)", "SQL Injection (CWE-89)", "Falso Positivo Señuelo", "RABBIT_HOLE{The_End_Is_Not_Here}", "Enumeración rigurosa de esquemas de datos previo a la extracción."),
        ("Fase 4: Amy Winehouse", "Stored XSS (CWE-79 / OWASP A03)", "Bandera Oficial (Session Theft)", "FLAG{Back_To_Black_XSS}", "Codificación contextual en salida y directivas HttpOnly y CSP."),
        ("Fase 4 (Rabbit Hole)", "Stored XSS (CWE-79)", "Falso Positivo Señuelo", "RABBIT_HOLE{Rehab_Was_A_Lie}", "Validación de atributos en cookies y tokens de prueba."),
        ("Fase 5: Kurt Cobain", "Permisos Excesivos SUID (CWE-250)", "Bandera Final Root (UID 0)", "FLAG{Smells_Like_Root_Spirit}", "Auditoría periódica de binarios con bit SUID y restricción de sudoers.")
    ]

    for row in data:
        row_cells = table.add_row().cells
        for idx, text in enumerate(row):
            row_cells[idx].text = text
            row_cells[idx].paragraphs[0].runs[0].font.name = "Arial"
            row_cells[idx].paragraphs[0].runs[0].font.size = Pt(8.5)

    doc.add_paragraph()

    # REFERENCIAS
    p_ref_title = doc.add_paragraph()
    r = p_ref_title.add_run("Referencias Bibliográficas (Formato IEEE)")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10.5)

    print("[*] Copiando Referencias IEEE...")
    for idx in range(121, 127):
        if idx < len(src.paragraphs):
            p = src.paragraphs[idx]
            copy_paragraph_with_images(p, doc)

    # Guardar en OUT_PATH
    doc.save(OUT_PATH)
    print(f"\n[+] ¡Documento oficial '{OUT_PATH}' generado exitosamente!")
    print(f"[+] Total párrafos: {len(doc.paragraphs)}")
    print(f"[+] Total imágenes: {len(doc.inline_shapes)}")
    print(f"[+] Total tablas de sección institucional: {len(doc.tables)}")

if __name__ == "__main__":
    build_rubrica_document()
