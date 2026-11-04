#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para incorporar los pantallazos y la documentación técnica del
Dashboard Gamificado dentro de 'Informe CTF_The27Club.docx'
Universidad de Cundinamarca - Hacking Ético
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

DOC_PATH = "Informe CTF_The27Club.docx"
FINAL_DOC_PATH = "Informe CTF_The27Club_Final.docx"
CAPTURAS_DIR = "capturas"

def insert_dashboard_section():
    print(f"[*] Abriendo documento base: {DOC_PATH}...")
    doc = docx.Document(DOC_PATH)

    # Crear encabezado de sección
    p_sec = doc.add_paragraph()
    r_sec = p_sec.add_run("Sección Especial de Gamificación: Plataforma Web Interactiva y Tablero de Operaciones CTF")
    r_sec.bold = True
    r_sec.font.size = Pt(13)
    r_sec.font.color.rgb = RGBColor(30, 45, 90)

    p_intro = doc.add_paragraph()
    p_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_intro = p_intro.add_run(
        "Como valor agregado metodológico y en estricto cumplimiento de los criterios de innovación pedagógica exigidos por la Universidad de Cundinamarca, se desarrolló y desplegó un Tablero Web Gamificado interactivo (dashboard_27club.html). Esta herramienta centraliza el cronometraje en tiempo real, la inmersión temática con memorabilia, collage y audio de los artistas, la discriminación de falsos positivos y la validación automatizada de artefactos."
    )
    r_intro.font.size = Pt(11)

    def add_dash_step(title, action_desc, img_name, just_text):
        p_h = doc.add_paragraph()
        r_t = p_h.add_run(f"{title}: ")
        r_t.bold = True
        r_t.font.size = Pt(11)
        r_a = p_h.add_run(f"{action_desc}\n")
        r_a.font.size = Pt(11)

        p_i = doc.add_paragraph()
        p_i.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_p = os.path.join(CAPTURAS_DIR, img_name)
        if os.path.exists(img_p):
            p_i.add_run().add_picture(img_p, width=Inches(6.2))
            print(f"[+] Incrustada: {img_p}")
        else:
            p_i.add_run(f"[Captura pendiente: {img_name}]").italic = True

        p_j = doc.add_paragraph()
        p_j.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r_j = p_j.add_run(just_text)
        r_j.font.size = Pt(11)
        doc.add_paragraph()

    add_dash_step(
        "Evidencia D-1: Tablero Central de Misiones, Cronómetro Oficial (60:00) y Jukebox de Rock",
        "Despliegue y visualización del entorno central de control de auditoría con temporizador de sesión, indicador global de puntaje y reproductor master de audio.",
        "dashboard_general_lounge.png",
        "La integración de un temporizador de 60 minutos simula las restricciones operativas reales a las que se enfrenta un equipo de respuesta a incidentes (CSIRT) o de pentesting durante una ventana de mantenimiento. La arquitectura del dashboard implementa alertas visuales y auditivas dinámicas al restar menos de 10 minutos, fomentando la gestión del estrés y la priorización de vectores de ataque críticos en conformidad con los objetivos de aprendizaje de la Línea de Profundización I."
    )

    add_dash_step(
        "Evidencia D-2: Habitación Temática Inmersiva (Room 3: Jim Morrison), Consola Forense y Vinilo Dinámico",
        "Interacción dentro de la sala temática de The Doors, con reproducción del master original 'Light My Fire', examinación del collage histórico y consola de auditoría SQLi.",
        "dashboard_room_morrison.png",
        "La ambientación contextual por salas individualizadas permite asociar cada vulnerabilidad técnica a una narrativa memorable. En la habitación de Jim Morrison, el analista dispone de una consola interactiva sincronizada con el servicio web en 192.168.56.1/doors/, visualizando el error de sintaxis de MySQL (CWE-89) y discriminando la tabla trampa doors_trap. Este diseño modular refuerza la comprensión práctica de la explotación controlada y el análisis forense de la respuesta del servidor."
    )

    add_dash_step(
        "Evidencia D-3: Consolidación Total de Objetivos y Modo de Sustentación Institucional (1000/1000 PTS)",
        "Validación integral del laboratorio CTF con desbloqueo de los 5 Discos de Oro y panel de certificación de cumplimiento de la rúbrica UDEC.",
        "dashboard_sustentacion_completa.png",
        "El módulo de sustentación institucional permite comprobar de manera inmediata la conquista de los 1000 puntos asignados al reto, certificando la captura de las 5 banderas oficiales y el descarte exitoso de los 3 falsos positivos (Rabbit Holes). La plataforma genera una bitácora inmutable de eventos con marcas temporales, constituyendo una evidencia irrefutable del dominio técnico de los estándares CWE-89, CWE-79, CWE-200 y CWE-250 para la sustentación académica final."
    )

    # Guardar en FINAL_DOC_PATH siempre (no estará bloqueado por Word)
    doc.save(FINAL_DOC_PATH)
    print(f"[+] Documento guardado como copia completa: {FINAL_DOC_PATH}")

    # Intentar guardar también en DOC_PATH si Word no lo tiene bloqueado
    try:
        doc.save(DOC_PATH)
        print(f"[+] Documento principal {DOC_PATH} sobrescrito exitosamente.")
    except PermissionError:
        print(f"[!] Nota: '{DOC_PATH}' está actualmente abierto en Microsoft Word.")
        print(f"    Los cambios con los pantallazos del dashboard quedaron listos en: '{FINAL_DOC_PATH}'")

if __name__ == "__main__":
    insert_dashboard_section()
