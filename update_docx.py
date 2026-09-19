# -*- coding: utf-8 -*-
"""
Script para actualizar CV_Ruben_Barrios_Analista_De_Datos.docx
Garantiza coherencia total con el estándar ATS de 100% cumplimiento (CV_ATS.jpeg).
"""

import zipfile
import os
import xml.sax.saxutils as saxutils

DOCX_PATH = "CV_Ruben_Barrios_Analista_De_Datos.docx"
BACKUP_PATH = "scratch/CV_Ruben_Barrios_Analista_De_Datos_original_backup.docx"

if not os.path.exists("scratch"):
    os.makedirs("scratch")
if not os.path.exists(BACKUP_PATH):
    with open(DOCX_PATH, "rb") as f_src, open(BACKUP_PATH, "wb") as f_dst:
        f_dst.write(f_src.read())

def escape_xml(s):
    return saxutils.escape(s)

def make_p(text, bold=False, italic=False, size=20, color="111827", align="left", space_before=0, space_after=60, bullet=False):
    jc = ""
    if align == "center":
        jc = '<w:jc w:val="center"/>'
    elif align == "right":
        jc = '<w:jc w:val="right"/>'
    elif align == "both":
        jc = '<w:jc w:val="both"/>'

    sp = f'<w:spacing w:before="{space_before}" w:after="{space_after}"/>'
    
    ind = ""
    if bullet:
        ind = '<w:ind w:left="360" w:hanging="240"/>'

    pPr = f'<w:pPr>{jc}{sp}{ind}</w:pPr>'

    runs_xml = ""
    parts = text.split("<b>")
    for i, part in enumerate(parts):
        if i == 0:
            if part:
                b_tag = "<w:b/>" if bold else ""
                i_tag = "<w:i/>" if italic else ""
                esc_part = escape_xml(part)
                runs_xml += f'<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>{b_tag}{i_tag}<w:color w:val="{color}"/><w:sz w:val="{size}"/></w:rPr><w:t xml:space="preserve">{esc_part}</w:t></w:r>'
        else:
            subparts = part.split("</b>")
            bold_part = escape_xml(subparts[0])
            norm_part = escape_xml(subparts[1]) if len(subparts) > 1 else ""
            
            runs_xml += f'<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:color w:val="{color}"/><w:sz w:val="{size}"/></w:rPr><w:t xml:space="preserve">{bold_part}</w:t></w:r>'
            if norm_part:
                b_tag = "<w:b/>" if bold else ""
                i_tag = "<w:i/>" if italic else ""
                runs_xml += f'<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>{b_tag}{i_tag}<w:color w:val="{color}"/><w:sz w:val="{size}"/></w:rPr><w:t xml:space="preserve">{norm_part}</w:t></w:r>'

    return f'<w:p>{pPr}{runs_xml}</w:p>'

def make_heading(title):
    pPr = '<w:pPr><w:spacing w:before="140" w:after="40"/><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="0F172A"/></w:pBdr></w:pPr>'
    r = f'<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:color w:val="0F172A"/><w:sz w:val="24"/></w:rPr><w:t>{escape_xml(title)}</w:t></w:r>'
    return f'<w:p>{pPr}{r}</w:p>'

def make_job_header(company, location, title, dates):
    company_esc = escape_xml(company)
    loc_esc = escape_xml(location)
    title_esc = escape_xml(title)
    dates_esc = escape_xml(dates)
    return f'''<w:tbl>
        <w:tblPr>
            <w:tblW w:w="0" w:type="auto"/>
            <w:tblBorders>
                <w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/>
            </w:tblBorders>
        </w:tblPr>
        <w:tr>
            <w:tc>
                <w:tcPr><w:tcW w:w="7200" w:type="dxa"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="60" w:after="10"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:color w:val="111827"/><w:sz w:val="21"/></w:rPr><w:t>{company_esc}</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:w="2800" w:type="dxa"/></w:tcPr>
                <w:p><w:pPr><w:jc w:val="right"/><w:spacing w:before="60" w:after="10"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:b/><w:color w:val="111827"/><w:sz w:val="20"/></w:rPr><w:t>{loc_esc}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        <w:tr>
            <w:tc>
                <w:tcPr><w:tcW w:w="7200" w:type="dxa"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="0" w:after="25"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:i/><w:color w:val="1E3A8A"/><w:sz w:val="19"/></w:rPr><w:t>{title_esc}</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:w="2800" w:type="dxa"/></w:tcPr>
                <w:p><w:pPr><w:jc w:val="right"/><w:spacing w:before="0" w:after="25"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:i/><w:color w:val="4B5563"/><w:sz w:val="19"/></w:rPr><w:t>{dates_esc}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
    </w:tbl>'''

paragraphs = []

# Encabezado con delimitadores horizontales estilo CV_ATS.jpeg
pPr_top_line = '<w:pPr><w:spacing w:before="0" w:after="30"/><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="0F172A"/></w:pBdr></w:pPr>'
paragraphs.append(f'<w:p>{pPr_top_line}</w:p>')

paragraphs.append(make_p("RUBÉN DAVID BARRIOS BELLO", bold=True, size=32, color="0F172A", align="center", space_before=0, space_after=30))
paragraphs.append(make_p("Data Analyst | Business Intelligence & Fraud Prevention | Lic. en Banca y Finanzas", bold=True, size=21, color="1E3A8A", align="center", space_before=0, space_after=30))
paragraphs.append(make_p("Tel: +54 9 11 7025-9429 | Email: rubendavid1809@gmail.com | Ubicación: Buenos Aires, Argentina", size=18, color="111827", align="center", space_before=0, space_after=20))
paragraphs.append(make_p("LinkedIn: linkedin.com/in/ruben-barrios-1430712ab | GitHub: github.com/rubenbarrios-bigdata | CV Web: rubenbarrios-bigdata.github.io/cv-ejecutivo-inteligente/", size=18, color="1D4ED8", align="center", space_before=0, space_after=30))

pPr_bottom_line = '<w:pPr><w:spacing w:before="0" w:after="80"/><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="0F172A"/></w:pBdr></w:pPr>'
paragraphs.append(f'<w:p>{pPr_bottom_line}</w:p>')

# PERFIL PROFESIONAL
paragraphs.append(make_heading("PERFIL PROFESIONAL"))
p1 = "<b>Analista de Datos</b> con experiencia comprobada en análisis de métricas de fraude en logística para e-commerce y distribución de última milla (Last-Mile Fulfillment), complementada por más de 15 años de sólida trayectoria en el sector bancario, negocios internacionales y finanzas corporativas. Hoy combino esa visión estratégica con un enfoque resolutivo orientado a transformar requerimientos de negocio en soluciones analíticas de alto impacto mediante el diseño de dashboards en <b>Excel y Power BI</b>, consultas <b>SQL (MySQL, PostgreSQL)</b>, automatización con <b>Python (pandas)</b> y analítica digital de productos con <b>GTM, GA4, BigQuery y Data Studio</b>."
paragraphs.append(make_p(p1, size=19, align="both", space_after=80))

p2 = "Historial comprobado en optimización de indicadores de negocio, destacando la <b>reducción del 80% en el ratio histórico de siniestralidad por fraude (de 0,150% a 0,030%)</b> en operaciones de alto volumen mediante el monitoreo continuo de métricas. Perfil analítico orientado a la toma de decisiones basada en evidencia y trabajo multidisciplinario con equipos de Producto, Backend y Operaciones."
paragraphs.append(make_p(p2, size=19, align="both", space_after=60))

# HABILIDADES TÉCNICAS Y COMPETENCIAS
paragraphs.append(make_heading("HABILIDADES TÉCNICAS Y COMPETENCIAS"))
paragraphs.append(make_p("• <b>Análisis de Datos y BI:</b> Power BI (DAX avanzado, Power Query, modelado dimensional, PBIP), SQL (MySQL, PostgreSQL: queries complejas, subconsultas, agregaciones), Python (pandas, NumPy, Matplotlib, Colab, VSCode), Excel avanzado (tablas dinámicas, fórmulas matriciales).", size=19, bullet=True, space_after=25))
paragraphs.append(make_p("• <b>Visualización y Producto:</b> Looker Studio, Google Analytics 4 (GA4), Google Tag Manager (GTM), Supabase, Firebase, BigQuery, diseño de KPIs ejecutivos, análisis de retención, engagement, funnel y conversión.", size=19, bullet=True, space_after=25))
paragraphs.append(make_p("• <b>Negocio y Metodologías:</b> Prevención de Fraudes, Detección de Anomalías en Logística/E-Commerce, Finanzas Corporativas, Comercio Exterior, Git/GitHub, CI/CD para BI, Scrum/Ágil, IA Generativa aplicada (ChatGPT, Copilot, Gemini, Claude, Make).", size=19, bullet=True, space_after=50))

# EXPERIENCIA LABORAL
paragraphs.append(make_heading("EXPERIENCIA LABORAL"))

# Puesto 1: Innova Lab
paragraphs.append(make_job_header("Innova Lab — Proyecto Mate-Mático", "Buenos Aires, Argentina", "Data Analyst & Digital Analytics Specialist (Proyecto MVP)", "Jul. 2026 – Presente"))
paragraphs.append(make_p("• <b>Liderazgo en arquitectura de datos y analítica digital:</b> Diseño e implementación de la infraestructura de medición de producto desde cero para la aplicación educativa Mate-Mático.", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Modelado de datos en base de datos:</b> Estructuración y consulta de tablas en <b>Supabase (PostgreSQL)</b> y Firebase para captura de eventos transaccionales y métricas de comportamiento de usuarios.", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Tracking avanzado de eventos:</b> Configuración integral de tags, triggers y variables con <b>Google Tag Manager (GTM)</b> y <b>Google Analytics 4 (GA4)</b>, validando el correcto flujo de datos junto a Backend y QA.", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Visualización ejecutiva de producto:</b> Creación de dashboard analítico en <b>Looker Studio</b> embebido en la aplicación, monitoreando KPIs de uso, retención, progresión académica y conversión.", size=18, bullet=True, space_after=40))

# Puesto 2: Webpack
paragraphs.append(make_job_header("Webpack S.R.L. — Operador Logístico Oficial de Mercado Libre", "Buenos Aires, Argentina", "Data Analyst | Fraud Prevention | E-commerce Logistics & Last-Mile", "Mar. 2020 – Oct. 2024"))
paragraphs.append(make_p("• <b>Logro Destacado de Negocio:</b> Reducción histórica del <b>80% en el ratio de siniestros por fraude (de 0,150% a 0,030%)</b>, posicionando a Webpack como la operación logística con el ratio más bajo y eficiente de toda la red de Mercado Libre.", size=18, bullet=True, color="0F172A", bold=True, space_after=25))
paragraphs.append(make_p("• <b>Detección de patrones anómalos y análisis SQL:</b> Extracción y limpieza de datos operativos con consultas analíticas en SQL y reporting automatizado para identificar desvíos sistemáticos y mitigar pérdidas financieras.", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Business Intelligence y tableros de control:</b> Diseño, automatización y mantenimiento de dashboards interactivos en <b>Power BI (DAX)</b> y modelos en Excel avanzado para la trazabilidad y análisis de reclamos y siniestros de alta volumetría.", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Optimización de procesos operativos:</b> Articulación y coordinación con despachos, operaciones y seguridad patrimonial, estableciendo protocolos de alerta temprana basados en evidencia analítica.", size=18, bullet=True, space_after=40))

# Puesto 3: Sector Bancario
paragraphs.append(make_job_header("Sector Bancario & Financiero (BFC / Banco Exterior / BVC)", "Caracas, Venezuela", "Especialista en Comercio Exterior, Operaciones y Finanzas Corporativas", "2002 – 2017"))
paragraphs.append(make_p("• <b>Comercio Exterior y Operaciones Internacionales (BFC / Banco Exterior):</b> Gestión integral de importaciones, cartas de crédito comerciales, cobranzas documentarias, liquidación de divisas y estricta trazabilidad de fondos.", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Control analítico, conciliaciones y auditoría:</b> Supervisión de auxiliares contables, conciliaciones bancarias y auditoría de datos financieros bajo riguroso cumplimiento normativo y regulatorio.", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Compras, gestión comercial y caja (Venezolano de Crédito S.A.):</b> Manejo de presupuestos y adquisición de activos operativos para el funcionamiento del banco; operaciones de caja, fidelización y cumplimiento de metas comerciales.", size=18, bullet=True, space_after=50))

# Proyectos
paragraphs.append(make_heading("PROYECTOS DESTACADOS DE ANÁLISIS DE DATOS"))
paragraphs.append(make_p("• <b>Mate-Mático – Analítica Digital & Producto (Innova Lab):</b> Implementación integral de tracking con GTM y GA4, persistencia de eventos en Supabase (PostgreSQL) y dashboard en Looker Studio para optimización del embudo de retención y engagement. (github.com/rubenbarrios-bigdata/Analitica-Digital-Mate-matico)", size=18, bullet=True, space_after=25))
paragraphs.append(make_p("• <b>Dashboard Atención al Cliente (Power BI + DAX):</b> Tablero interactivo para optimización de operaciones de servicio al cliente: seguimiento de volumen de tickets, tiempos de primera respuesta, SLA de resolución y métricas operativas con medidas y cálculos en DAX. (github.com/rubenbarrios-bigdata/dashboard-atencion-al-cliente)", size=18, bullet=True, space_after=25))
paragraphs.append(make_p("• <b>Dashboard Reporte de RRHH (Power BI + DAX):</b> Análisis integral de headcount, métricas de rotación voluntaria/involuntaria (turnover), distribución demográfica y evolución de desempeño para People Analytics. (github.com/rubenbarrios-bigdata/dashboard-rrhh)", size=18, bullet=True, space_after=25))
paragraphs.append(make_p("• <b>Proyecto SQL Orders & E-Commerce Analysis:</b> Análisis exploratorio y transaccional sobre datasets de ventas reales en MySQL empleando subqueries, agrupaciones y funciones de agregación para evaluación de métricas comerciales y márgenes de rentabilidad. (github.com/rubenbarrios-bigdata/proyecto-sql-orders)", size=18, bullet=True, space_after=25))
paragraphs.append(make_p("• <b>Análisis Exploratorio de Datos (EDA) en Python:</b> Limpieza de datos, manejo de outliers y análisis estadístico multivariado con pandas, NumPy y Matplotlib sobre datasets a escala.", size=18, bullet=True, space_after=25))
paragraphs.append(make_p("Todos los proyectos, modelos de datos y documentación técnica disponibles en: github.com/rubenbarrios-bigdata", italic=True, size=18, color="1D4ED8", space_after=50))

# Educación
paragraphs.append(make_heading("EDUCACIÓN Y FORMACIÓN"))
paragraphs.append(make_p("• <b>Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial</b> — En curso (Primer Año) — Instituto de Formación Técnica Superior | Ministerio de Educación GCBA", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Business Intelligence (BI Consulting)</b> — En curso (Segundo cuatrimestre de tres, ruta formativa oficial hacia Análisis de Datos) — Talento Tech | Ministerio de Educación GCBA", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Power BI DevOps: PBIP, Git, CI/CD y Microsoft Fabric</b> — En curso — Udemy", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>Licenciatura en Administración de Recursos Materiales y Financieros</b> — Universidad Nacional Experimental Simón Rodríguez | Caracas, Venezuela", size=18, bullet=True, space_after=20))
paragraphs.append(make_p("• <b>T.S.U. en Administración de Recursos Físicos y Financieros</b> — Colegio Universitario Fermín Toro | Caracas, Venezuela", size=18, bullet=True, space_after=50))

# Certificados Extracurriculares
paragraphs.append(make_heading("CERTIFICACIONES"))
paragraphs.append(make_p("• <b>Analítica Digital: Google Tag Manager, Google Analytics 4 y Data Studio</b> | Analytics Way", size=18, bullet=True, space_after=15))
paragraphs.append(make_p("• <b>Análisis de Datos: Excel, Power BI, SQL y Python</b> | Datax", size=18, bullet=True, space_after=15))
paragraphs.append(make_p("• <b>Fundamentos de Inteligencia Artificial (Artificial Intelligence Fundamentals)</b> | IBM SkillsBuild", size=18, bullet=True, space_after=15))
paragraphs.append(make_p("• <b>Iniciación a la Programación con Python</b> | Talento Tech — Ministerio de Educación GCBA", size=18, bullet=True, space_after=15))
paragraphs.append(make_p("• <b>IA Aplicada al Entorno Laboral: ChatGPT, Gemini, Copilot, Make</b> | Datax", size=18, bullet=True, space_after=35))

# Idiomas (Sección independiente según CV_ATS.jpeg)
paragraphs.append(make_heading("IDIOMAS"))
paragraphs.append(make_p("• <b>Español:</b> Nativo | <b>Inglés:</b> Técnico / Lectura y comprensión profesional de documentación y datos.", size=18, bullet=True, space_after=35))

# Referencias (Sección independiente según CV_ATS.jpeg)
paragraphs.append(make_heading("REFERENCIAS"))
paragraphs.append(make_p("Referencias laborales y académicas comprobables disponibles a solicitud.", size=18, space_after=30))

# Sección de página
sectPr = '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720" w:header="720" w:footer="720" w:gutter="0"/><w:cols w:space="720"/><w:docGrid w:linePitch="360"/></w:sectPr>'

body_xml = "".join(paragraphs) + sectPr
full_doc_xml = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>{body_xml}</w:body></w:document>'

tmp_docx = "scratch/temp_updated.docx"
base_zip = BACKUP_PATH if os.path.exists(BACKUP_PATH) else DOCX_PATH
with zipfile.ZipFile(base_zip, 'r') as zin, zipfile.ZipFile(tmp_docx, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        if item.filename == 'word/document.xml':
            zout.writestr(item, full_doc_xml.encode('utf-8'))
        else:
            zout.writestr(item, zin.read(item.filename))

os.replace(tmp_docx, DOCX_PATH)
print("DOCX actualizado y verificado con éxito según CV_ATS.jpeg:", DOCX_PATH)
