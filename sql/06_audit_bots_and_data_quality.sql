-- =========================================================================
-- CV Ejecutivo Inteligente - Telemetry Analytics Engine
-- Modelo: Auditoría de Tráfico Sintético (Bots Datacenters vs. Tráfico Humano)
-- Autor: Rubén David Barrios Bello | Data Analyst
-- Plataforma: CV Ejecutivo Inteligente
-- Motor: Google Cloud BigQuery (Standard SQL)
-- =========================================================================
-- Descripción:
-- 1. Identifica y categoriza sesiones provenientes de datacenters de Azure y AWS
--    (Boydton, Dulles, Ashburn, Council Bluffs, Boardman).
-- 2. Evalúa el impacto de Data Quality: compara la tasa de conversión bruta
--    (contaminada por bots) contra la tasa de conversión real limpia.
-- =========================================================================

-- CONSULTA 1: AUDITORÍA GEOGRÁFICA Y DETECCIÓN DE ANOMALÍAS
SELECT
  geo.country AS pais,
  geo.city AS ciudad,
  device.category AS dispositivo,
  COUNT(DISTINCT (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id')) AS total_sesiones,
  COUNTIF(event_name = 'page_view') AS total_visitas_pagina,
  COUNTIF(event_name IN ('cv_document_download', 'cv_download_pdf', 'cv_contact_channel')) AS conversiones_clave,
  CASE
    WHEN geo.country = 'United States' AND geo.city IN ('Boydton', 'Dulles', 'Ashburn', 'Council Bluffs', 'Boardman')
      THEN '🚨 Bot Sintético (Azure / AWS / GCP Datacenter)'
    ELSE '✅ Tráfico Humano Legítimo'
  END AS clasificacion_trafico
FROM
  `talent-intelligence-career-tic.analytics_553518369.events_*`
WHERE
  _TABLE_SUFFIX >= '20260901'
GROUP BY
  pais, ciudad, dispositivo, clasificacion_trafico
ORDER BY
  total_visitas_pagina DESC;

-- =========================================================================
-- CONSULTA 2: IMPACTO EN EL NEGOCIO (CONVERSIÓN CONTAMINADA VS. CONVERSIÓN REAL)
-- =========================================================================
WITH raw_events AS (
  SELECT
    event_date,
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS session_id,
    event_name,
    CASE
      WHEN geo.country = 'United States' AND geo.city IN ('Boydton', 'Dulles', 'Ashburn', 'Council Bluffs', 'Boardman')
        THEN TRUE
      ELSE FALSE
    END AS es_bot_datacenter
  FROM
    `talent-intelligence-career-tic.analytics_553518369.events_*`
  WHERE
    _TABLE_SUFFIX >= '20260901'
)

SELECT
  COUNT(DISTINCT session_id) AS total_sesiones_brutas,
  COUNT(DISTINCT IF(es_bot_datacenter, session_id, NULL)) AS sesiones_bots_descartadas,
  COUNT(DISTINCT IF(NOT es_bot_datacenter, session_id, NULL)) AS sesiones_humanas_validas,
  
  -- Dilución de métricas: la tasa contaminada parece artificialmente baja porque el denominador está inflado por bots
  ROUND(SAFE_DIVIDE(
    COUNT(DISTINCT IF(event_name IN ('cv_document_download', 'cv_download_pdf', 'cv_contact_channel'), session_id, NULL)),
    COUNT(DISTINCT session_id)
  ) * 100, 2) AS tasa_conversion_bruta_contaminada_pct,

  -- Tasa real de conversión humana
  ROUND(SAFE_DIVIDE(
    COUNT(DISTINCT IF(NOT es_bot_datacenter AND event_name IN ('cv_document_download', 'cv_download_pdf', 'cv_contact_channel'), session_id, NULL)),
    COUNT(DISTINCT IF(NOT es_bot_datacenter, session_id, NULL))
  ) * 100, 2) AS tasa_conversion_limpia_real_pct
FROM
  raw_events;
