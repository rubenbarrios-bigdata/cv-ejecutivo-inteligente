-- =========================================================================
-- CV Ejecutivo Inteligente - Telemetry Analytics Engine
-- Modelo: Vista Analítica de Interacciones con KPIs Estratégicos
-- Autor: Rubén David Barrios Bello | Data Analyst
-- Plataforma: CV Ejecutivo Inteligente
-- Motor: Google Cloud BigQuery (Standard SQL)
-- =========================================================================
-- Descripción:
-- Desanida (UNNEST) la estructura de arrays 'event_params' de GA4 para extraer
-- las dimensiones personalizadas de cada clic en las tarjetas de KPI del CV:
-- (+4 Años Métricas, Ratio Fraude -80%, +15 Años Banca, 9 Proyectos Analytics).
-- =========================================================================

CREATE OR REPLACE VIEW `talent-intelligence-career-tic.analytics_tic.vw_kpi_interactions` AS
WITH raw_kpi_events AS (
    SELECT
        PARSE_DATE('%Y%m%d', event_date) AS fecha_evento,
        TIMESTAMP_MICROS(event_timestamp) AS timestamp_utc,
        event_name,
        user_pseudo_id,
        (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS session_id,
        
        -- Dimensiones personalizadas desanidadas
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'candidate_id') AS candidate_id,
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'kpi_id') AS kpi_id,
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'kpi_number') AS kpi_number,
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'kpi_label') AS kpi_label,
        (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'target_anchor') AS target_anchor,
        
        -- Contexto técnico y geográfico del visitante/reclutador
        device.category AS tipo_dispositivo,
        device.web_info.browser AS navegador,
        device.operating_system AS sistema_operativo,
        geo.country AS pais_origen,
        geo.city AS ciudad_origen
    FROM
        -- Reemplazar con el ID exacto del dataset de tu propiedad en BigQuery
        `talent-intelligence-career-tic.analytics_*.events_*`
    WHERE
        event_name = 'cv_kpi_interaction'
)
SELECT
    fecha_evento,
    timestamp_utc,
    candidate_id,
    kpi_id,
    kpi_number,
    kpi_label,
    target_anchor,
    tipo_dispositivo,
    pais_origen,
    ciudad_origen,
    user_pseudo_id,
    session_id,
    COUNT(1) OVER (PARTITION BY kpi_id) AS total_historico_clics_kpi,
    DENSE_RANK() OVER (PARTITION BY fecha_evento ORDER BY COUNT(1) OVER(PARTITION BY fecha_evento, kpi_id) DESC) AS ranking_kpi_del_dia
FROM
    raw_kpi_events;
