# -*- coding: utf-8 -*-
"""
Generador de Documento PDF Ejecutivo: Plan Estratégico y Arquitectura de Evolución
"Personal Career Intelligence" - Rubén David Barrios Bello
Estructurado rigurosamente en 2 Macro-Fases y 4 Páginas ejecutivas de alta densidad y balance visual.
"""

import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Canvas de dos pasadas para calcular y mostrar 'Página X de Y' y encabezados elegantes."""
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#475569"))

        # Header elegante en todas las páginas salvo la portada
        if self._pageNumber > 1:
            self.drawString(48, 11 * inch - 36, "CV EJECUTIVO INTELIGENTE | PLAN ESTRATÉGICO & ARQUITECTURA")
            self.drawRightString(8.5 * inch - 48, 11 * inch - 36, "RUBÉN DAVID BARRIOS BELLO")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(48, 11 * inch - 42, 8.5 * inch - 48, 11 * inch - 42)

        # Footer elegante en todas las páginas
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(48, 42, 8.5 * inch - 48, 42)
        self.setFont("Helvetica", 8)
        self.drawString(48, 30, "Documento de Planificación y Arquitectura Técnica • Confidencial & Portafolio Profesional")
        page_text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(8.5 * inch - 48, 30, page_text)

        self.restoreState()


def build_pdf(filename="Plan_Estrategico_CV_Ejecutivo_Inteligente_Ruben_Barrios.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=48,
        rightMargin=48,
        topMargin=46,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()

    # Paleta cromática ejecutiva
    C_PRIMARY = colors.HexColor("#0F172A")    # Slate 900
    C_SECONDARY = colors.HexColor("#1E3A8A")  # Blue 900
    C_ACCENT = colors.HexColor("#0284C7")     # Sky 600
    C_TEXT = colors.HexColor("#334155")       # Slate 700
    C_MUTED = colors.HexColor("#64748B")      # Slate 500
    C_BG_LIGHT = colors.HexColor("#F8FAFC")   # Slate 50
    C_BORDER = colors.HexColor("#CBD5E1")     # Slate 300
    C_SUCCESS = colors.HexColor("#059669")    # Emerald 600

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=21,
        leading=25,
        textColor=C_PRIMARY,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=C_ACCENT,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=C_PRIMARY,
        spaceBefore=8,
        spaceAfter=5,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=C_SECONDARY,
        spaceBefore=6,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.2,
        textColor=C_TEXT,
        spaceAfter=4
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=C_PRIMARY
    )

    meta_label = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=C_MUTED
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_PRIMARY
    )

    story = []

    # =========================================================================
    # PÁGINA 1: PORTADA, RESUMEN EJECUTIVO Y ARQUITECTURA EN DOS MACRO-FASES
    # =========================================================================
    story.append(Paragraph("DATA-DRIVEN EXECUTIVE DASHBOARD & AI CAREER HUB", subtitle_style))
    story.append(Paragraph("CV Ejecutivo Inteligente", title_style))
    story.append(Paragraph("Plan Estratégico y Arquitectura Técnica: Estructuración en Dos Macro-Fases", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_ACCENT, spaceBefore=2, spaceAfter=8))

    meta_data = [
        [Paragraph("<b>Proyecto:</b>", meta_label), Paragraph("CV Ejecutivo Inteligente", meta_val),
         Paragraph("<b>Fecha:</b>", meta_label), Paragraph("Septiembre 2026", meta_val)],
        [Paragraph("<b>Autor:</b>", meta_label), Paragraph("Rubén David Barrios Bello", meta_val),
         Paragraph("<b>Estado:</b>", meta_label), Paragraph("Fase 1 Operativa (v1.0.0)", meta_val)],
        [Paragraph("<b>Repositorio:</b>", meta_label), Paragraph("rubenbarrios-bigdata/cv-ejecutivo-inteligente", meta_val),
         Paragraph("<b>Enfoque:</b>", meta_label), Paragraph("2 Fases: Diseño CV + Inteligencia & Analytics", meta_val)]
    ]
    t_meta = Table(meta_data, colWidths=[1.0*inch, 2.7*inch, 0.9*inch, 2.6*inch])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.75, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Visión y Fundamento Estratégico", h1_style))
    story.append(Paragraph(
        "El proyecto <b>CV Ejecutivo Inteligente</b> replantea el concepto de currículum tradicional. "
        "En lugar de ser un documento estático, evoluciona hacia un <b>producto de datos interactivo y vivo</b>, "
        "donde la propia plataforma sirve como prueba empírica e irrefutable de las competencias del candidato en "
        "maquetación web, analítica digital de comportamiento, ingeniería de datos en la nube e inteligencia artificial.",
        body_style
    ))
    story.append(Paragraph(
        "El proyecto se estructura de forma deliberada en <b>dos macro-fases</b> independientes pero complementarias: "
        "la <b>Fase 1</b>, centrada en el diseño visual, experiencia de usuario y consolidación legal de la obra; y la "
        "<b>Fase 2</b>, centrada en la evolución tecnológica integral (desde la organización y analítica digital, hasta "
        "el pipeline en BigQuery, el dashboard de métricas en Looker Studio y el agente interactivo con Gemini).",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("2. Comparativa y Módulos de las Dos Macro-Fases", h1_style))

    phase_overview = [
        [Paragraph("<b>MACRO-FASE 1: DISEÑO Y CONSOLIDACIÓN DEL CV (V1.0)</b>", meta_val),
         Paragraph("<b>MACRO-FASE 2: ANALYTICS, BIGQUERY E IA (V2.0 - V3.0)</b>", meta_val)],
        [Paragraph(
            "<b>Propósito:</b> Establecer la base visual, UX y presentación profesional del perfil.<br/>"
            "• <b>Enfoque Dashboard:</b> Banner de 4 KPIs estratégicos cuantificables.<br/>"
            "• <b>Arquitectura Desacoplada:</b> Capa de datos (<code>data.json</code>) vs. Vista.<br/>"
            "• <b>UX & Accesibilidad:</b> Modo Oscuro/Claro persistente y diseño Responsive.<br/>"
            "• <b>Explorador de Certificaciones:</b> Filtrado interactivo por especialidad.<br/>"
            "• <b>Resguardo Jurídico:</b> Registro de autoría de página web en <b>DNDA (TAD)</b>.",
            body_style
         ),
         Paragraph(
            "<b>Propósito:</b> Dotar a la plataforma de telemetría de negocio e inteligencia activa.<br/>"
            "• <b>Paso 0 (Organización):</b> Roadmap público y arquitectura en GitHub.<br/>"
            "• <b>Paso 1 (Analytics):</b> DataLayer nativo + Google Tag Manager + GA4.<br/>"
            "• <b>Paso 2 (Data Pipeline):</b> Streaming a BigQuery (SQL) + Looker Studio.<br/>"
            "• <b>Paso 3 (Agente IA):</b> Asistente <i>Ask Rubén AI</i> con Gemini + Deep Linking.<br/>"
            "• <b>Extensiones Futuras:</b> Motor de Job Matching ATS y Career Brief.",
            body_style
         )]
    ]
    t_phase = Table(phase_overview, colWidths=[3.6*inch, 3.6*inch])
    t_phase.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#E0F2FE")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#EDE9FE")),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor("#F8FAFC")),
        ('BACKGROUND', (1,1), (1,1), colors.HexColor("#FDF4FF")),
        ('BOX', (0,0), (-1,-1), 0.75, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_phase)

    # =========================================================================
    # PÁGINA 2: FASE 1 EN PROFUNDIDAD (DISEÑO, ARQUITECTURA Y DNDA)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("3. Macro-Fase 1: Diseño, Experiencia Visual y Consolidación (V1.0)", h1_style))
    story.append(Paragraph(
        "La Fase 1 materializa el CV como un producto web autosuficiente, altamente optimizado para lectura ejecutiva "
        "rápida. Su objetivo principal es captar la atención de reclutadores y líderes técnicos mediante métricas "
        "cuantificables y una experiencia visual de primer nivel.",
        body_style
    ))

    story.append(Paragraph("3.1. Arquitectura de Información y Filosofía de Diseño", h2_style))
    story.append(Paragraph(
        "• <b>Mentalidad de Executive Dashboard:</b> Se eliminan párrafos densos al inicio. El encabezado destaca "
        "<b>4 KPIs Clave</b> que resumen más de 16 años de trayectoria: <i>+4 Años en Prevención de Fraude E-Commerce</i>, "
        "<i>Descenso del 80% en Ratio de Fraude (de 0,150 a 0,030)</i>, <i>+15 Años en Sector Bancario y Finanzas</i>, "
        "y <i>9 Proyectos de Analítica aplicados</i> (Power BI, DAX, SQL, Python).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Separación de Capas (Data Layer vs. Presentation):</b> Se diseñó un esquema desacoplado donde la fuente "
        "de verdad radica en <code>data.json</code> y <code>data_en.json</code>. El frontend HTML/JS consume esta "
        "estructura mediante <code>fetch API</code> asíncrona, incorporando un fallback pre-renderizado automático "
        "para garantizar visualización impecable offline o ante bloqueos de CORS.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>UX y Diseño Responsivo:</b> Maquetación en CSS moderno con variables HSL, conmutador de Modo Oscuro / Claro "
        "persistente en <code>localStorage</code>, y adaptación ergonómica a pantallas móviles (<code>mobile.html</code>).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Centro Interactivo de Certificaciones:</b> Sistema dinámico de filtrado por pilares de especialidad "
        "(Data & BI, IA & ML, Programación, Trabajo Remoto) con accesos a credenciales verificadas (Credly, OpenBadge).",
        bullet_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("3.2. Estrategia Jurídica y Registro de Autoría (Argentina - DNDA / INPI)", h2_style))
    story.append(Paragraph(
        "Frente a la inquietud sobre plagio o copia de la obra, se aplica una estrategia legal pragmática y accesible. "
        "Las ideas abstractas no se patentan; lo que se protege y certifica es la <b>obra concreta, el código, el diseño "
        "y la estructura de presentación</b>:",
        body_style
    ))

    legal_rows = [
        [Paragraph("<b>Instancia / Organismo</b>", meta_label), Paragraph("<b>Objeto Protegido</b>", meta_label), Paragraph("<b>Arancel Oficial</b>", meta_label), Paragraph("<b>Estrategia y Entregables</b>", meta_label)],
        [Paragraph("<b>DNDA (TAD)</b><br/>Página Web Publicada", body_style),
         Paragraph("Diseño visual, estructura de navegación, contenido textual y CSS.", body_style),
         Paragraph("$2.000 ARS<br/>(Tasa económica oficial)", body_style),
         Paragraph("Compilación en PDF de capturas del sitio en GitHub Pages y memoria descriptiva.", body_style)],
        [Paragraph("<b>DNDA (TAD)</b><br/>Software Publicado", body_style),
         Paragraph("Código fuente HTML, JavaScript Vanilla, capa JSON y scripts Python.", body_style),
         Paragraph("~$3.800 ARS + tasa<br/>(Muy accesible)", body_style),
         Paragraph("Impresión a PDF del código fuente estructurado y declaración de autoría.", body_style)],
        [Paragraph("<b>GitHub Releases</b><br/>Timestamp Criptográfico", body_style),
         Paragraph("Trazabilidad histórica pública de commits, versiones y fechas ciertas.", body_style),
         Paragraph("Gratuito ($0 USD)", body_style),
         Paragraph("Crear tag oficial <code>v1.0.0</code> y documentar <code>CHANGELOG.md</code>.", body_style)],
        [Paragraph("<b>INPI</b><br/>Registro de Marca", body_style),
         Paragraph("Nombre comercial distintivo (ej. <i>CV Ejecutivo Inteligente</i>).", body_style),
         Paragraph("Arancel UMAPI mensual<br/>(Fase posterior)", body_style),
         Paragraph("Evaluar recién al consolidar la marca y lanzar el agente de IA en Fase 2.", body_style)]
    ]
    t_legal = Table(legal_rows, colWidths=[1.6*inch, 2.3*inch, 1.4*inch, 1.9*inch])
    t_legal.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.75, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_legal)

    # =========================================================================
    # PÁGINA 3: FASE 2 - PASOS 0, 1 Y 2 (ORGANIZACIÓN, ANALYTICS Y BIGQUERY)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("4. Macro-Fase 2: Infraestructura Analítica y Big Data (Pasos 0 al 2)", h1_style))
    story.append(Paragraph(
        "La Fase 2 transforma el CV en una plataforma de telemetría en tiempo real. Demuestra ante cualquier evaluador "
        "el dominio práctico del stack moderno de Digital Analytics y Data Warehousing en Google Cloud Platform.",
        body_style
    ))

    story.append(Paragraph("4.1. Paso 0: Organización, Arquitectura y Documentación Pública", h2_style))
    story.append(Paragraph(
        "• <b>Roadmap en el Repositorio:</b> Incorporación en el <code>README.md</code> de la sección <i>'Evolution of the Project'</i>, "
        "dejando constancia pública y cronológica del desarrollo modular.<br/>"
        "• <b>Diccionario de Datos del DataLayer:</b> Definición de la taxonomía formal de eventos para estandarizar nombres, "
        "tipos de datos y parámetros antes de tocar el código de producción.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("4.2. Paso 1: Digital Analytics Nativo (DataLayer + GTM + GA4)", h2_style))
    story.append(Paragraph(
        "Implementación de un sistema de telemetría que registra el comportamiento de navegación sin almacenar datos "
        "personales, demostrando buenas prácticas de medición y privacidad:",
        body_style
    ))

    events_data = [
        [Paragraph("<b>Evento Personalizado</b>", meta_label), Paragraph("<b>Trigger / Acción del Usuario</b>", meta_label), Paragraph("<b>Parámetros de Medición Asociados</b>", meta_label)],
        [Paragraph("<code>cv_scroll_depth</code>", body_style), Paragraph("Desplazamiento vertical en la pantalla", body_style), Paragraph("<code>depth_percentage</code>: 25%, 50%, 75%, 100%", body_style)],
        [Paragraph("<code>cv_kpi_interaction</code>", body_style), Paragraph("Clic en indicadores del banner superior", body_style), Paragraph("<code>kpi_name</code>, <code>kpi_value</code>, <code>target_anchor</code>", body_style)],
        [Paragraph("<code>cv_project_click</code>", body_style), Paragraph("Clic en enlaces o detalles de proyectos", body_style), Paragraph("<code>project_id</code>, <code>tech_stack</code> (PowerBI, SQL, Python)", body_style)],
        [Paragraph("<code>cv_cert_filter</code>", body_style), Paragraph("Uso de filtros en módulo de certificaciones", body_style), Paragraph("<code>category</code> (Data, IA, Programación, Remoto)", body_style)],
        [Paragraph("<code>cv_document_download</code>", body_style), Paragraph("Descarga del CV en versión PDF o DOCX", body_style), Paragraph("<code>file_format</code>, <code>language</code> (ES / EN)", body_style)],
        [Paragraph("<code>cv_theme_toggle</code>", body_style), Paragraph("Cambio de tema Dark / Light", body_style), Paragraph("<code>selected_theme</code>: dark | light", body_style)],
        [Paragraph("<code>cv_section_engagement</code>", body_style), Paragraph("Tiempo de permanencia real por sección", body_style), Paragraph("<code>section_id</code>, <code>time_seconds</code>", body_style)]
    ]
    t_events = Table(events_data, colWidths=[1.8*inch, 2.4*inch, 3.0*inch])
    t_events.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.75, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_events)

    story.append(Spacer(1, 4))
    story.append(Paragraph("4.3. Paso 2: Data Pipeline a BigQuery y Dashboard en Looker Studio", h2_style))
    story.append(Paragraph(
        "• <b>Exportación a BigQuery (Raw Events):</b> Configuración del streaming continuo y gratuito desde GA4 hacia Google "
        "Cloud BigQuery. Esto permite disponer de la tabla de eventos en crudo sin el muestreo que aplica la interfaz estándar.<br/>"
        "• <b>Transformación y Modelado en SQL:</b> Creación de queries y vistas programadas para desanidar registros anidados "
        "(<code>UNNEST(event_params)</code>), estructurar el embudo de conversión del reclutador y calcular tasas de interacción.<br/>"
        "• <b>Dashboard Ejecutivo en Looker Studio:</b> Creación de un panel de visualización conectado a BigQuery y enlazado "
        "desde el CV. Exhibe de forma anónima métricas reales de lectura: proyectos más consultados, países de origen, "
        "dispositivos y ratios de descarga de PDF. Es la prueba fehaciente de capacidad en Business Intelligence.",
        body_style
    ))

    # =========================================================================
    # PÁGINA 4: FASE 2 - PASO 3 (IA GEMINI), ROADMAP Y CONCLUSIONES
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("5. Macro-Fase 2: Inteligencia Artificial y Smart Navigator (Paso 3 y Extensiones)", h1_style))
    story.append(Paragraph(
        "El asistente de IA no es un chatbot genérico: opera como un <b>navegador inteligente del portafolio</b> y una "
        "herramienta de diagnóstico de adecuación laboral en tiempo real.",
        body_style
    ))

    story.append(Paragraph("5.1. Paso 3: Asistente 'Ask Rubén AI' con Gemini API", h2_style))
    story.append(Paragraph(
        "• <b>Arquitectura de Contexto (RAG Ligero):</b> Se inyecta la base de conocimiento estructurada de <code>data.json</code> "
        "y el historial profesional en el prompt del sistema de Gemini, respondiendo preguntas sobre la trayectoria con total fidelidad.<br/>"
        "• <b>Smart Navigation (Deep Linking a la UI):</b> Cuando el reclutador consulta <i>'¿Qué experiencia tiene en Power BI?'</i> "
        "o <i>'¿Cómo redujo el fraude?'</i>, la IA no solo responde verbalmente: emite una acción que ejecuta un auto-scroll fluido "
        "y resalta visualmente la tarjeta del proyecto o la métrica en la pantalla del usuario.<br/>"
        "• <b>Telemetría de Consultas (Market Demand Insights):</b> Las intenciones de búsqueda de los visitantes se categorizan "
        "y envían como evento anónimo al DataLayer. Esto permite saber en BigQuery qué habilidades consulta más el mercado laboral.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("5.2. Extensiones Futuras: Job Matching ATS y Career Brief", h2_style))
    story.append(Paragraph(
        "• <b>Calculadora de Match Laboral:</b> Módulo en la web donde un reclutador pega una vacante (<i>Job Description</i>); "
        "Gemini compara los requisitos con el perfil y genera un ATS Match Score, habilidades coincidentes y el <i>Skill Gap</i>.<br/>"
        "• <b>Agente Autónomo:</b> Script en Python que monitorea ofertas laborales y genera un reporte periódico de vacantes afines.",
        body_style
    ))

    # =========================================================================
    # PÁGINA 5: MACRO-FASE 3 (PLATAFORMA SAAS MULTIUSUARIO) Y ROADMAP GLOBAL
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("6. Macro-Fase 3: Plataforma SaaS Multiusuario — Cloud Platform", h1_style))
    story.append(Paragraph(
        "La culminación estratégica de la plataforma trasciende el portafolio individual y evoluciona hacia una <b>plataforma tecnológica "
        "multiusuario (Software as a Service - SaaS)</b> que permite a cualquier profesional o candidato transformar su currículum estático "
        "en un Executive Dashboard interactivo con telemetría en tiempo real y asistente de inteligencia artificial.",
        body_style
    ))

    story.append(Paragraph("6.1. Pilares de la Arquitectura SaaS Multiusuario", h2_style))
    story.append(Paragraph(
        "• <b>Ingestión y Parser Inteligente de CVs (AI Onboarding):</b> El usuario sube su CV en formato PDF o enlaza su perfil de LinkedIn; "
        "un motor multimodal con Google Gemini analiza la trayectoria, sintetiza los 4 KPIs clave de negocio y genera automáticamente el "
        "archivo estructurado de datos (<code>data.json</code>) sin necesidad de que el usuario programe código.<br/>"
        "• <b>Portal de Telemetría para el Postulante (Recruiter Insights):</b> Cada usuario dispone de un panel privado donde monitorea en tiempo "
        "real el impacto de sus postulaciones: empresas que abrieron su enlace, tiempo promedio de lectura, KPIs con más clics y descargas de PDF.<br/>"
        "• <b>Motor de Enlaces Dinámicos y Marca Blanca:</b> Asignación de URLs personalizadas (ej. <code>cv-inteligente.app/@usuario</code>) con soporte "
        "para dominios propios y exportación de versiones PDF optimizadas contra filtros ATS de selección.<br/>"
        "• <b>Growth Loop Viral Orgánico:</b> Cada CV generado incluye al pie la leyenda <i>'Desarrollado con CV Ejecutivo Inteligente'</i>, "
        "convirtiendo cada postulación enviada en un canal de adquisición natural de nuevos usuarios para la plataforma.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("6.2. Matriz Cronológica Integral de Ejecución (Macro-Fases 1, 2 y 3)", h1_style))

    roadmap_data = [
        [Paragraph("<b>Fase / Hito</b>", meta_label), Paragraph("<b>Alcance y Entregables Clave</b>", meta_label), Paragraph("<b>Tecnologías Involucradas</b>", meta_label), Paragraph("<b>Estado</b>", meta_label)],
        [Paragraph("<b>Fase 1: Consolidación V1</b><br/>Executive Dashboard", body_style),
         Paragraph("CV interactivo desktop/móvil, desacoplamiento data.json, autoría formal y dossier DNDA/TAD.", body_style),
         Paragraph("HTML5, CSS3, JS Vanilla, JSON, TAD DNDA, GitHub Pages", body_style),
         Paragraph("<font color='#059669'><b>Completado / Dossier Listo</b></font>", body_style)],
        [Paragraph("<b>Fase 2: Pasos 0 & 1</b><br/>Telemetría DataLayer", body_style),
         Paragraph("Inyección de window.dataLayer nativo en el CV insignia y configuración de triggers en GTM/GA4.", body_style),
         Paragraph("JavaScript (dataLayer.push), GTM Container, GA4 Admin", body_style),
         Paragraph("<font color='#0284C7'><b>Próximo Paso Inmediato</b></font>", body_style)],
        [Paragraph("<b>Fase 2: Paso 2</b><br/>BigQuery + Looker", body_style),
         Paragraph("Exportación de eventos a Google Cloud, vistas SQL analíticas y dashboard público embebido.", body_style),
         Paragraph("Google BigQuery, SQL (UNNEST), Looker Studio", body_style),
         Paragraph("<b>Planificado</b>", body_style)],
        [Paragraph("<b>Fase 2: Paso 3</b><br/>Asistente Ask Rubén AI", body_style),
         Paragraph("Agente conversacional Gemini API con Smart Navigator (deep linking) y Matcher ATS de vacantes.", body_style),
         Paragraph("Google Gemini API, Prompt Engineering, JS Controls", body_style),
         Paragraph("<b>Planificado</b>", body_style)],
        [Paragraph("<b>Fase 3: SaaS Platform</b><br/>Cloud Multiusuario", body_style),
         Paragraph("Plataforma web con autenticación, parser automático de PDFs con IA y portal de métricas para postulantes.", body_style),
         Paragraph("Next.js/Python, PostgreSQL/Supabase, Gemini Multimodal", body_style),
         Paragraph("<b>Visión Estratégica</b>", body_style)]
    ]
    t_roadmap = Table(roadmap_data, colWidths=[1.5*inch, 2.7*inch, 1.8*inch, 1.2*inch])
    t_roadmap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.75, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_roadmap)

    story.append(Spacer(1, 6))

    cta_content = [
        [Paragraph(
            "<b>PLAN DE ACCIÓN INMEDIATO RECOMENDADO:</b><br/>"
            "<b>1. Resguardo de Activos V1:</b> El dossier oficial DNDA (.zip con hash SHA-256 y memoria técnica) está generado y listo para su presentación en TAD.<br/>"
            "<b>2. Instrumentación de Telemetría (Fase 2 - Paso 1):</b> Implementar el objeto <code>window.dataLayer</code> nativo en el código para iniciar la captación de eventos analíticos que validen la plataforma.",
            callout_style
        )]
    ]
    t_cta = Table(cta_content, colWidths=[7.2*inch])
    t_cta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, C_ACCENT),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_cta)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado con éxito: {filename}")

if __name__ == "__main__":
    primary_file = "Plan_Estrategico_CV_Ejecutivo_Inteligente_Ruben_Barrios.pdf"
    build_pdf(primary_file)


