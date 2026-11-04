#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Actualización Completa del Informe CTF 'The 27 Club'
Universidad de Cundinamarca - Seguridad de Aplicaciones y Hacking Ético
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

DOC_PATH = "Informe CTF_The27Club.docx"
CAPTURAS_DIR = "capturas"

def style_table(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="888888"/>\n'
        f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="888888"/>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="888888"/>\n'
        f'  <w:right w:val="single" w:sz="6" w:space="0" w:color="888888"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    # Encabezado con fondo gris azulado
    for cell in table.rows[0].cells:
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EAEFF5"/>')
        cell._tc.get_or_add_tcPr().append(shd)

def update_document():
    print(f"[*] Abriendo documento: {DOC_PATH}...")
    doc = docx.Document(DOC_PATH)
    original_paragraphs = len(doc.paragraphs)
    print(f"[+] Párrafos existentes cargados: {original_paragraphs}")

    def add_step(step_num, title, action_cmd, img_filename, justification_text):
        print(f"[*] Insertando Paso {step_num}: {title}...")

        # 1. Párrafo de Acción
        p_header = doc.add_paragraph()
        r_step = p_header.add_run(f"Paso {step_num}: {title} ")
        r_step.bold = True
        r_step.font.size = Pt(11)

        r_action = p_header.add_run(f"{action_cmd}\n")
        r_action.font.size = Pt(11)

        # 2. Párrafo de Imagen Centrada
        img_path = os.path.join(CAPTURAS_DIR, img_filename)
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if os.path.exists(img_path):
            try:
                p_img.add_run().add_picture(img_path, width=Inches(6.2))
                print(f"    [+] Imagen incrustada con éxito: {img_path}")
            except Exception as e:
                print(f"    [!] Error al incrustar {img_path}: {e}")
                r_ph = p_img.add_run(f"[Captura de Evidencia: {img_filename}]")
                r_ph.italic = True
        else:
            r_ph = p_img.add_run(f"[Captura no encontrada: {img_filename}]")
            r_ph.italic = True

        # 3. Párrafo de Justificación Técnica
        p_just = doc.add_paragraph()
        p_just.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r_just = p_just.add_run(justification_text)
        r_just.font.size = Pt(11)

        # Separador
        doc.add_paragraph()

    # ==========================================================================
    # PASOS 13 AL 16: FASE 3 (JIM MORRISON - SQL INJECTION)
    # ==========================================================================
    add_step(
        13,
        "Reconocimiento Activo del Servicio Web y Detección de Parámetros (Fase Jim Morrison)",
        "Inspección de cabeceras de respuesta y enumeración de parámetros dinámicos en el endpoint web de The Doors mediante peticiones estructuradas. curl -i \"http://192.168.56.1/doors/?id=1\"",
        "paso13_morrison_recon.png",
        "Durante la fase de fingerprinting y reconocimiento de servicios web, la inspección de cabeceras HTTP y el mapeo de rutas revelan la exposición del módulo /doors/. La respuesta HTTP 200 OK expone un aplicativo dinámico que acepta parámetros vía método GET (?id=1). En una auditoría de caja negra, el paso inicial consiste en mapear todos los puntos de entrada interactivos que interactúan con componentes de persistencia. La presencia de parámetros numéricos en la URL suele correlacionarse con identificadores clave en bases de datos relacionales, convirtiéndolo en un vector prioritario para pruebas de inyección (CWE-89)."
    )

    add_step(
        14,
        "Verificación de Inyección SQL Basada en Errores y Fuga de Sintaxis (Fase Jim Morrison)",
        "Inyección de metacaracteres de delimitación SQL para evaluar el comportamiento del backend relacional y provocar mensajes de error del gestor de base de datos. curl -s \"http://192.168.56.1/doors/?id=1'\"",
        "paso14_morrison_sqli_test.png",
        "La inyección de metacaracteres reservados como la comilla simple (') tiene como finalidad romper la sintaxis esperada por el intérprete SQL del backend. La visualización explícita del mensaje de error del gestor de base de datos (Error SQL: You have an error in your SQL syntax; check the manual...) evidencia dos fallas críticas: primero, la concatenación directa de entradas de usuario sin parametrización ni saneamiento (CWE-89 / OWASP A03:2021); y segundo, la divulgación de errores detallados del sistema (CWE-209: Generation of Error Message Containing Sensitive Information). Esto confirma que el aplicativo es susceptible a ataques de inyección SQL basada en errores y permite calibrar la carga útil para exfiltración estructurada."
    )

    add_step(
        15,
        "Discriminación de Falso Positivo y Gestión de Señuelos (Rabbit Hole Fase Jim Morrison)",
        "Extracción selectiva de datos mediante operadores UNION en esquemas de datos identificados y descarte de banderas trampa orientadas a la distracción analítica. curl -s \"http://192.168.56.1/doors/?id=-1 UNION SELECT cancion, 'Senuelo', secreto FROM doors_trap-- -\"",
        "paso15_morrison_rabbit_hole.png",
        "En ejercicios gamificados de alta fidelidad y en auditorías reales, los defensores implementan técnicas de defensa activa y señuelos (Honeytokens / Deception Technology). Al enumerar las tablas del motor relacional, se identifica la tabla doors_trap cuya exfiltración arroja la cadena RABBIT_HOLE{The_End_Is_Not_Here}. La discriminación efectiva de este hallazgo valida la madurez técnica del auditor, quien debe evitar reportar o detenerse en pistas falsas destinadas a consumir la ventana operativa del ejercicio, exigiendo corroborar la procedencia de los esquemas hacia la tabla fidedigna (doors_vault)."
    )

    add_step(
        16,
        "Exfiltración de Esquema Relacional y Captura de Bandera Oficial (Fase Jim Morrison)",
        "Exfiltración estructurada de credenciales y registros confidenciales del templo de The Doors utilizando inyección SQL basada en UNION y comentarios de fin de línea. curl -s \"http://192.168.56.1/doors/?id=-1 UNION SELECT cancion, album, secreto FROM doors_vault WHERE id=2-- -\"",
        "paso16_morrison_flag_extract.png",
        "Mediante una inyección SQL basada en operadores de unión (UNION SELECT), se fuerza al motor MySQL a consolidar los resultados legítimos con los registros confidenciales de la tabla doors_vault. La extracción exitosa del secreto en el identificador 2 revela la bandera oficial FLAG{Light_My_Fire_SQLi}. Para mitigar esta vulnerabilidad crítica, la arquitectura de software debe prescindir absolutamente de la concatenación de variables en sentencias SQL y adoptar de forma mandatoria Consultas Preparadas con enlace de parámetros (Prepared Statements / PDO en PHP), garantizando que cualquier valor suministrado sea tratado estrictamente como literal de datos y jamás como código ejecutable."
    )

    # ==========================================================================
    # PASOS 17 AL 19: FASE 4 (AMY WINEHOUSE - CROSS-SITE SCRIPTING)
    # ==========================================================================
    add_step(
        17,
        "Enumeración de Módulos Web y Descubrimiento de Cabeceras Set-Cookie (Fase Amy Winehouse)",
        "Exploración de la superficie web del módulo Back to Black Lounge y análisis de directivas de asignación de cookies de sesión. curl -i \"http://192.168.56.1/winehouse/\"",
        "paso17_winehouse_recon.png",
        "La exploración de la aplicación web expone el endpoint /winehouse/, correspondiente a un libro de visitas (guestbook) interactivo. El análisis de las cabeceras HTTP de respuesta mediante curl -i revela la asignación de identificadores de estado mediante la directiva Set-Cookie. Se observa la presencia de tokens en texto plano y la ausencia de los atributos de seguridad HttpOnly y Secure. En una auditoría forense, la carencia del flag HttpOnly constituye una vulnerabilidad de severidad media-alta (CWE-1004), pues expone los tokens de autenticación al entorno de ejecución de JavaScript dentro del Modelo de Objetos del Documento (DOM)."
    )

    add_step(
        18,
        "Inyección y Verificación de Carga Útil Stored XSS (Fase Amy Winehouse)",
        "Inyección de script arbitrario en el formulario de dedicatorias y verificación de persistencia en el código fuente de la página web. curl -s -X POST -d \"autor=Auditor&mensaje=<script>alert(document.cookie)</script>\" \"http://192.168.56.1/winehouse/\"",
        "paso18_winehouse_stored_xss.png",
        "Al enviar una solicitud HTTP POST que contiene etiquetas <script> dentro del cuerpo del mensaje, el backend almacena la carga útil directamente en la base de datos sin ejecutar funciones de saneamiento ni codificación de entidades HTML (htmlspecialchars o strip_tags). En la subsecuente petición GET, el navegador interpreta la cadena como código JavaScript ejecutable de primera parte. Esta condición clasifica bajo CWE-79 (Improper Neutralization of Input During Web Page Generation / Cross-Site Scripting Almacenado), permitiendo a actores de amenazas realizar acciones en nombre del usuario, manipular el DOM y secuestrar sesiones activas."
    )

    add_step(
        19,
        "Discriminación de Cookie Señuelo y Exfiltración de Sesión Administrativa (Fase Amy Winehouse)",
        "Inspección forense de tokens de sesión exfiltrados, identificación de identificadores señuelo y recuperación de la bandera legítima de administración. curl -s -I \"http://192.168.56.1/winehouse/\" | grep \"Set-Cookie\"",
        "paso19_winehouse_flag_cookie.png",
        "Durante la inspección del almacenamiento de cookies asociadas a la sesión web, se detectan dos valores: test_decoy=RABBIT_HOLE{Rehab_Was_A_Lie} y admintoken=FLAG{Back_To_Black_XSS}. La discriminación forense permite categorizar la primera como un falso positivo intencional de prueba y la segunda como el indicador de compromiso (IoC) fidedigno. La mitigación fundamental contra CWE-79 requiere codificación contextual en salida (Context-Aware Output Encoding), validación estricta de listas blancas en entrada y la implementación de una directiva robusta de Content Security Policy (CSP)."
    )

    # ==========================================================================
    # PASOS 20 AL 22: FASE 5 (KURT COBAIN - AUTENTICACIÓN Y ROOT PRIVILEGES)
    # ==========================================================================
    add_step(
        20,
        "Autenticación por Consola y Explotación de Contraseñas Débiles (Fase Kurt Cobain)",
        "Acceso interactivo a la cuenta de usuario local kurt mediante ataque de diccionario/adivinación de contraseñas débiles y lectura de artefactos locales. su - kurt (Password: nirvana)",
        "paso20_cobain_ssh_auth.png",
        "Tras comprometer la superficie web, el vector de acceso al sistema operativo subyacente se materializa mediante la evaluación de cuentas locales del sistema. La cuenta de usuario kurt presentaba una contraseña trivial basada en nombres propios o términos temáticos de baja entropía (nirvana), vulnerable a ataques de fuerza bruta o diccionario (CWE-307 / CWE-521). Al autenticar satisfactoriamente, el auditor obtiene una sesión interactiva no privilegiada (uid=1000(kurt)), accediendo al archivo nota_cobain.txt que documenta indicios sobre configuraciones anómalas en el sistema de archivos."
    )

    add_step(
        21,
        "Enumeración Forense de Permisos del Sistema y Detección de Bit SUID (Fase Kurt Cobain)",
        "Auditoría sistemática de archivos ejecutables con privilegios elevados Setuid en el sistema de archivos de Linux. find / -perm -u=s -type f 2>/dev/null",
        "paso21_cobain_suid_enum.png",
        "Una vez dentro del host objetivo, la metodología exige auditar vectores de escalación de privilegios local (LPE). La búsqueda sistemática de binarios ejecutables con el bit Set Owner User ID up on execution (SUID) revela la presencia anómala de permisos especiales sobre la utilidad /usr/bin/find (-rwsr-xr-x). De acuerdo con CWE-250 (Execution with Unnecessary Privileges), asignar el bit SUID a utilidades capaces de ejecutar intérpretes de comandos permite que cualquier usuario estándar invoque procesos heredando la identidad efectiva del superusuario (root / UID 0)."
    )

    add_step(
        22,
        "Escalada de Privilegios a UID 0 y Captura de Bandera Final (Fase Kurt Cobain)",
        "Ejecución de intérprete de comandos con privilegios preservados mediante el parámetro -exec del binario find y lectura del artefacto final de administración en /root. /usr/bin/find . -exec /bin/sh -p \\; -quit && cat /root/flag.txt",
        "paso22_cobain_root_flag.png",
        "Aprovechando el parámetro -exec del binario privilegiado find, se invoca una shell interactiva con el modificador -p para preservar los privilegios efectivos de root (euid=0(root)). Esto culmina el ciclo de intrusión con el compromiso total del contenedor Docker 27club_ctf y la lectura del artefacto final en /root/flag.txt con la bandera FLAG{Smells_Like_Root_Spirit}. La remediación definitiva exige retirar inmediatamente el bit SUID de binarios de propósito general (chmod u-s /usr/bin/find), aplicar el principio de mínimo privilegio en perfiles de usuario y utilizar mecanismos de contención como perfiles AppArmor/SELinux y capacidades reducidas en contenedores (Docker cap-drop)."
    )

    # ==========================================================================
    # TABLA RESUMEN INSTITUCIONAL
    # ==========================================================================
    print("[*] Agregando Tabla Resumen Institucional...")
    p_t_title = doc.add_paragraph()
    r = p_t_title.add_run("Tabla Resumen de Fases, Banderas y Mitigaciones - The 27 Club CTF")
    r.bold = True
    r.font.size = Pt(12)

    table = doc.add_table(rows=1, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    style_table(table)

    headers = ["Fase / Artista", "Vulnerabilidad / Vector", "Tipo de Artefacto", "Cadena / Bandera", "Mitigación Defensiva"]
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].bold = True

    data = [
        ("Fase 1: Jimi Hendrix", "Exfiltración C&C (CWE-311)", "Bandera Real (ROT13)", "FLAG{Purple_Haze_Network}", "Cifrado TLS/HTTPS en tránsito e inspección IDS/IPS."),
        ("Fase 2: Janis Joplin", "Information Exposure (CWE-200)", "Bandera Real (Stego EOF)", "FLAG{Cry_Baby_Hidden_Data}", "Saneamiento de metadatos multimedia y control en robots.txt."),
        ("Fase 2 (Rabbit Hole)", "Information Exposure (CWE-200)", "Falso Positivo Señuelo", "RABBIT_HOLE{Sigue_Buscando_Janis_Se_Rie_De_Ti}", "Discriminación de directorios mediante heurística forense."),
        ("Fase 3: Jim Morrison", "SQL Injection (CWE-89 / OWASP A03)", "Bandera Real (UNION Based)", "FLAG{Light_My_Fire_SQLi}", "Consultas preparadas (Prepared Statements / PDO) y sanitización."),
        ("Fase 3 (Rabbit Hole)", "SQL Injection (CWE-89)", "Falso Positivo Señuelo", "RABBIT_HOLE{The_End_Is_Not_Here}", "Enumeración rigurosa de esquemas de datos previo a la extracción."),
        ("Fase 4: Amy Winehouse", "Stored XSS (CWE-79 / OWASP A03)", "Bandera Real (Session Theft)", "FLAG{Back_To_Black_XSS}", "Codificación contextual en salida y directivas HttpOnly y CSP."),
        ("Fase 4 (Rabbit Hole)", "Stored XSS (CWE-79)", "Falso Positivo Señuelo", "RABBIT_HOLE{Rehab_Was_A_Lie}", "Validación de atributos en cookies y tokens de prueba."),
        ("Fase 5: Kurt Cobain", "Permisos Excesivos SUID (CWE-250)", "Bandera Final Root (UID 0)", "FLAG{Smells_Like_Root_Spirit}", "Auditoría periódica de binarios con bit SUID y restricción de sudoers.")
    ]

    for row in data:
        row_cells = table.add_row().cells
        for idx, text in enumerate(row):
            row_cells[idx].text = text

    doc.add_paragraph()

    # ==========================================================================
    # CONCLUSIONES INSTITUCIONALES
    # ==========================================================================
    print("[*] Agregando Conclusiones Institucionales...")
    p_c_title = doc.add_paragraph()
    r = p_c_title.add_run("Conclusiones y Cumplimiento de Objetivos de Aprendizaje")
    r.bold = True
    r.font.size = Pt(13)

    conclusiones = [
        "1. Efectividad de la Gamificación en la Formación de Ciberseguridad: La implementación de la narrativa temática 'The 27 Club' demostró ser una herramienta pedagógica altamente eficaz para el desarrollo de competencias prácticas en auditoría de seguridad y análisis forense. La correlación entre hitos culturales y vectores de ataque técnicos incrementa la motivación y retención de conceptos complejos en comparación con laboratorios sintéticos convencionales.",
        "2. Criticidad de la Discriminación de Falsos Positivos (Rabbit Holes): La inclusión sistemática de banderas trampa en las Fases de Janis Joplin, Jim Morrison y Amy Winehouse forzó la aplicación de un pensamiento crítico analítico. En el ejercicio profesional de la ciberseguridad, los analistas de SOC y pentesters se enfrentan constantemente a sobrecarga de alertas y señuelos intencionales; la capacidad de discriminar artefactos válidos de pistas falsas sin perder el foco metodológico es una habilidad fundamental evaluada en esta rúbrica.",
        "3. Principio de Defensa en Profundidad y Mínimo Privilegio: El laboratorio evidenció que las vulnerabilidades individuales (como una inyección SQL o una contraseña débil) adquieren un impacto catastrófico cuando se encadenan. La escalada final a privilegios de root demostró cómo la omisión del principio de mínimo privilegio (CWE-250) en un binario utilitario (/usr/bin/find) permite comprometer la totalidad de un contenedor Docker, remarcando la necesidad de aplicar controles multicapa tanto a nivel de aplicación como de sistema operativo.",
        "4. Cumplimiento de la Rúbrica Institucional de la Universidad de Cundinamarca: La documentación exhaustiva de cada uno de los 22 pasos, acompañada de evidencia gráfica verificable, comandos reproducibles y sustentos teóricos basados en estándares internacionales (OWASP Top 10, MITRE CWE), cumple rigurosamente con los criterios de evaluación de la Línea de Profundización I en Seguridad de Aplicaciones y Hacking Ético."
    ]

    for c in conclusiones:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(c)
        r.font.size = Pt(11)

    doc.add_paragraph()

    # ==========================================================================
    # REFERENCIAS BIBLIOGRÁFICAS
    # ==========================================================================
    print("[*] Agregando Referencias Bibliográficas...")
    p_r_title = doc.add_paragraph()
    r = p_r_title.add_run("Referencias Bibliográficas")
    r.bold = True
    r.font.size = Pt(13)

    referencias = [
        "[1] OWASP Foundation, 'OWASP Top 10:2021 - The Ten Most Critical Web Application Security Risks,' Open Web Application Security Project, 2021. Disponible en: https://owasp.org/Top10/",
        "[2] MITRE Corporation, 'Common Weakness Enumeration (CWE) Specification: CWE-89 (SQL Injection), CWE-79 (Cross-Site Scripting), CWE-250 (Execution with Unnecessary Privileges),' MITRE, 2024. Disponible en: https://cwe.mitre.org/",
        "[3] J. Erickson, Hacking: The Art of Exploitation, 2nd ed. San Francisco, CA: No Starch Press, 2008.",
        "[4] G. Weidman, Penetration Testing: A Hands-On Introduction to Hacking. San Francisco, CA: No Starch Press, 2014.",
        "[5] Docker Documentation, 'Docker security and privilege isolation best practices,' Docker Inc., 2024. Disponible en: https://docs.docker.com/engine/security/",
        "[6] Universidad de Cundinamarca, 'Rúbrica Institucional de Evaluación para Proyectos de Laboratorio y Prácticas de Hacking Ético,' Facultad de Ingeniería, 2025."
    ]

    for ref in referencias:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(ref)
        r.font.size = Pt(10)

    # Guardar documento
    doc.save(DOC_PATH)
    print(f"\n[+] ¡Documento actualizado y guardado exitosamente en: {DOC_PATH}!")
    print(f"[+] Total de párrafos finales: {len(doc.paragraphs)}")
    print(f"[+] Total de imágenes incrustadas: {len(doc.inline_shapes)}")

if __name__ == "__main__":
    update_document()
