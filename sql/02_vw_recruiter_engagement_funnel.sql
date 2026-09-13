-- =========================================================================
-- CV Ejecutivo Inteligente - Telemetry Analytics Engine
-- Modelo: Embudo de Conversión de Reclutadores (Recruiter Engagement Funnel)
-- Autor: Rubén David Barrios Bello | Data Analyst
-- Plataforma: CV Ejecutivo Inteligente
-- Motor: Google Cloud BigQuery (Standard SQL)
-- =========================================================================
-- Descripción:
-- Modela las etapas de interés de un reclutador o hiring manager por sesión:
-- Etapa 1: Llegada al CV (page_view)
-- Etapa 2: Lectura profunda (cv_scroll_depth >= 50%)
-- Etapa 3: Interés en Métricas Clave (cv_kpi_interaction)
-- Etapa 4: Validación de Habilidades (cv_cert_filter)
-- Etapa 5: Conversión Máxima (cv_document_download de PDF o cv_external_click)
-- =========================================================================

CREATE OR REPLACE VIEW `talent-intelligence-career-tic.analytics_tic.vw_recruiter_engagement_funnel` AS
WITH session_events AS (
    SELECT
        PARSE_DATE('%Y%m%d', event_date) AS fecha_sesion,
        user_pseudo_id,
        (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS session_id,
        event_name,
        (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'depth_percentage') AS scroll_depth,
        device.category AS dispositivo,
        geo.country AS pais
    FROM
        `talent-intelligence-career-tic.analytics_*.events_*`
),
session_flags AS (
    SELECT
        fecha_sesion,
        user_pseudo_id,
        session_id,
        dispositivo,
        pais,
        -- Banderas de etapas del embudo
        MAX(IF(event_name = 'page_view', 1, 0)) AS paso_1_llegada_cv,
        MAX(IF(event_name = 'cv_scroll_depth' AND scroll_depth >= 50, 1, 0)) AS paso_2_lectura_profunda_50pct,
        MAX(IF(event_name = 'cv_kpi_interaction', 1, 0)) AS paso_3_interaccion_kpis,
        MAX(IF(event_name = 'cv_cert_filter', 1, 0)) AS paso_4_filtro_certificaciones,
        MAX(IF(event_name IN ('cv_document_download', 'cv_external_click'), 1, 0)) AS paso_5_conversion_contacto_descarga
    FROM
        session_events
    WHERE
        session_id IS NOT NULL
    GROUP BY
        fecha_sesion,
        user_pseudo_id,
        session_id,
        dispositivo,
        pais
)
SELECT
    fecha_sesion,
    dispositivo,
    pais,
    COUNT(DISTINCT session_id) AS total_sesiones,
    SUM(paso_1_llegada_cv) AS etapa_1_visitas,
    SUM(paso_2_lectura_profunda_50pct) AS etapa_2_lectura_50,
    SUM(paso_3_interaccion_kpis) AS etapa_3_exploro_kpis,
    SUM(paso_4_filtro_certificaciones) AS etapa_4_exploro_certificaciones,
    SUM(paso_5_conversion_contacto_descarga) AS etapa_5_contacto_o_descarga,
    
    -- Tasas de Conversión Analíticas (Conversion Rates)
    SAFE_DIVIDE(SUM(paso_2_lectura_profunda_50pct), SUM(paso_1_llegada_cv)) * 100 AS tasa_retencion_lectura_pct,
    SAFE_DIVIDE(SUM(paso_3_interaccion_kpis), SUM(paso_1_llegada_cv)) * 100 AS tasa_engagement_kpis_pct,
    SAFE_DIVIDE(SUM(paso_5_conversion_contacto_descarga), SUM(paso_1_llegada_cv)) * 100 AS tasa_conversion_final_pct
FROM
    session_flags
GROUP BY
    fecha_sesion,
    dispositivo,
    pais;
