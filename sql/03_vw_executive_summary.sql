-- =========================================================================
-- CV Ejecutivo Inteligente - Telemetry Analytics Engine
-- Modelo: Resumen Ejecutivo Diario de Audiencia y Preferencias UX
-- Autor: Rubén David Barrios Bello | Data Analyst
-- Plataforma: CV Ejecutivo Inteligente
-- Motor: Google Cloud BigQuery (Standard SQL)
-- =========================================================================

CREATE OR REPLACE VIEW `talent-intelligence-career-tic.analytics_tic.vw_executive_summary` AS
WITH daily_metrics AS (
    SELECT
        PARSE_DATE('%Y%m%d', event_date) AS fecha,
        user_pseudo_id,
        (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS session_id,
        event_name,
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'selected_language') AS idioma_evento,
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'theme_applied') AS tema_evento,
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'document_name') AS doc_descargado,
        geo.country AS pais,
        device.category AS dispositivo
    FROM
        `talent-intelligence-career-tic.analytics_*.events_*`
)
SELECT
    fecha,
    pais,
    dispositivo,
    COUNT(DISTINCT user_pseudo_id) AS usuarios_unicos,
    COUNT(DISTINCT session_id) AS sesiones_totales,
    COUNTIF(event_name = 'page_view') AS total_pageviews,
    COUNTIF(event_name = 'cv_kpi_interaction') AS total_clics_kpis,
    COUNTIF(event_name = 'cv_document_download') AS total_descargas_pdf,
    COUNTIF(event_name = 'cv_language_switch' AND idioma_evento = 'en') AS cambios_a_ingles,
    COUNTIF(event_name = 'cv_language_switch' AND idioma_evento = 'es') AS cambios_a_espanol,
    COUNTIF(event_name = 'cv_theme_toggle' AND tema_evento = 'dark') AS cambios_modo_oscuro,
    COUNTIF(event_name = 'cv_theme_toggle' AND tema_evento = 'light') AS cambios_modo_claro
FROM
    daily_metrics
GROUP BY
    fecha,
    pais,
    dispositivo
ORDER BY
    fecha DESC,
    sesiones_totales DESC;
