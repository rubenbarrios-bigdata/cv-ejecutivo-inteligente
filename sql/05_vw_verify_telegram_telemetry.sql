-- =========================================================================
-- CV Ejecutivo Inteligente - Telemetry Analytics Engine
-- Modelo: Verificación y Auditoría de Telemetría Reactiva (Telegram Webhook)
-- Autor: Rubén David Barrios Bello | Data Analyst
-- Plataforma: CV Ejecutivo Inteligente
-- Motor: Google Cloud BigQuery (Standard SQL)
-- =========================================================================
-- Objetivo:
-- 1. Auditar la recepción del evento 'telegram_alert_dispatch' en BigQuery.
-- 2. Desanidar parámetros operativos: alert_type, lead_action, user_location, device_type.
-- 3. Medir el SLA de entrega reactiva frente a Macro-Conversiones (Descarga PDF y Contacto).
-- 4. Certificar la gobernanza No-PII (sin exposición de datos sensibles).
-- =========================================================================

WITH telemetry_events AS (
  SELECT
    event_date,
    TIMESTAMP_MICROS(event_timestamp) AS timestamp_evento,
    event_name,
    user_pseudo_id,
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS session_id,
    geo.country AS pais,
    geo.city AS ciudad,
    device.category AS dispositivo_ga4,
    
    -- Parámetros específicos de la alerta de Telegram
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'alert_type') AS alert_type,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'lead_action') AS lead_action,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'user_location') AS user_location,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'device_type') AS device_reported,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'candidate_id') AS candidate_id,

    -- Parámetros de conversiones estándar
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'contact_channel') AS contact_channel,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'document_name') AS doc_name
  FROM
    `rubenbarrios-analytics.analytics_cv_ejecutivo.events_*`
  WHERE
    _TABLE_SUFFIX >= '20260901'
    -- Exclusión analítica de datacenters de crawlers conocidos
    AND NOT (geo.country = 'United States' AND geo.city IN ('Boydton', 'Dulles', 'Ashburn', 'Council Bluffs', 'Boardman'))
),

-- Resumen diario de alertas despachadas vs conversiones
daily_telemetry_audit AS (
  SELECT
    event_date,
    COUNTIF(event_name = 'telegram_alert_dispatch') AS total_alertas_telegram,
    COUNTIF(event_name = 'telegram_alert_dispatch' AND alert_type = 'hot_lead') AS alertas_hot_leads,
    COUNTIF(event_name = 'telegram_alert_dispatch' AND alert_type = 'qualified_visit') AS alertas_visitas_calificadas,
    
    -- Macroconversiones en el cliente
    COUNTIF(event_name IN ('cv_download_pdf', 'cv_document_download')) AS total_descargas_pdf,
    COUNTIF(event_name = 'cv_contact_channel' OR (event_name = 'cv_external_click' AND contact_channel IS NOT NULL)) AS total_contactos,
    
    -- Cobertura de telemetría (SLA de despacho reactivo)
    ROUND(
      SAFE_DIVIDE(
        COUNTIF(event_name = 'telegram_alert_dispatch' AND alert_type = 'hot_lead'),
        COUNTIF(event_name IN ('cv_download_pdf', 'cv_document_download', 'cv_contact_channel'))
      ) * 100, 2
    ) AS sla_cobertura_alertas_pct
  FROM
    telemetry_events
  GROUP BY
    event_date
)

-- Consulta Principal 1: Matriz de Auditoría y Entrega por Fecha
SELECT
  event_date,
  total_alertas_telegram,
  alertas_hot_leads,
  alertas_visitas_calificadas,
  total_descargas_pdf,
  total_contactos,
  sla_cobertura_alertas_pct
FROM
  daily_telemetry_audit
ORDER BY
  event_date DESC;

-- =========================================================================
-- CONSULTA SECUNDARIA: DETALLE DE ALERTAS DESPACHADAS (ÚLTIMAS 50)
-- =========================================================================
-- SELECT
--   timestamp_evento,
--   session_id,
--   alert_type,
--   lead_action,
--   device_reported,
--   pais,
--   ciudad,
--   user_location,
--   candidate_id
-- FROM
--   telemetry_events
-- WHERE
--   event_name = 'telegram_alert_dispatch'
-- ORDER BY
--   timestamp_evento DESC
-- LIMIT 50;
