-- =========================================================================
-- CV Ejecutivo Inteligente - Telemetry Analytics Engine
-- Modelo: Embudo Limpio para Looker Studio (Exclusión de Crawlers/Datacenters)
-- Autor: Rubén David Barrios Bello | Data Analyst
-- Plataforma: CV Ejecutivo Inteligente
-- Motor: Google Cloud BigQuery (Standard SQL)
-- =========================================================================
-- Descripción:
-- Consulta analítica para Looker Studio con exclusión de datacenters conocidos
-- (Microsoft Azure, AWS, GCP) y cálculo de tasa de conversión por sesión humana válida.
-- =========================================================================

WITH raw_data AS (
  SELECT
    event_date,
    device.category AS device_type,
    geo.city,
    geo.country,
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS session_id,
    event_name,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'contact_channel') AS contact_channel
  FROM
    `rubenbarrios-analytics.analytics_cv_ejecutivo.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260901' AND '20260930'
),

clean_sessions AS (
  SELECT
    *
  FROM
    raw_data
  WHERE
    -- Exclusión analítica de datacenters identificados (Microsoft Azure, AWS, GCP)
    NOT (country = 'United States' AND city IN ('Boydton', 'Dulles', 'Ashburn', 'Council Bluffs', 'Boardman'))
)

SELECT
  event_date,
  device_type,
  city,
  COUNT(DISTINCT session_id) AS sesiones_humanas_validas,
  COUNTIF(event_name = 'page_view') AS total_vistas_limpias,
  COUNTIF(event_name = 'cv_kpi_interaction') AS interacciones_kpis,
  COUNTIF(event_name = 'cv_cert_interaction') AS consultas_certificaciones,
  COUNTIF(event_name = 'cv_download_pdf') AS descargas_pdf_ats,
  COUNTIF(event_name = 'cv_contact_channel' AND contact_channel = 'whatsapp') AS contactos_whatsapp,
  -- Tasa de conversión real por sesión humana
  ROUND(SAFE_DIVIDE(COUNT(DISTINCT IF(event_name = 'cv_contact_channel' OR event_name = 'cv_download_pdf', session_id, NULL)), COUNT(DISTINCT session_id)) * 100, 2) AS tasa_conversion_sesion_pct
FROM
  clean_sessions
GROUP BY
  1, 2, 3
ORDER BY
  event_date DESC, sesiones_humanas_validas DESC;
