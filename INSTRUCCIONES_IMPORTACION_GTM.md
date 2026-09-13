# 🏷️ Guía de 1 Clic: Importar la Telemetría de CV Ejecutivo Inteligente en Google Tag Manager

Ya tienes generado en la carpeta del proyecto el archivo oficial de configuración maestro:
📁 **`gtm_cv_inteligente_container.json`**

Este archivo contiene:
- ✅ **1 Etiqueta de Configuración de Google Analytics 4 (GA4):** Vinculada a tu ID `G-NQC5PHY67R`.
- ✅ **7 Etiquetas de Eventos de GA4:**
  1. `cv_kpi_interaction` (Mide clics en los 4 KPIs).
  2. `cv_cert_filter` (Mide uso de filtros de certificaciones: Power BI, IA, SQL, etc.).
  3. `cv_document_download` (Mide descargas del CV en PDF).
  4. `cv_scroll_depth` (Mide profundidad de lectura al 25%, 50%, 75% y 100%).
  5. `cv_theme_toggle` (Mide cambios entre Modo Oscuro y Claro).
  6. `cv_language_switch` (Mide cambios entre Español e Inglés).
  7. `cv_external_click` (Mide clics a LinkedIn, GitHub, WhatsApp, Email).
- ✅ **7 Activadores (Triggers) de Eventos Personalizados.**
- ✅ **13 Variables de Capa de Datos (Data Layer Variables)** para capturar parámetros de métricas.

---

## 🚀 Pasos para Importar en GTM (Tarda 15 segundos):

1. Entrá a tu contenedor en **[tagmanager.google.com](https://tagmanager.google.com/)** (`GTM-P2Z4TZ4Z`).
2. En la barra superior, hacé clic en la pestaña **Administración** (al lado de *Espacio de trabajo*).
3. En la columna de la derecha (*Contenedor*), hacé clic en **Importar contenedor**.
4. En **Seleccionar archivo de contenedor**, hacé clic en **Elegir archivo** y seleccioná el archivo `gtm_cv_inteligente_container.json` que está en tu carpeta de descargas (`CV_html`).
5. En **Elegir espacio de trabajo**:
   - Marcá **Existente** (*Existing*) ➔ hacé clic en **Default Workspace**.
6. En **Elegir opción de importación**:
   - Marcá **Combinar** (*Merge*) ➔ y seleccioná **Sobrescribir las etiquetas, activadores y variables conflictivos** (o *Overwrite*).
7. Verás en pantalla el resumen con las **8 etiquetas, 7 activadores y 13 variables**.
8. Hacé clic en el botón azul **Confirmar** (abajo a la izquierda).
9. Por último, arriba a la derecha, hacé clic en el botón azul **Enviar** ➔ **Publicar** ➔ **Continuar** (omitiendo descripción).

---

## 🎉 ¡Listo!
A partir de ese momento, cada persona que entre a tu CV en vivo ([https://rubenbarrios-bigdata.github.io/cv-ejecutivo-inteligente/](https://rubenbarrios-bigdata.github.io/cv-ejecutivo-inteligente/)) y haga clic en un KPI, descargue el PDF o use los filtros, enviará los eventos en tiempo real directo a tu panel de **Google Analytics 4** (`G-NQC5PHY67R`).
