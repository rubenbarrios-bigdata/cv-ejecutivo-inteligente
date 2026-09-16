# -*- coding: utf-8 -*-
"""
Generador de CV en PDF Optimizado para Filtros ATS y Reclutadores IT
Candidato: Rubén David Barrios Bello
Soporte Bilingüe:
  - Español: CV_Ruben_Barrios_Analista_De_Datos.pdf
  - Inglés:  CV_Ruben_Barrios_Data_Analyst.pdf
"""

import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

PRIMARY = colors.HexColor("#1A365D")       # Azul marino profundo institucional
SECONDARY = colors.HexColor("#2B6CB0")     # Azul corporativo medio
TEXT_DARK = colors.HexColor("#1A202C")     # Gris muy oscuro para lectura óptima
TEXT_MUTED = colors.HexColor("#4A5568")    # Gris neutro secundario
LINE_COLOR = colors.HexColor("#CBD5E0")    # Línea divisoria sutil
LINK_COLOR = colors.HexColor("#2B6CB0")    # Color de enlaces

class ATSNumberedCanvasES(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(ATSNumberedCanvasES, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            super(ATSNumberedCanvasES, self).showPage()
        super(ATSNumberedCanvasES, self).save()

    def draw_page_elements(self, page_count):
        self.saveState()
        if self._pageNumber > 1:
            self.setFont("Helvetica", 8)
            self.setFillColor(TEXT_MUTED)
            self.drawString(36, 11 * inch - 26, "RUBÉN DAVID BARRIOS BELLO — CURRÍCULUM VITAE")
            self.drawRightString(8.5 * inch - 36, 11 * inch - 26, "DATA ANALYST & BUSINESS INTELLIGENCE")
            self.setStrokeColor(LINE_COLOR)
            self.setLineWidth(0.5)
            self.line(36, 11 * inch - 30, 8.5 * inch - 36, 11 * inch - 30)

        self.setStrokeColor(LINE_COLOR)
        self.setLineWidth(0.5)
        self.line(36, 26, 8.5 * inch - 36, 26)
        self.setFont("Helvetica", 8)
        self.setFillColor(TEXT_MUTED)
        self.drawString(36, 16, "rubendavid1809@gmail.com • Tel. +54 9 11 7025-9429 • Buenos Aires, Argentina")
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(8.5 * inch - 36, 16, page_str)
        self.restoreState()


class ATSNumberedCanvasEN(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(ATSNumberedCanvasEN, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            super(ATSNumberedCanvasEN, self).showPage()
        super(ATSNumberedCanvasEN, self).save()

    def draw_page_elements(self, page_count):
        self.saveState()
        if self._pageNumber > 1:
            self.setFont("Helvetica", 8)
            self.setFillColor(TEXT_MUTED)
            self.drawString(36, 11 * inch - 26, "RUBÉN DAVID BARRIOS BELLO — CURRICULUM VITAE")
            self.drawRightString(8.5 * inch - 36, 11 * inch - 26, "DATA ANALYST & BUSINESS INTELLIGENCE")
            self.setStrokeColor(LINE_COLOR)
            self.setLineWidth(0.5)
            self.line(36, 11 * inch - 30, 8.5 * inch - 36, 11 * inch - 30)

        self.setStrokeColor(LINE_COLOR)
        self.setLineWidth(0.5)
        self.line(36, 26, 8.5 * inch - 36, 26)
        self.setFont("Helvetica", 8)
        self.setFillColor(TEXT_MUTED)
        self.drawString(36, 16, "rubendavid1809@gmail.com • Phone: +54 9 11 7025-9429 • Buenos Aires, Argentina")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 36, 16, page_str)
        self.restoreState()


def get_styles():
    return {
        "Name": ParagraphStyle("Name", fontName="Helvetica-Bold", fontSize=18, leading=20, textColor=PRIMARY, alignment=1, spaceAfter=2),
        "Headline": ParagraphStyle("Headline", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=SECONDARY, alignment=1, spaceAfter=4),
        "Contact": ParagraphStyle("Contact", fontName="Helvetica", fontSize=8.5, leading=11, textColor=TEXT_DARK, alignment=1, spaceAfter=2),
        "Links": ParagraphStyle("Links", fontName="Helvetica", fontSize=8.5, leading=11, textColor=TEXT_DARK, alignment=1, spaceAfter=6),
        "SectionTitle": ParagraphStyle("SectionTitle", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=PRIMARY, spaceBefore=4, spaceAfter=2, keepWithNext=True),
        "JobTitleLeft": ParagraphStyle("JobTitleLeft", fontName="Helvetica-Bold", fontSize=9.2, leading=11.2, textColor=TEXT_DARK),
        "JobDateRight": ParagraphStyle("JobDateRight", fontName="Helvetica-Oblique", fontSize=8.5, leading=11.2, textColor=TEXT_MUTED, alignment=2),
        "JobRole": ParagraphStyle("JobRole", fontName="Helvetica-Bold", fontSize=8.8, leading=10.8, textColor=SECONDARY, spaceAfter=2),
        "Body": ParagraphStyle("Body", fontName="Helvetica", fontSize=8.4, leading=10.8, textColor=TEXT_DARK, alignment=4),
        "Bullet": ParagraphStyle("Bullet", fontName="Helvetica", fontSize=8.2, leading=10.5, textColor=TEXT_DARK, leftIndent=12, firstLineIndent=-12, spaceAfter=1.3),
        "Achievement": ParagraphStyle("Achievement", fontName="Helvetica-Bold", fontSize=8.2, leading=10.5, textColor=PRIMARY, leftIndent=12, firstLineIndent=-12, spaceAfter=2),
        "SkillCategory": ParagraphStyle("SkillCategory", fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, textColor=PRIMARY),
        "SkillText": ParagraphStyle("SkillText", fontName="Helvetica", fontSize=8.3, leading=10.5, textColor=TEXT_DARK),
        "ProjectItem": ParagraphStyle("ProjectItem", fontName="Helvetica", fontSize=8.2, leading=10.5, textColor=TEXT_DARK, leftIndent=10, firstLineIndent=-10, spaceAfter=2)
    }

def hr():
    return HRFlowable(width="100%", thickness=0.8, color=PRIMARY, spaceBefore=2, spaceAfter=3)


def build_pdf_es(filename="CV_Ruben_Barrios_Analista_De_Datos.pdf"):
    margin = 36
    doc = SimpleDocTemplate(
        filename, pagesize=letter, leftMargin=margin, rightMargin=margin, topMargin=34, bottomMargin=30,
        title="CV - Rubén David Barrios Bello - Data Analyst & BI",
        author="Rubén David Barrios Bello",
        subject="Curriculum Vitae - Data Analyst & Business Intelligence",
        keywords="Data Analyst, Business Intelligence, Power BI, SQL, Python, DAX, GTM, GA4, Looker Studio, PostgreSQL, Fraud Prevention, E-Commerce, Logistics"
    )
    usable_width = 8.5 * inch - 2 * margin
    styles = get_styles()
    story = []

    # PÁGINA 1
    story.append(Paragraph("RUBÉN DAVID BARRIOS BELLO", styles["Name"]))
    story.append(Paragraph("Data Analyst | Business Intelligence & Fraud Prevention | Lic. en Banca y Finanzas", styles["Headline"]))
    story.append(Paragraph('Buenos Aires, Argentina &nbsp;|&nbsp; <a href="mailto:rubendavid1809@gmail.com" color="#2B6CB0">rubendavid1809@gmail.com</a> &nbsp;|&nbsp; Tel. +54 9 11 7025-9429', styles["Contact"]))
    story.append(Paragraph('LinkedIn: <a href="https://linkedin.com/in/ruben-barrios-1430712ab" color="#2B6CB0"><b>linkedin.com/in/ruben-barrios-1430712ab</b></a> &nbsp;|&nbsp; GitHub: <a href="https://github.com/rubenbarrios-bigdata" color="#2B6CB0"><b>github.com/rubenbarrios-bigdata</b></a> &nbsp;|&nbsp; CV Digital: <a href="https://rubenbarrios-bigdata.github.io/cv-ejecutivo-inteligente/" color="#2B6CB0"><b>cv-ejecutivo-inteligente</b></a>', styles["Links"]))

    story.append(Paragraph("RESUMEN PROFESIONAL", styles["SectionTitle"]))
    story.append(hr())
    story.append(Paragraph("<b>Analista de Datos</b> con experiencia demostrada en análisis de métricas de fraude, logística y e-commerce, y más de 15 años de sólida trayectoria previa en el sector bancario y financiero internacional. Especializado en transformar requerimientos de negocio en soluciones analíticas de alto impacto mediante el diseño de dashboards en <b>Power BI (DAX)</b>, consultas avanzadas en <b>SQL (MySQL, PostgreSQL)</b>, automatización con <b>Python (pandas)</b> y analítica digital de productos con <b>GTM, GA4, Supabase y Looker Studio</b>.", styles["Body"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Historial comprobado en optimización de indicadores de negocio, destacando la <b>reducción del 80% en el ratio histórico de siniestralidad por fraude (de 0,150% a 0,030%)</b> en operaciones de alto volumen mediante sistemas de monitoreo en tiempo real. Perfil analítico orientado a la toma de decisiones basada en evidencia, conciliaciones complejas y trabajo multidisciplinario con equipos de Producto, Backend y Operaciones.", styles["Body"]))
    story.append(Spacer(1, 2))

    story.append(Paragraph("HABILIDADES TÉCNICAS", styles["SectionTitle"]))
    story.append(hr())
    skills_data = [
        [Paragraph("<b>Análisis de Datos y BI:</b>", styles["SkillCategory"]), Paragraph("Power BI (DAX avanzado, Power Query, modelado dimensional, PBIP), SQL (MySQL, PostgreSQL: queries complejas, subconsultas, agregaciones), Python (pandas, NumPy, Matplotlib, Colab, VSCode), Excel avanzado (tablas dinámicas, fórmulas complejas).", styles["SkillText"])],
        [Paragraph("<b>Visualización y Producto:</b>", styles["SkillCategory"]), Paragraph("Looker Studio, Google Analytics 4 (GA4), Google Tag Manager (GTM), Supabase, Firebase, BigQuery, diseño de KPIs ejecutivos, análisis de retención, engagement, funnel y conversión.", styles["SkillText"])],
        [Paragraph("<b>Negocio y Metodologías:</b>", styles["SkillCategory"]), Paragraph("Prevención de Fraudes, Detección de Anomalías en Logística/E-Commerce, Finanzas, Comercio Exterior, Git/GitHub, CI/CD para BI, Scrum/Ágil, IA Generativa aplicada (ChatGPT, Copilot, Gemini, Claude, Make).", styles["SkillText"])],
        [Paragraph("<b>Idiomas:</b>", styles["SkillCategory"]), Paragraph("Español (Nativo) &nbsp;|&nbsp; Inglés (Técnico / Lectura y comprensión profesional).", styles["SkillText"])]
    ]
    skills_table = Table(skills_data, colWidths=[130, usable_width - 130])
    skills_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 1), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(skills_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("EXPERIENCIA LABORAL", styles["SectionTitle"]))
    story.append(hr())

    # Puesto 1: Innova Lab
    t_p1 = Table([[Paragraph("Innova Lab — Proyecto Mate-Mático | Buenos Aires, Argentina", styles["JobTitleLeft"]), Paragraph("Jul. 2026 – Presente", styles["JobDateRight"])]], colWidths=[usable_width - 110, 110])
    t_p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p1)
    story.append(Paragraph("Data Analyst & Digital Analytics Specialist (Proyecto MVP)", styles["JobRole"]))
    story.append(Paragraph("• <b>Liderazgo en arquitectura de datos y analítica digital:</b> Diseño e implementación de la infraestructura de medición de producto desde cero para la aplicación educativa Mate-Mático.", styles["Bullet"]))
    story.append(Paragraph("• <b>Modelado de datos en base de datos:</b> Estructuración y consulta de tablas en <b>Supabase (PostgreSQL)</b> y Firebase para captura de eventos transaccionales y métricas de comportamiento de usuarios.", styles["Bullet"]))
    story.append(Paragraph("• <b>Tracking avanzado de eventos:</b> Configuración integral de tags, triggers y variables con <b>Google Tag Manager (GTM)</b> y <b>Google Analytics 4 (GA4)</b>, validando el correcto flujo de datos junto a Backend y QA.", styles["Bullet"]))
    story.append(Paragraph("• <b>Visualización ejecutiva de producto:</b> Creación de dashboard analítico en <b>Looker Studio</b> embebido en la aplicación, monitoreando KPIs de uso, retención, progresión académica y conversión.", styles["Bullet"]))
    story.append(Spacer(1, 2))

    # Puesto 2: Webpack
    t_p2 = Table([[Paragraph("Webpack S.R.L — Logística Mercado Libre | Buenos Aires, Argentina", styles["JobTitleLeft"]), Paragraph("Mar. 2020 – Oct. 2024", styles["JobDateRight"])]], colWidths=[usable_width - 110, 110])
    t_p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p2)
    story.append(Paragraph("Data Analyst — Prevención de Fraudes y Siniestros E-Commerce", styles["JobRole"]))
    story.append(Paragraph("• <b>Logro Destacado de Negocio:</b> Reducción histórica del <b>80% en el ratio de siniestros por fraude (de 0,150% a 0,030%)</b>, posicionando a Webpack como la operación logística con el ratio más bajo y eficiente de toda la red de Mercado Libre.", styles["Achievement"]))
    story.append(Paragraph("• <b>Monitoreo y tableros de control en tiempo real:</b> Diseño, automatización y mantenimiento de dashboards interactivos en <b>Power BI (DAX)</b> y modelos en Excel avanzado para supervisión de siniestros y reclamos de alta volumetría.", styles["Bullet"]))
    story.append(Paragraph("• <b>Detección de patrones anómalos y análisis SQL:</b> Extracción y limpieza de datos operativos con consultas analíticas en SQL y reporting automatizado para identificar desvíos sistemáticos y mitigar pérdidas financieras.", styles["Bullet"]))
    story.append(Paragraph("• <b>Optimización de procesos operativos:</b> Articulación y coordinación con despachos, operaciones y seguridad patrimonial, estableciendo protocolos de alerta temprana basados en evidencia analítica.", styles["Bullet"]))

    story.append(PageBreak())

    # PÁGINA 2
    story.append(Paragraph("EXPERIENCIA LABORAL (CONTINUACIÓN)", styles["SectionTitle"]))
    story.append(hr())
    t_p3 = Table([[Paragraph("Sector Bancario y Finanzas Internacionales | Caracas, Venezuela", styles["JobTitleLeft"]), Paragraph("2002 – 2017", styles["JobDateRight"])]], colWidths=[usable_width - 110, 110])
    t_p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p3)
    story.append(Paragraph("Especialista de Comercio Exterior / Analista Financiero y Operaciones — BFC Banco Fondo Común, Banco Exterior, Banco Venezolano de Crédito", styles["JobRole"]))
    story.append(Paragraph("• <b>Gestión y análisis de operaciones financieras:</b> Más de 15 años administrando operaciones de comercio exterior, cartas de crédito, cobranzas documentarias y divisas con estricta trazabilidad de fondos.", styles["Bullet"]))
    story.append(Paragraph("• <b>Control analítico y conciliaciones contables:</b> Supervisión de auxiliares contables, conciliaciones bancarias complejas y auditoría de datos financieros bajo riguroso cumplimiento normativo y regulatorio.", styles["Bullet"]))
    story.append(Paragraph("• <b>Riesgo y optimización operativa:</b> Control de riesgos operacionales y cambiarios, elaboración de reportes cuantitativos para comités ejecutivos y auditoría interna.", styles["Bullet"]))
    story.append(Spacer(1, 3))

    story.append(Paragraph("PROYECTOS DESTACADOS DE ANÁLISIS DE DATOS", styles["SectionTitle"]))
    story.append(hr())
    projects = [
        ("<b>Mate-Mático – Analítica Digital & Producto (Innova Lab):</b>", "Implementación integral de tracking con GTM y GA4, persistencia de eventos en Supabase (PostgreSQL) y dashboard en Looker Studio para optimización del embudo de retención y engagement. " + '<a href="https://github.com/rubenbarrios-bigdata/Analitica-Digital-Mate-matico" color="#2B6CB0"><b>[Ver en GitHub]</b></a>'),
        ("<b>Dashboard Atención al Cliente (Power BI + DAX):</b>", "Tablero interactivo para optimización de operaciones de servicio al cliente: seguimiento de volumen de tickets, tiempos de primera respuesta, SLA de resolución y métricas operativas con medidas y cálculos en DAX. " + '<a href="https://github.com/rubenbarrios-bigdata/dashboard-atencion-al-cliente" color="#2B6CB0"><b>[Ver en GitHub]</b></a>'),
        ("<b>Dashboard Reporte de RRHH (Power BI + DAX):</b>", "Análisis integral de headcount, métricas de rotación voluntaria/involuntaria (turnover), distribución demográfica y evolución de desempeño del personal para la toma de decisiones estratégicas de People Analytics. " + '<a href="https://github.com/rubenbarrios-bigdata/dashboard-rrhh" color="#2B6CB0"><b>[Ver en GitHub]</b></a>'),
        ("<b>Proyecto SQL Orders & E-Commerce Analysis:</b>", "Análisis exploratorio y transaccional sobre datasets de ventas reales en MySQL empleando subqueries, agrupaciones y funciones de agregación para evaluación de métricas comerciales y márgenes de rentabilidad. " + '<a href="https://github.com/rubenbarrios-bigdata/proyecto-sql-orders" color="#2B6CB0"><b>[Ver en GitHub]</b></a>'),
        ("<b>Análisis Exploratorio de Datos (EDA) en Python:</b>", "Limpieza de datos, manejo de valores atípicos y análisis estadístico multivariado con pandas, NumPy y visualizaciones con Matplotlib/Seaborn sobre datasets a escala. " + '<a href="https://github.com/rubenbarrios-bigdata" color="#2B6CB0"><b>[Ver Repositorio]</b></a>')
    ]
    for p_title, p_desc in projects:
        story.append(Paragraph(f"• {p_title} {p_desc}", styles["ProjectItem"]))
    story.append(Paragraph('<i>Todos los proyectos, modelos de datos y documentación técnica disponibles en: <a href="https://github.com/rubenbarrios-bigdata" color="#2B6CB0"><b>github.com/rubenbarrios-bigdata</b></a></i>', styles["Body"]))
    story.append(Spacer(1, 3))

    story.append(Paragraph("EDUCACIÓN", styles["SectionTitle"]))
    story.append(hr())
    edu = [
        ("Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial", "En curso (Primer Año) — Instituto de Formación Técnica Superior | Ministerio de Educación GCBA"),
        ("Business Intelligence (BI Consulting)", "En curso (Segundo cuatrimestre de tres, ruta formativa oficial hacia Análisis de Datos) — Talento Tech | Ministerio de Educación GCBA"),
        ("Power BI DevOps: PBIP, Git, CI/CD y Microsoft Fabric", "En curso — Udemy"),
        ("Licenciatura en Administración de Recursos Materiales y Financieros", "Universidad Nacional Experimental Simón Rodríguez | Caracas, Venezuela"),
        ("T.S.U. en Administración de Recursos Físicos y Financieros", "Colegio Universitario Fermín Toro | Caracas, Venezuela")
    ]
    for deg, inst in edu:
        story.append(Paragraph(f"• <b>{deg}</b> — {inst}", styles["Bullet"]))
    story.append(Spacer(1, 3))

    story.append(Paragraph("CERTIFICADOS EXTRACURRICULARES", styles["SectionTitle"]))
    story.append(hr())
    certs = [
        ("Analítica Digital: Google Tag Manager, Google Analytics 4 y Data Studio", "Analytics Way"),
        ("Análisis de Datos: Excel, Power BI, SQL y Python", "Datax"),
        ("Fundamentos de Inteligencia Artificial (Artificial Intelligence Fundamentals)", "IBM SkillsBuild"),
        ("Iniciación a la Programación con Python", "Talento Tech — Ministerio de Educación GCBA"),
        ("IA Aplicada al Entorno Laboral: ChatGPT, Gemini, Copilot, Make", "IA Leaders")
    ]
    for c_name, c_inst in certs:
        story.append(Paragraph(f"• <b>{c_name}</b> &nbsp;|&nbsp; <i>{c_inst}</i>", styles["Bullet"]))

    doc.build(story, canvasmaker=ATSNumberedCanvasES)
    print(f"PDF Español generado: {filename}")


def build_pdf_en(filename="CV_Ruben_Barrios_Data_Analyst.pdf"):
    margin = 36
    doc = SimpleDocTemplate(
        filename, pagesize=letter, leftMargin=margin, rightMargin=margin, topMargin=34, bottomMargin=30,
        title="CV - Rubén David Barrios Bello - Data Analyst & BI",
        author="Rubén David Barrios Bello",
        subject="Curriculum Vitae - Data Analyst & Business Intelligence",
        keywords="Data Analyst, Business Intelligence, Power BI, SQL, Python, DAX, GTM, GA4, Looker Studio, PostgreSQL, Fraud Prevention, E-Commerce, Logistics"
    )
    usable_width = 8.5 * inch - 2 * margin
    styles = get_styles()
    story = []

    # PAGE 1
    story.append(Paragraph("RUBÉN DAVID BARRIOS BELLO", styles["Name"]))
    story.append(Paragraph("Data Analyst | Business Intelligence & Fraud Prevention | B.A. in Banking & Finance", styles["Headline"]))
    story.append(Paragraph('Buenos Aires, Argentina &nbsp;|&nbsp; <a href="mailto:rubendavid1809@gmail.com" color="#2B6CB0">rubendavid1809@gmail.com</a> &nbsp;|&nbsp; Phone: +54 9 11 7025-9429', styles["Contact"]))
    story.append(Paragraph('LinkedIn: <a href="https://linkedin.com/in/ruben-barrios-1430712ab" color="#2B6CB0"><b>linkedin.com/in/ruben-barrios-1430712ab</b></a> &nbsp;|&nbsp; GitHub: <a href="https://github.com/rubenbarrios-bigdata" color="#2B6CB0"><b>github.com/rubenbarrios-bigdata</b></a> &nbsp;|&nbsp; Digital CV: <a href="https://rubenbarrios-bigdata.github.io/cv-ejecutivo-inteligente/" color="#2B6CB0"><b>cv-ejecutivo-inteligente</b></a>', styles["Links"]))

    story.append(Paragraph("PROFESSIONAL SUMMARY", styles["SectionTitle"]))
    story.append(hr())
    story.append(Paragraph("<b>Data Analyst</b> with demonstrated experience analyzing fraud metrics, logistics, and e-commerce operations, backed by over 15 years of solid prior experience in the international banking and financial sector. Specialized in transforming business requirements into high-impact analytical solutions through <b>Power BI dashboards (DAX)</b>, advanced <b>SQL queries (MySQL, PostgreSQL)</b>, data automation with <b>Python (pandas)</b>, and digital product analytics with <b>GTM, GA4, Supabase, and Looker Studio</b>.", styles["Body"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Proven track record of business metric optimization, highlighted by an <b>80% historical reduction in the fraud loss ratio (from 0.150% to 0.030%)</b> across high-volume logistics operations via real-time monitoring systems. Analytical mindset oriented towards evidence-based decision-making, complex reconciliations, and cross-functional collaboration with Product, Backend, and Operations teams.", styles["Body"]))
    story.append(Spacer(1, 2))

    story.append(Paragraph("TECHNICAL SKILLS", styles["SectionTitle"]))
    story.append(hr())
    skills_data = [
        [Paragraph("<b>Data Analytics & BI:</b>", styles["SkillCategory"]), Paragraph("Power BI (Advanced DAX, Power Query, dimensional modeling, PBIP), SQL (MySQL, PostgreSQL: complex queries, subqueries, aggregations), Python (pandas, NumPy, Matplotlib, Colab, VSCode), Advanced Excel (pivot tables, complex formulas).", styles["SkillText"])],
        [Paragraph("<b>Visualization & Product:</b>", styles["SkillCategory"]), Paragraph("Looker Studio, Google Analytics 4 (GA4), Google Tag Manager (GTM), Supabase, Firebase, BigQuery, executive KPI design, user retention, engagement, funnel and conversion tracking.", styles["SkillText"])],
        [Paragraph("<b>Business & Methodologies:</b>", styles["SkillCategory"]), Paragraph("Fraud Prevention, Anomaly Detection in Logistics/E-Commerce, Finance, International Trade, Git/GitHub, CI/CD for BI, Agile/Scrum, Generative AI (ChatGPT, Copilot, Gemini, Claude, Make).", styles["SkillText"])],
        [Paragraph("<b>Languages:</b>", styles["SkillCategory"]), Paragraph("Spanish (Native) &nbsp;|&nbsp; English (Technical / Professional reading & comprehension).", styles["SkillText"])]
    ]
    skills_table = Table(skills_data, colWidths=[130, usable_width - 130])
    skills_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 1), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(skills_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["SectionTitle"]))
    story.append(hr())

    # Position 1
    t_p1 = Table([[Paragraph("Innova Lab — Mate-Mático Project | Buenos Aires, Argentina", styles["JobTitleLeft"]), Paragraph("Jul. 2026 – Present", styles["JobDateRight"])]], colWidths=[usable_width - 110, 110])
    t_p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p1)
    story.append(Paragraph("Data Analyst & Digital Analytics Specialist (MVP Project)", styles["JobRole"]))
    story.append(Paragraph("• <b>End-to-End Data & Analytics Architecture:</b> Designed and deployed product analytics and event-tracking infrastructure from scratch for the Mate-Mático educational platform.", styles["Bullet"]))
    story.append(Paragraph("• <b>Database Modeling & Querying:</b> Structured and queried relational schemas in <b>Supabase (PostgreSQL)</b> and Firebase to track transactional events and user behavior metrics.", styles["Bullet"]))
    story.append(Paragraph("• <b>Advanced Event Tracking:</b> Configured and validated tracking tags, triggers, and custom parameters using <b>Google Tag Manager (GTM)</b> and <b>Google Analytics 4 (GA4)</b> in close alignment with Backend and QA teams.", styles["Bullet"]))
    story.append(Paragraph("• <b>Product Executive Dashboards:</b> Built real-time interactive dashboards in <b>Looker Studio</b> embedded inside the application, monitoring user retention, academic progression, and conversion KPIs.", styles["Bullet"]))
    story.append(Spacer(1, 2))

    # Position 2
    t_p2 = Table([[Paragraph("Webpack S.R.L — Mercado Libre Logistics | Buenos Aires, Argentina", styles["JobTitleLeft"]), Paragraph("Mar. 2020 – Oct. 2024", styles["JobDateRight"])]], colWidths=[usable_width - 110, 110])
    t_p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p2)
    story.append(Paragraph("Data Analyst — E-Commerce Fraud Prevention & Claims", styles["JobRole"]))
    story.append(Paragraph("• <b>Key Business Impact:</b> Achieved a historic <b>80% reduction in the fraud loss ratio (from 0.150% to 0.030%)</b>, establishing Webpack as the benchmark logistics operator across Mercado Libre's entire network.", styles["Achievement"]))
    story.append(Paragraph("• <b>Real-Time Monitoring Dashboards:</b> Designed, automated, and maintained interactive dashboards in <b>Power BI (DAX)</b> and advanced Excel models for continuous supervision of high-volume package incidents.", styles["Bullet"]))
    story.append(Paragraph("• <b>Anomaly Detection & SQL Analysis:</b> Queried, transformed, and cleaned operational transaction data using SQL and automated reporting to identify systemic fraud patterns and mitigate direct financial losses.", styles["Bullet"]))
    story.append(Paragraph("• <b>Operational Process Optimization:</b> Coordinated with dispatch, warehouse, and asset protection teams to establish early-warning response protocols driven by data evidence.", styles["Bullet"]))

    story.append(PageBreak())

    # PAGE 2
    story.append(Paragraph("PROFESSIONAL EXPERIENCE (CONTINUED)", styles["SectionTitle"]))
    story.append(hr())
    t_p3 = Table([[Paragraph("Banking Sector & International Finance | Caracas, Venezuela", styles["JobTitleLeft"]), Paragraph("2002 – 2017", styles["JobDateRight"])]], colWidths=[usable_width - 110, 110])
    t_p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p3)
    story.append(Paragraph("Foreign Trade Specialist / Financial & Operations Analyst — BFC Banco Fondo Común, Banco Exterior, Banco Venezolano de Crédito", styles["JobRole"]))
    story.append(Paragraph("• <b>Financial Operations & Analysis:</b> Over 15 years managing foreign trade transactions, letters of credit, documentary collections, and foreign exchange under strict funds traceability.", styles["Bullet"]))
    story.append(Paragraph("• <b>Analytical Auditing & Reconciliations:</b> Supervised general ledgers, handled complex multi-currency bank reconciliations, and audited financial data under strict regulatory compliance frameworks.", styles["Bullet"]))
    story.append(Paragraph("• <b>Risk Management & Operational Optimization:</b> Mitigated currency and operational risk, producing quantitative reports for executive committees and external audit reviews.", styles["Bullet"]))
    story.append(Spacer(1, 3))

    story.append(Paragraph("KEY DATA ANALYTICS PROJECTS", styles["SectionTitle"]))
    story.append(hr())
    projects_en = [
        ("<b>Mate-Mático – Digital Analytics & Product (Innova Lab):</b>", "Comprehensive event tracking with GTM & GA4, transactional event persistence in Supabase (PostgreSQL), and Looker Studio dashboard for funnel and retention optimization. " + '<a href="https://github.com/rubenbarrios-bigdata/Analitica-Digital-Mate-matico" color="#2B6CB0"><b>[View on GitHub]</b></a>'),
        ("<b>Customer Service Dashboard (Power BI + DAX):</b>", "Interactive dashboard optimizing customer support operations: tracking ticket volume, first-response time, resolution SLA, and service metrics with custom DAX measures. " + '<a href="https://github.com/rubenbarrios-bigdata/dashboard-atencion-al-cliente" color="#2B6CB0"><b>[View on GitHub]</b></a>'),
        ("<b>HR Analytics Dashboard (Power BI + DAX):</b>", "Workforce analytics covering headcount trends, voluntary/involuntary turnover, demographic distribution, and performance evolution for strategic People Analytics decisions. " + '<a href="https://github.com/rubenbarrios-bigdata/dashboard-rrhh" color="#2B6CB0"><b>[View on GitHub]</b></a>'),
        ("<b>SQL Orders & E-Commerce Analysis:</b>", "Exploratory and transactional analysis over real sales datasets in MySQL using subqueries, groupings, and aggregation functions to evaluate sales KPIs and profitability margins. " + '<a href="https://github.com/rubenbarrios-bigdata/proyecto-sql-orders" color="#2B6CB0"><b>[View on GitHub]</b></a>'),
        ("<b>Exploratory Data Analysis (EDA) in Python:</b>", "Data cleaning, outlier treatment, and multivariate statistical analysis using pandas, NumPy, and Matplotlib/Seaborn visualizations over datasets at scale. " + '<a href="https://github.com/rubenbarrios-bigdata" color="#2B6CB0"><b>[View Repository]</b></a>')
    ]
    for p_title, p_desc in projects_en:
        story.append(Paragraph(f"• {p_title} {p_desc}", styles["ProjectItem"]))
    story.append(Paragraph('<i>All projects, data models, and technical documentation available at: <a href="https://github.com/rubenbarrios-bigdata" color="#2B6CB0"><b>github.com/rubenbarrios-bigdata</b></a></i>', styles["Body"]))
    story.append(Spacer(1, 3))

    story.append(Paragraph("EDUCATION", styles["SectionTitle"]))
    story.append(hr())
    edu_en = [
        ("Associate Degree in Data Science & Artificial Intelligence", "In Progress (1st Year) — Higher Technical Training Institute | Ministry of Education, City of Buenos Aires (GCBA)"),
        ("Business Intelligence (BI Consulting)", "In Progress (2nd of 3 terms, official learning path toward Data Analytics) — Talento Tech | Ministry of Education, City of Buenos Aires (GCBA)"),
        ("Power BI DevOps: PBIP, Git, CI/CD, and Microsoft Fabric", "In Progress — Udemy"),
        ("Bachelor's Degree (Lic.) in Material & Financial Resources Administration", "Simón Rodríguez National Experimental University | Caracas, Venezuela"),
        ("Associate Degree (T.S.U.) in Physical & Financial Resources Administration", "Fermín Toro University College | Caracas, Venezuela")
    ]
    for deg, inst in edu_en:
        story.append(Paragraph(f"• <b>{deg}</b> — {inst}", styles["Bullet"]))
    story.append(Spacer(1, 3))

    story.append(Paragraph("EXTRACURRICULAR CERTIFICATES", styles["SectionTitle"]))
    story.append(hr())
    certs_en = [
        ("Digital Analytics: Google Tag Manager, Google Analytics 4, and Data Studio", "Analytics Way"),
        ("Data Analysis: Excel, Power BI, SQL, and Python", "Datax"),
        ("Artificial Intelligence Fundamentals", "IBM SkillsBuild"),
        ("Introduction to Programming with Python", "Talento Tech — Ministry of Education, City of Buenos Aires (GCBA)"),
        ("Applied AI in the Workplace: ChatGPT, Gemini, Copilot, Make", "IA Leaders")
    ]
    for c_name, c_inst in certs_en:
        story.append(Paragraph(f"• <b>{c_name}</b> &nbsp;|&nbsp; <i>{c_inst}</i>", styles["Bullet"]))

    doc.build(story, canvasmaker=ATSNumberedCanvasEN)
    print(f"PDF Inglés generado: {filename}")


if __name__ == "__main__":
    build_pdf_es("CV_Ruben_Barrios_Analista_De_Datos.pdf")
    build_pdf_en("CV_Ruben_Barrios_Data_Analyst.pdf")
