---
# ══════════════════════════════════════════════════════════════
# PLANTILLA SEO — TÉRMINO DEL DICCIONARIO DE PSICOLOGÍA
# Versión con conexión DSM-5-TR y CIE-11
#
# Instrucciones:
#   1. Copia con el nombre del slug: ansiedad.md, memoria.md
#   2. Rellena TODOS los campos obligatorios (*)
#   3. Los campos dsm5tr y cie11 solo si aplican al término
#   4. El H1 lo genera el layout automáticamente desde `termino`
# ══════════════════════════════════════════════════════════════

layout: term

# ── IDENTIFICACIÓN (*) ──────────────────────────────────────
term_id:   "PSY-000000"           # * ID único estable (nunca reutilizar)
termino:   "NOMBRE DEL TÉRMINO"   # * Término exacto en español → genera H1
slug:      "nombre-del-termino"   # * URL amigable: lowercase, sin tildes, guiones

# ── CATEGORIZACIÓN (*) ──────────────────────────────────────
area: "Psicología clínica"
# Valores válidos:
#   Psicología clínica | Psicología cognitiva | Psicología social
#   Psicología del desarrollo | Neuropsicología | Psicoanálisis
#   Psicometría | Psicología conductual | Psicología humanista
#   Psicología educativa | Psicología de la salud | Psicobiología
#   Psicología forense | Psicología organizacional
#   Psicología positiva | General

# ── SEO META (*) ────────────────────────────────────────────
description: >
  Qué es [TÉRMINO] en psicología: definición técnica, clasificación DSM-5-TR
  y CIE-11, ejemplo clínico y referencias APA 7 verificadas.
# REGLA: 130-160 caracteres. Incluir: término + "psicología" + DSM o CIE si aplica.

image: "/assets/img/terms/nombre-del-termino.png"  # OG image 1200×630 px

# ── DEFINICIONES (*) ────────────────────────────────────────
definicion_corta: >
  Definición de 1-2 oraciones (máx. 250 caracteres). Directa y sin rodeos.
  Ej.: "La ansiedad es un estado emocional de aprensión ante amenazas percibidas."

definicion_tecnica: >
  Definición técnica completa (100-400 palabras). Incluir:
  origen del concepto, autores clave, mecanismo, clasificaciones,
  aplicaciones clínicas y estado actual del debate científico.

ejemplo: >
  Ejemplo concreto en contexto clínico, experimental o teórico.
  Describir un caso o situación observable.

# ── CONEXIÓN CON DSM-5-TR ────────────────────────────────────
dsm5tr:
  aplica: true
  categoria: "Trastornos de ansiedad"
  codigo: "300.00 (F41.9)"
  criterios_resumen: >
    Resumen breve de los criterios diagnósticos del DSM-5-TR
    (no reproducir literalmente; parafrasear y citar).
  nota_dsm: >
    Observación clínica o contextual relevante sobre la clasificación DSM.
  referencia_dsm: >
    American Psychiatric Association. (2022).
    Diagnostic and statistical manual of mental disorders (5th ed., text rev.).
    https://doi.org/10.1176/appi.books.9780890425787

# ── CONEXIÓN CON CIE-11 ──────────────────────────────────────
cie11:
  aplica: true
  capitulo: "06 Trastornos mentales, del comportamiento o del neurodesarrollo"
  codigo: "6B00"
  nombre_cie: "Trastorno de ansiedad generalizada"
  descripcion_cie: >
    Descripción breve de la entidad CIE-11 (parafrasear, no copiar literalmente).
  url_cie: "https://icd.who.int/browse/2024-01/mms/es#XXXXXXX"
  referencia_cie: >
    World Health Organization. (2019). International classification of diseases,
    eleventh revision (ICD-11). https://icd.who.int/

# ── RELACIONES SEMÁNTICAS ────────────────────────────────────
no_confundir_con:
  - "Término parecido 1"
  - "Término parecido 2"

relaciones:
  - "Término relacionado 1"
  - "Término relacionado 2"
  - "Término relacionado 3"

# ── CALIDAD EDITORIAL (*) ────────────────────────────────────
nivel_confianza: "A"

fuentes:
  - "Apellido, N. (año). *Título*. Editorial. https://doi.org/XXXXX"
  - "Apellido, N. (año). Título. *Revista*, vol(n), pp. https://doi.org/XXXXX"

# ── VERSIÓN (*) ──────────────────────────────────────────────
version:         "1.0.0"
fecha_revision:  "2026-03-28"
---

<!-- ══════════════════════════════════════════════════════
     CONTENIDO ADICIONAL OPCIONAL
     El layout genera automáticamente todas las secciones.
     Usa este espacio solo para tablas, figuras o notas extra.
     ══════════════════════════════════════════════════════ -->
