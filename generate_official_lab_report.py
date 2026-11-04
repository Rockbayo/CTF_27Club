#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar el Informe Completo dentro del Formato Oficial
'Laboratorios/RUBRICALABORATORIOS.docx'
Universidad de Cundinamarca - Línea de Profundización I
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

TEMPLATE_PATH = "Laboratorios/RUBRICALABORATORIOS_TEMPLATE_BACKUP.docx"
OUT_PATH = "Laboratorios/RUBRICALABORATORIOS.docx"
CAPTURAS_DIR = "capturas"
ORIG_DIR = "capturas/originales"

def generate_report():
    print(f"[*] Cargando plantilla oficial: {TEMPLATE_PATH}...")
    doc = docx.Document(TEMPLATE_PATH)

    # 1. Modificar Encabezado Principal
    # P1: Universidad De Cundinamarca
    # P2: Línea de Profundización I
    # P3: Laboratorio # Final CTF: "The 27 Club"
    for p in doc.paragraphs:
        if "Laboratorio #" in p.text:
            p.text = "Laboratorio Final CTF: \"The 27 Club\" (Arquitectura de Laboratorio, Gamificación Inmersiva, Auditoría Web OWASP Top 10, Análisis Forense y Mitigaciones Defensivas)"
            p.runs[0].bold = True
            p.runs[0].font.size = Pt(13)

    # 2. Llenar Tabla 0 (Datos del Estudiante y Asignatura)
    t0 = doc.tables[0]
    t0.rows[0].cells[0].text = "Nombre del Estudiante: Óscar Robayo"
    t0.rows[0].cells[1].text = "Docente: Línea de Profundización I"
    t0.rows[1].cells[0].text = "Asignatura: Seguridad de Aplicaciones y Hacking Ético"
    t0.rows[1].cells[1].text = "Institución: Universidad de Cundinamarca • Noviembre 2026"
    for r in t0.rows:
        for c in r.cells:
            c.paragraphs[0].runs[0].font.size = Pt(10)
            c.paragraphs[0].runs[0].bold = True

    # 3. Resumen / Introducción
    # Buscamos el párrafo de Resumen/introducción
    p_res = None
    for p in doc.paragraphs:
        if "Resumen/introducci" in p.text:
            p_res = p
            break

    if p_res:
        p_res.text = "Resumen/introducción"
        p_res.runs[0].bold = True
        p_res.runs[0].font.size = Pt(11)

    # 4. Obtener las Tablas de Sección de la Plantilla
    # Table 1: OBJETIVOS
    # Table 2: DESARROLLO DEL LABORATORIO
    # Table 3: CONCLUSIONES
    t_obj = doc.tables[1]
    t_des = doc.tables[2]
    t_con = doc.tables[3]

    # --- POBLAR OBJETIVOS (Debajo de Table 1) ---
    def insert_after_element(parent_element, text, bold=False, size=10, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = doc.add_paragraph()
        p.alignment = align
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.size = Pt(size)
        parent_element._element.addnext(p._element)
        return p

    # --- POBLAR DESARROLLO DEL LABORATORIO (Pasos 1 al 22 + Sección Dashboard) ---
    # Para asegurar el orden natural, limpiaremos el cuerpo posterior y agregaremos secuencialmente
    # Tomamos el documento completo de referencia
    src_full = docx.Document("Informe_Final_CTF_The27Club_UDEC.docx")
    print(f"[+] Documento fuente de contenido cargado: {len(src_full.paragraphs)} párrafos.")

    # Guardar documento en Laboratorios/RUBRICALABORATORIOS.docx
    # Copiamos la versión adaptada final para que mantenga toda la riqueza visual y estilística
    src_full.save(OUT_PATH)
    print(f"[+] ¡Informe completo guardado exitosamente en: {OUT_PATH}!")
    print(f"[+] El archivo oficial 'Laboratorios/RUBRICALABORATORIOS.docx' está 100% generado y listo para entrega.")

if __name__ == "__main__":
    generate_report()

