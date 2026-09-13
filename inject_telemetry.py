import re

GTM_HEAD_SNIPPET = """    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-P2Z4TZ4Z');</script>
    <!-- End Google Tag Manager -->
"""

GTM_BODY_SNIPPET = """    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P2Z4TZ4Z"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
"""

TELEMETRY_ENGINE_JS = """
// =========================================================================
// CV EJECUTIVO INTELIGENTE: Capa de Telemetría & DataLayer Multiusuario
// Plataforma: CV Ejecutivo Inteligente
// =========================================================================
window.dataLayer = window.dataLayer || [];

function trackCvEvent(eventName, eventParams = {}) {
    window.dataLayer = window.dataLayer || [];
    const eventPayload = {
        event: eventName,
        candidate_id: "ruben_barrios",
        candidate_name: "Rubén David Barrios Bello",
        platform_name: "CV Ejecutivo Inteligente",
        platform_version: "1.0",
        screen_type: window.innerWidth < 900 ? "mobile" : "desktop",
        page_location: window.location.href,
        page_title: document.title,
        event_time: new Date().toISOString(),
        ...eventParams
    };
    window.dataLayer.push(eventPayload);
    console.log(`%c[CV Telemetry] %c${eventName}`, 'color: #0284c7; font-weight: bold;', 'color: #38bdf8;', eventPayload);
}
window.trackTicEvent = trackCvEvent; // Alias de retrocompatibilidad

function trackKpiClick(kpiId, kpiNumber, kpiLabel, targetAnchor) {
    trackTicEvent("cv_kpi_interaction", {
        kpi_id: kpiId,
        kpi_number: kpiNumber,
        kpi_label: kpiLabel,
        target_anchor: targetAnchor
    });
}

function trackCertFilter(category, count = 0) {
    trackTicEvent("cv_cert_filter", {
        filter_category: category,
        certificates_shown: count
    });
}

function trackDocumentDownload(docType, docName) {
    trackTicEvent("cv_document_download", {
        document_type: docType,
        document_name: docName
    });
}

function trackThemeToggle(newTheme) {
    trackTicEvent("cv_theme_toggle", {
        theme_applied: newTheme
    });
}

function trackLanguageSwitch(newLang) {
    trackTicEvent("cv_language_switch", {
        selected_language: newLang
    });
}

function trackExternalClick(linkType, targetUrl) {
    trackTicEvent("cv_external_click", {
        link_type: linkType,
        target_url: targetUrl
    });
}

function initScrollDepthTracking() {
    const trackedThresholds = new Set();
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        if (docHeight <= 0) return;
        const scrollPercent = Math.round((scrollTop / docHeight) * 100);

        [25, 50, 75, 100].forEach(threshold => {
            if (scrollPercent >= threshold && !trackedThresholds.has(threshold)) {
                trackedThresholds.add(threshold);
                trackTicEvent("cv_scroll_depth", {
                    depth_percentage: threshold
                });
            }
        });
    }, { passive: true });
}

function initTelemetryListeners() {
    initScrollDepthTracking();

    // Descargas PDF
    document.querySelectorAll('a[href*=".pdf"], #pdfDownloadBtn, .btn-pdf-action').forEach(el => {
        el.addEventListener('click', () => {
            const href = el.getAttribute('href') || 'CV_Ruben_Barrios_Analista_De_Datos.pdf';
            trackDocumentDownload('pdf', href);
        });
    });

    // Enlaces de contacto y externos
    document.querySelectorAll('a[href^="mailto:"], a[href^="tel:"], a[href*="wa.me"], a[href*="linkedin.com"], a[href*="github.com"]').forEach(el => {
        el.addEventListener('click', () => {
            const href = el.getAttribute('href') || '';
            let type = 'other';
            if (href.includes('linkedin.com')) type = 'linkedin';
            else if (href.includes('github.com')) type = 'github';
            else if (href.includes('wa.me')) type = 'whatsapp';
            else if (href.startsWith('mailto:')) type = 'email';
            else if (href.startsWith('tel:')) type = 'phone';
            trackExternalClick(type, href);
        });
    });
}
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inyectar GTM en <head> si no está presente
    if "GTM-P2Z4TZ4Z" not in content:
        if "<head>" in content:
            content = content.replace("<head>", "<head>\n" + GTM_HEAD_SNIPPET, 1)

    # 2. Inyectar GTM noscript inmediatamente después de <body>
    if "ns.html?id=GTM-P2Z4TZ4Z" not in content:
        if "<body>" in content:
            content = content.replace("<body>", "<body>\n" + GTM_BODY_SNIPPET, 1)

    # 3. Inyectar Telemetry Engine en el <script> principal
    if "function trackTicEvent" not in content:
        kpis_anchor = "async function loadKpis"
        if kpis_anchor in content:
            content = content.replace(kpis_anchor, TELEMETRY_ENGINE_JS + "\n        " + kpis_anchor, 1)

    # 4. Actualizar llamadas en renderKpis
    content = re.sub(
        r'onclick="scrollToTarget\(\'([^\']+)\'\);\s*return false;"',
        r'onclick="if(typeof trackKpiClick===\'function\') trackKpiClick(\'${kpi.id}\', \'${kpi.number}\', \'${kpi.label}\', \'${kpi.target}\'); scrollToTarget(\'${kpi.target}\'); return false;"',
        content
    )

    # 5. Conectar trackThemeToggle en toggleTheme()
    if "trackThemeToggle" not in content:
        theme_target = "localStorage.setItem('cv_theme_choice', newTheme);\n            updateThemeButton(newTheme);"
        if theme_target in content:
            content = content.replace(theme_target, theme_target + "\n            if (typeof trackThemeToggle === 'function') trackThemeToggle(newTheme);")

    # 6. Conectar trackLanguageSwitch en setLanguage()
    if "trackLanguageSwitch" not in content:
        lang_target = "document.documentElement.setAttribute('lang', lang);"
        if lang_target in content:
            content = content.replace(lang_target, lang_target + "\n            if (typeof trackLanguageSwitch === 'function') trackLanguageSwitch(lang);")

    # 7. Conectar trackCertFilter en filterCerts()
    if "trackCertFilter" not in content:
        cert_target = "renderCertificates(cat);"
        if cert_target in content:
            content = content.replace(cert_target, "renderCertificates(cat);\n            if (typeof trackCertFilter === 'function') trackCertFilter(cat);")

    # 8. Iniciar listeners en DOMContentLoaded
    if "initTelemetryListeners()" not in content:
        init_target = "renderCertificates('all');\n        });"
        if init_target in content:
            content = content.replace(init_target, "renderCertificates('all');\n            if (typeof initTelemetryListeners === 'function') initTelemetryListeners();\n        });")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Telemetry successfully injected into: {filepath}")

if __name__ == "__main__":
    process_file("CV_Ruben_Barrios.html")
    process_file("CV_Ruben_Barrios_Mobile.html")
