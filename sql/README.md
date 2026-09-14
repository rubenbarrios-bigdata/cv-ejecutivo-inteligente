# 🏛️ CV Ejecutivo Inteligente - BigQuery Analytics Engine

> **Autor:** Rubén David Barrios Bello  
> **Especialidad:** Data Analyst | BI & Digital Analytics  
> **Plataforma:** CV Ejecutivo Inteligente  
> **Data Warehouse:** Google Cloud BigQuery (Standard SQL)  
> **Proyecto GCP:** `talent-intelligence-career-tic`

---

## 📐 Arquitectura de la Tubería de Datos (Data Pipeline)

```mermaid
flowchart LR
    A[CV Web Ejecutivo\nJavaScript DataLayer] -->|Eventos DataLayer| B[Google Tag Manager\nGTM-P2Z4TZ4Z]
    B -->|GA4 Measurement Protocol| C[Google Analytics 4\nG-NQC5PHY67R]
    C -->|Batch Export Diario Gratuito| D[(Google Cloud BigQuery\nDataset analytics_tic)]
    D -->|Vistas SQL Modeladas| E[Looker Studio\nDashboard Ejecutivo]
```

---

## 🗄️ Modelos de Datos & Resultados de Consultas en BigQuery

Los eventos exportados por GA4 contienen el esquema nativo de Google Analytics, donde cada evento incluye un array anidado de tipo `ARRAY<STRUCT<key STRING, value STRUCT<...>>>` denominado `event_params`.

A continuación se presentan los **3 modelos analíticos en producción**, con el **código SQL de cada consulta** y la **evidencia de los resultados reales ejecutados en Google Cloud BigQuery**:

---

### 1. Modelo de Interacciones con KPIs Estratégicos
* **Archivo:** [`01_vw_kpi_interactions.sql`](01_vw_kpi_interactions.sql)
* **Objetivo:** Desanidar (`UNNEST`) los parámetros de los KPIs del CV, medir volumen de clics por reclutador y calcular el ranking de popularidad en tiempo real con funciones de ventana (`DENSE_RANK()`).

#### Consulta SQL:
```sql
SELECT
  fecha,
  (SELECT string_val FROM UNNEST(event_params) WHERE key = 'kpi_id') AS kpi_id,
  (SELECT string_val FROM UNNEST(event_params) WHERE key = 'kpi_number') AS kpi_number,
  (SELECT string_val FROM UNNEST(event_params) WHERE key = 'kpi_label') AS kpi_label,
  COUNT(1) AS total_interacciones,
  COUNT(DISTINCT user_pseudo_id) AS reclutadores_unicos,
  DENSE_RANK() OVER (ORDER BY COUNT(1) DESC) AS ranking_impacto
FROM
  `talent-intelligence-career-tic.analytics_tic.events_*`
WHERE
  event_name = 'cv_kpi_interaction'
GROUP BY
  fecha, kpi_id, kpi_number, kpi_label
ORDER BY
  ranking_impacto ASC;
```

#### 📊 Resultado Real en BigQuery:
| Fila | Fecha | KPI ID | KPI Valor | KPI Métrica Descriptiva | Total Clics | Reclutadores Únicos | Ranking de Impacto |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :---: |
| **1** | `2026-09-09` | `kpi-ratio` | **`0,150 ➔ 0,030`** | **Ratio Fraude (-80%)** | **2** | **2** | 🥇 **1** |
| **2** | `2026-09-09` | `kpi-proyectos` | **`9 Proyectos`** | **Análisis de Datos** | **1** | **1** | 🥈 **2** |
| **3** | `2026-09-09` | `kpi-fraude` | **`+4 Años`** | **Analizando Métricas** | **1** | **1** | 🥈 **2** |

> **Insight de Negocio:** La métrica de reducción de ratio de fraude en logística/e-commerce es el principal punto de atracción de los reclutadores (Ranking #1).

---

### 2. Embudo de Conversión de Reclutadores (*Funnel Analytics*)
* **Archivo:** [`02_vw_recruiter_engagement_funnel.sql`](02_vw_recruiter_engagement_funnel.sql)
* **Objetivo:** Rastrear el recorrido analítico por sesión a través de 5 etapas progresivas y calcular las tasas de conversión y retención porcentual (`SAFE_DIVIDE`).

#### Consulta SQL:
```sql
WITH session_stages AS (
  SELECT
    session_id,
    MAX(IF(event_name = 'page_view', 1, 0)) AS paso_1_llegada,
    MAX(IF(event_name = 'cv_scroll_depth' AND scroll_depth >= 50, 1, 0)) AS paso_2_lectura_50,
    MAX(IF(event_name = 'cv_kpi_interaction', 1, 0)) AS paso_3_exploro_kpis,
    MAX(IF(event_name = 'cv_cert_filter', 1, 0)) AS paso_4_filtro_certs,
    MAX(IF(event_name = 'cv_document_download', 1, 0)) AS paso_5_descargo_cv
  FROM
    `talent-intelligence-career-tic.analytics_tic.events_*`
  GROUP BY
    session_id
)
SELECT
  COUNT(session_id) AS total_sesiones,
  SUM(paso_1_llegada) AS etapa_1_visitas,
  SUM(paso_2_lectura_50) AS etapa_2_lectura_profunda,
  SUM(paso_3_exploro_kpis) AS etapa_3_interaccion_kpis,
  SUM(paso_4_filtro_certs) AS etapa_4_filtro_certificaciones,
  SUM(paso_5_descargo_cv) AS etapa_5_descarga_cv_pdf,

  -- Tasas de Conversión Analíticas (%)
  ROUND(SAFE_DIVIDE(SUM(paso_2_lectura_50), SUM(paso_1_llegada)) * 100, 1) AS tasa_retencion_lectura_pct,
  ROUND(SAFE_DIVIDE(SUM(paso_3_exploro_kpis), SUM(paso_1_llegada)) * 100, 1) AS tasa_interes_kpis_pct,
  ROUND(SAFE_DIVIDE(SUM(paso_5_descargo_cv), SUM(paso_1_llegada)) * 100, 1) AS tasa_conversion_final_pct
FROM
  session_stages;
```

#### 📊 Resultado Real en BigQuery:
| Total Sesiones | Etapa 1: Visitas | Etapa 2: Lectura >50% | Etapa 3: Clic KPIs | Etapa 4: Filtro Certs | Etapa 5: Descarga PDF | Tasa Retención Lectura | Tasa Interés KPIs | Tasa Conversión Final |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **4** | **4** | **3** | **3** | **1** | **2** | **75.0%** | **75.0%** | 🎯 **50.0%** |

> **Insight de Negocio:** El **75%** de los visitantes lee a profundidad el contenido y explora métricas, y un contundente **50%** de las sesiones culmina con la descarga del documento formal en PDF.

---

### 3. Resumen Ejecutivo de Audiencia y Preferencias UX
* **Archivo:** [`03_vw_executive_summary.sql`](03_vw_executive_summary.sql)
* **Objetivo:** Segmentar el comportamiento de los reclutadores por tipo de dispositivo (*Desktop* vs *Mobile*), preferencia idiomática (*Español* vs *Inglés*) y adopción del modo de interfaz (*Dark Mode* vs *Light Mode*).

#### Consulta SQL:
```sql
SELECT
  dispositivo,
  COUNT(1) AS total_sesiones,
  COUNTIF(idioma = 'es') AS prefieren_espanol,
  COUNTIF(idioma = 'en') AS prefieren_ingles,
  COUNTIF(tema = 'dark') AS prefieren_modo_oscuro,
  COUNTIF(tema = 'light') AS prefieren_modo_claro,
  ROUND(SAFE_DIVIDE(COUNTIF(tema = 'dark'), COUNT(1)) * 100, 1) AS adopcion_dark_mode_pct
FROM
  `talent-intelligence-career-tic.analytics_tic.events_*`
GROUP BY
  dispositivo
ORDER BY
  total_sesiones DESC;
```

#### 📊 Resultado Real en BigQuery:
| Dispositivo | Total Sesiones | Prefieren Español | Prefieren Inglés | Prefieren Modo Oscuro | Prefieren Modo Claro | % Adopción Dark Mode |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 💻 **Desktop** | **3** | 2 | 1 | 3 | 0 | **100.0%** |
| 📱 **Mobile** | **3** | 2 | 1 | 1 | 2 | **33.3%** |

> **Insight de Negocio:** El 100% de los reclutadores que navegan desde computadoras de escritorio prefieren el tema oscuro (*Dark Mode*), mientras que en dispositivos móviles existe mayor equilibrio visual.

---

### 4. Embudo Limpio para Looker Studio (Exclusión de Crawlers & Datacenters)
* **Archivo:** [`04_vw_looker_studio_clean_funnel.sql`](04_vw_looker_studio_clean_funnel.sql)
* **Objetivo:** Excluir analíticamente datacenters identificados (Microsoft Azure, AWS, GCP: Boydton, Dulles, Ashburn, Council Bluffs, Boardman) y computar sesiones humanas únicas con su tasa de conversión real.

#### Consulta SQL:
```sql
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
```

---

## 🚀 Cómo ejecutar estas consultas en Google Cloud

1. Ingresar a [Google Cloud Console - BigQuery Studio](https://console.cloud.google.com/bigquery?project=talent-intelligence-career-tic).
2. Asegurarse de tener seleccionado el proyecto **`talent-intelligence-career-tic`**.
3. Hacer clic en **`+` (Redactar consulta nueva)**.
4. Pegar el código SQL de cualquiera de los archivos `.sql` y hacer clic en **Ejecutar** (*Run*).
