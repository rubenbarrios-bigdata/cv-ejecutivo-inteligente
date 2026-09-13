import os
import zipfile
import hashlib
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

def create_zip_archive():
    zip_filename = "CV_Ejecutivo_Inteligente_v1.0_Codigo_Fuente_Ruben_Barrios.zip"
    files_to_include = [
        "CV_Ruben_Barrios.html",
        "CV_Ruben_Barrios_Mobile.html",
        "index.html",
        "mobile.html",
        "data.json",
        "data_en.json",
        "README.md",
        "Plan_Estrategico_CV_Ejecutivo_Inteligente_Ruben_Barrios.pdf",
        "CV_Ruben_Barrios_Analista_De_Datos.pdf"
    ]
    dirs_to_include = ["certs_images", "screenshots"]

    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for f in files_to_include:
            if os.path.exists(f):
                zipf.write(f, arcname=f"CV_Ejecutivo_Inteligente_v1.0/{f}")
        for d in dirs_to_include:
            if os.path.exists(d):
                for root, _, filenames in os.walk(d):
                    for fn in filenames:
                        full_p = os.path.join(root, fn)
                        rel_p = os.path.relpath(full_p, ".")
                        zipf.write(full_p, arcname=f"CV_Ejecutivo_Inteligente_v1.0/{rel_p}")

    # Compute hashes
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()
    with open(zip_filename, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
            md5_hash.update(byte_block)

    file_size_bytes = os.path.getsize(zip_filename)
    file_size_kb = round(file_size_bytes / 1024, 2)

    return {
        "filename": zip_filename,
        "sha256": sha256_hash.hexdigest(),
        "md5": md5_hash.hexdigest(),
        "size_kb": file_size_kb,
        "size_bytes": file_size_bytes
    }

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 752, "CV Ejecutivo Inteligente — Memoria Técnica y Descriptiva (DNDA / Ley 11.723)")
            self.setStrokeColor(colors.HexColor("#e2e8f0"))
            self.setLineWidth(0.6)
            self.line(54, 744, 558, 744)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.6)
        self.line(54, 48, 558, 48)
        self.drawString(54, 36, "Autor: Rubén David Barrios Bello • Buenos Aires, Argentina • Expediente DNDA / TAD")
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(558, 36, page_str)
        self.restoreState()

def generate_pdf(zip_meta):
    pdf_filename = "Memoria_Tecnica_Descriptiva_DNDA_Ruben_Barrios.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=60
    )

    styles = getSampleStyleSheet()
    
    c_primary = colors.HexColor("#0c1e33")
    c_accent = colors.HexColor("#0284c7")
    c_dark = colors.HexColor("#1e293b")
    c_muted = colors.HexColor("#64748b")
    c_light = colors.HexColor("#f8fafc")
    c_border = colors.HexColor("#cbd5e1")

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=c_primary,
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=c_accent,
        spaceAfter=15
    )
    h1_style = ParagraphStyle(
        'SecH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_primary,
        spaceBefore=12,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_dark,
        spaceAfter=6
    )
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    code_style = ParagraphStyle(
        'HashText',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0f172a")
    )
    badge_style = ParagraphStyle(
        'Badge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0369a1")
    )

    story = []

    # Title & Legal Heading
    story.append(Paragraph("REPÚBLICA ARGENTINA • MINISTERIO DE JUSTICIA", badge_style))
    story.append(Paragraph("DIRECCIÓN NACIONAL DEL DERECHO DE AUTOR (DNDA) — PLATAFORMA TAD", ParagraphStyle('SubTop', parent=badge_style, fontSize=7.5, textColor=c_muted, spaceAfter=8)))
    story.append(Paragraph("MEMORIA TÉCNICA Y DESCRIPTIVA DE SOFTWARE", title_style))
    story.append(Paragraph("Depósito de Obra Inédita / Soporte Lógico • Régimen Legal Ley N° 11.723 de Propiedad Intelectual", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_accent, spaceBefore=0, spaceAfter=12))

    # Section 1: Identificación de la Obra y del Autor
    story.append(Paragraph("1. IDENTIFICACIÓN FORMAL DE LA OBRA Y TITULARIDAD", h1_style))
    
    meta_table_data = [
        [Paragraph("<b>Denominación de la Obra:</b>", body_style), Paragraph("<b>CV Ejecutivo Inteligente</b>", body_bold)],
        [Paragraph("<b>Acrónimo / Subtítulo:</b>", body_style), Paragraph("CV Ejecutivo Inteligente", body_style)],
        [Paragraph("<b>Género / Tipo de Creación:</b>", body_style), Paragraph("Software / Soporte Lógico / Aplicación Web Interactiva", body_style)],
        [Paragraph("<b>Versión Depositada:</b>", body_style), Paragraph("Versión 1.0 (Core & Executive Dashboard)", body_style)],
        [Paragraph("<b>Autor y Titular Exclusivo:</b>", body_style), Paragraph("<b>Rubén David Barrios Bello</b>", body_bold)],
        [Paragraph("<b>Nacionalidad de Origen:</b>", body_style), Paragraph("Venezolana", body_style)],
        [Paragraph("<b>Radicación y Residencia:</b>", body_style), Paragraph("Ciudad Autónoma de Buenos Aires, República Argentina (desde 2018)", body_style)],
        [Paragraph("<b>Perfil Profesional:</b>", body_style), Paragraph("Licenciado en Banca y Finanzas • Data Analyst & BI Specialist", body_style)],
        [Paragraph("<b>Lugar y Año de Fijación:</b>", body_style), Paragraph("Buenos Aires, República Argentina — 2026", body_style)],
        [Paragraph("<b>Dominio / Repositorio Público:</b>", body_style), Paragraph("https://rubenbarrios-bigdata.github.io/cv-ejecutivo-inteligente/", code_style)]
    ]
    t_meta = Table(meta_table_data, colWidths=[160, 344])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.4, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # Section 2: Comprobación Criptográfica
    story.append(Paragraph("2. DECLARACIÓN DE INTEGRIDAD Y HUELLA CRIPTOGRÁFICA DEL SOPORTE LÓGICO", h1_style))
    story.append(Paragraph(
        "A los efectos de otorgar plena certeza temporal, inalterabilidad probatoria y constancia de intangibilidad digital "
        "respecto al contenido exacto del código fuente depositado bajo el régimen de la Ley 11.723, se certifica la huella "
        "criptográfica del paquete de archivos que conforma la presente obra técnica:",
        body_style
    ))

    hash_table_data = [
        [Paragraph("<b>Archivo Comprimido:</b>", body_style), Paragraph(f"<b>{zip_meta['filename']}</b>", body_style)],
        [Paragraph("<b>Tamaño del Archivo:</b>", body_style), Paragraph(f"{zip_meta['size_kb']} KB ({zip_meta['size_bytes']:,} bytes)", body_style)],
        [Paragraph("<b>Algoritmo Hash SHA-256:</b>", body_style), Paragraph(f"<b>{zip_meta['sha256']}</b>", code_style)],
        [Paragraph("<b>Algoritmo Hash MD5:</b>", body_style), Paragraph(f"{zip_meta['md5']}", code_style)]
    ]
    t_hash = Table(hash_table_data, colWidths=[140, 364])
    t_hash.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#94a3b8")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_hash)
    story.append(Spacer(1, 10))

    # Section 3: Memoria Descriptiva Funcional
    story.append(Paragraph("3. MEMORIA DESCRIPTIVA Y OBJETO DEL SOFTWARE", h1_style))
    story.append(Paragraph(
        "<b>CV Ejecutivo Inteligente</b> es una aplicación y plataforma interactiva concebida con criterio analítico "
        "que revoluciona la presentación curricular transformándola en un <b>Executive Dashboard de métricas y analítica profesional</b>. "
        "A diferencia de los currículums tradicionales impresos en papel o exportados a formatos de documento estático, opera como un "
        "sistema de inteligencia curricular desacoplado, modular y altamente reactivo, permitiendo a decisores de negocio y reclutadores técnicos "
        "interactuar con la trayectoria profesional del autor mediante indicadores cuantitativos verificables.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Principios de Diseño e Innovación Técnica:</b>", body_bold
    ))
    bullet_items_sec3 = [
        "• <b>Mentalidad de Dashboard Ejecutivo:</b> Estructuración de la propuesta de valor profesional mediante 4 Indicadores Clave de Rendimiento (KPIs) primarios: <i>+4 Años Analizando Métricas</i>, <i>0,150 ➔ 0,030 Ratio Fraude (-80%)</i>, <i>+15 Años Sector Bancario</i> y <i>9 Proyectos Data Analytics</i>.",
        "• <b>Desacoplamiento Arquitectónico (Data Layer vs Presentation):</b> La información de indicadores, tooltips y taxonomías reside en esquemas de datos estructurados en formato JSON (<code>data.json</code> y <code>data_en.json</code>), desacoplados de la plantilla HTML. Esto garantiza escalabilidad, gobierno de datos y mantenimiento ágil.",
        "• <b>Resiliencia con Fallback Progresivo:</b> Motor JavaScript con doble vía de carga: consumo asíncrono vía <code>fetch API</code> con promesas en entornos web, y fallback nativo pre-renderizado con inyección en el DOM ante aperturas locales desconectadas (<code>file:///</code>).",
        "• <b>Motor Bilingüe Reactivo (ES/EN):</b> Conmutación instantánea de idiomas sin recarga de página, actualizando títulos, descripciones, atributos de accesibilidad y textos de manera dinámica.",
        "• <b>Centro Interactivo de Certificaciones:</b> Módulo de filtrado multidimensional por categorías técnicas (Data & BI, IA & Machine Learning, Programación, Metodologías Ágiles) con renderizado dinámico de tarjetas y enlaces a credenciales verificables (Credly, etc.).",
        "• <b>Doble Arquitectura de Interfaz (Desktop & Native Mobile):</b> Diseños especializados para pantallas de escritorio y vista optimizada para interacción táctil vertical en smartphones."
    ]
    for b in bullet_items_sec3:
        story.append(Paragraph(b, body_style))
        story.append(Spacer(1, 2))
    story.append(Spacer(1, 6))

    # Section 4: Estructura del Soporte Lógico Depositado
    story.append(Paragraph("4. ESTRUCTURA Y COMPONENTES DEL SOPORTE LÓGICO DEPOSITADO", h1_style))
    story.append(Paragraph(
        "El paquete de código fuente comprimido contiene los siguientes módulos y archivos esenciales:",
        body_style
    ))

    struct_table_data = [
        [Paragraph("<b>Archivo / Módulo</b>", body_bold), Paragraph("<b>Lenguaje / Formato</b>", body_bold), Paragraph("<b>Función Técnica en la Arquitectura</b>", body_bold)],
        [Paragraph("<code>CV_Ruben_Barrios.html</code><br/><code>index.html</code>", code_style), Paragraph("HTML5 / CSS3 / JS", body_style), Paragraph("Interfaz web principal para entornos desktop. Integra el dashboard, filtros dinámicos y esquema Schema.org JSON-LD.", body_style)],
        [Paragraph("<code>CV_Ruben_Barrios_Mobile.html</code><br/><code>mobile.html</code>", code_style), Paragraph("HTML5 / CSS3 / JS", body_style), Paragraph("Interfaz táctil adaptada para navegación vertical rápida en terminales móviles.", body_style)],
        [Paragraph("<code>data.json</code>", code_style), Paragraph("JSON", body_style), Paragraph("Capa de datos central (Data Layer) en español: almacena valores de KPIs, rutas, iconos y metadatos.", body_style)],
        [Paragraph("<code>data_en.json</code>", code_style), Paragraph("JSON", body_style), Paragraph("Capa de datos internacional en idioma inglés con nomenclatura analítica adaptada.", body_style)],
        [Paragraph("<code>README.md</code>", code_style), Paragraph("Markdown", body_style), Paragraph("Documentación del software, guía de ejecución, especificación de capas y declaración formal de autoría.", body_style)],
        [Paragraph("<code>Plan_Estrategico_*.pdf</code>", code_style), Paragraph("PDF / ReportLab", body_style), Paragraph("Dossier maestro de arquitectura de la plataforma y hoja de ruta evolutiva de CV Ejecutivo Inteligente.", body_style)],
        [Paragraph("<code>certs_images/</code>", code_style), Paragraph("Imágenes WebP/PNG", body_style), Paragraph("Directorio de activos visuales de certificaciones técnicas verificadas.", body_style)],
        [Paragraph("<code>screenshots/</code>", code_style), Paragraph("Imágenes PNG", body_style), Paragraph("Evidencia gráfica del renderizado visual de la interfaz de usuario en modo claro y oscuro.", body_style)]
    ]
    t_struct = Table(struct_table_data, colWidths=[120, 94, 290])
    t_struct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f2b48")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.4, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_struct)
    story.append(Spacer(1, 10))

    # Section 5: Hoja de Ruta Conceptual
    story.append(Paragraph("5. HOJA DE RUTA EVOLUTIVA Y ESPECIFICACIÓN CONCEPTUAL (MACRO-FASE 2)", h1_style))
    story.append(Paragraph(
        "Se deja expresa constancia en el presente depósito de la propiedad intelectual correspondiente a la <b>arquitectura conceptual "
        "y metodológica de los módulos complementarios de CV Ejecutivo Inteligente</b> programados para su despliegue en etapas sucesivas:",
        body_style
    ))
    bullet_items_sec5 = [
        "• <b>Módulo de Telemetría Web y Analítica Digital:</b> Inyección de eventos en <code>window.dataLayer</code> nativo para medición de interacciones de reclutadores, clicks en KPIs, profundidad de scroll y consumo de certificaciones vía Google Tag Manager (GTM) y Google Analytics 4 (GA4).",
        "• <b>Pipeline Cloud y Dashboard Público de Rendimiento:</b> Conexión automatizada de telemetría hacia Google BigQuery y modelado en Looker Studio para exhibir métricas de consumo del propio CV en tiempo real.",
        "• <b>Agente Conversacional 'Ask Rubén AI':</b> Asistente inteligente basado en Google Gemini integrado a la interfaz para responder consultas técnicas de reclutadores y navegar dinámicamente hacia las secciones de evidencia del CV.",
        "• <b>Motor de Ajuste de Perfiles (Job Matching ATS):</b> Algoritmo de comparación semántica entre descripciones de vacantes laborales y el stack analítico de la plataforma."
    ]
    for b in bullet_items_sec5:
        story.append(Paragraph(b, body_style))
        story.append(Spacer(1, 2))
    story.append(Spacer(1, 10))

    # Section 6: Declaración Jurada y Reserva Legal
    story.append(Paragraph("6. DECLARACIÓN JURADA DE AUTORÍA Y RESERVA DE DERECHOS", h1_style))
    story.append(Paragraph(
        "El abajo firmante, <b>Rubén David Barrios Bello</b>, en su condición de autor, diseñador y programador creador de la plataforma "
        "<b>CV Ejecutivo Inteligente</b>, declara bajo juramento que la presente obra técnica y el soporte lógico que la integra "
        "son de su autoría original y creación exclusiva, no vulnerando derechos de terceros ni habiendo cedido con anterioridad la titularidad "
        "de los mismos. Se efectúa el depósito en los términos del régimen establecido por la <b>Ley N° 11.723</b> de la República Argentina, "
        "reservándose expresamente la totalidad de los derechos morales y patrimoniales que de ella se derivan.",
        body_style
    ))
    story.append(Spacer(1, 15))

    # Signature Block
    sig_data = [
        [Paragraph("<b>Lugar y Fecha:</b> Ciudad Autónoma de Buenos Aires, República Argentina — 2026", body_style)],
        [Spacer(1, 20)],
        [Paragraph("___________________________________________________", body_style)],
        [Paragraph("<b>Rubén David Barrios Bello</b><br/>Autor y Titular Exclusivo<br/>CV Ejecutivo Inteligente", body_style)]
    ]
    t_sig = Table(sig_data, colWidths=[504])
    t_sig.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(KeepTogether(t_sig))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF Generated: {pdf_filename}")

if __name__ == "__main__":
    zip_meta = create_zip_archive()
    print("ZIP Created successfully:")
    print(f"File: {zip_meta['filename']}")
    print(f"Size: {zip_meta['size_kb']} KB")
    print(f"SHA-256: {zip_meta['sha256']}")
    print(f"MD5: {zip_meta['md5']}")
    
    generate_pdf(zip_meta)
