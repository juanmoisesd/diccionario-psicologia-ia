---
# ══════════════════════════════════════════════════════════════════
# PLANTILLA — TÉRMINO DIAGNÓSTICO
# Para términos con clasificación en DSM-5-TR y/o CIE-11.
# Ejemplos: Depresión, Ansiedad, TEPT, Esquizofrenia, TDAH, TOC...
#
# Autor del diccionario: Dr. Juan Moisés de la Serna
# Web: https://juanmoisesdelaserna.es/
# ORCID: https://orcid.org/0000-0002-8401-8018
# ══════════════════════════════════════════════════════════════════

layout: term-diagnostico
tipo_termino: diagnostico

term_id:  "PSY-000000"
termino:  "NOMBRE DEL TRASTORNO"
slug:     "nombre-del-trastorno"
area:     "Psicología clínica"

description: >
  Qué es [TRASTORNO] según el DSM-5-TR y la CIE-11: criterios diagnósticos,
  evolución histórica, diagnóstico diferencial y referencias APA 7.
  Diccionario de psicología editado por el Dr. Juan Moisés de la Serna — juanmoisesdelaserna.es

definicion_corta: >
  Definición breve (máx. 250 caracteres). Directa y sin rodeos.

definicion_tecnica: >
  Definición técnica completa (100-400 palabras): origen, autores clave,
  mecanismo, clasificaciones actuales, aplicaciones clínicas.

ejemplo: >
  Caso clínico o situación concreta que ilustra la presentación típica.

evolucion_diagnostica:

  - manual: "DSM-I"
    anio: 1952
    codigo: ""
    descripcion: >
      Describir cómo se contemplaba este cuadro en el DSM-I (1952).
    nota: ""

  - manual: "DSM-5-TR"
    anio: 2022
    codigo: ""
    descripcion: >
      DSM-5-TR (2022): actualización del texto, nuevos especificadores,
      datos de prevalencia actualizados. Estado actual.
    nota: ""

  - manual: "CIE-11"
    anio: 2022
    codigo: ""
    descripcion: >
      CIE-11 (OMS, vigente 2022): cambios respecto a CIE-10.
      Nuevo código alfanumérico, nuevas especificaciones.
    nota: ""

dsm5tr:
  aplica: true
  categoria: "COMPLETAR — ej.: Trastornos depresivos"
  codigo: "COMPLETAR — ej.: 296.20 (F32.0)"
  criterios_resumen: >
    Paráfrasis de los criterios A, B, C, D... del DSM-5-TR.
    No reproducir literalmente. Mínimo 80 palabras.
  especificadores: >
    Listar los especificadores relevantes del trastorno.
  prevalencia: "COMPLETAR — dato de prevalencia según DSM-5-TR."
  nota_dsm: >
    Observación clínica relevante o cambio en la edición texto revisado.
  referencia_dsm: >
    American Psychiatric Association. (2022). Diagnostic and statistical
    manual of mental disorders (5th ed., text rev.).
    https://doi.org/10.1176/appi.books.9780890425787

cie11:
  aplica: true
  capitulo: "COMPLETAR — ej.: 06 Trastornos mentales, del comportamiento o del neurodesarrollo"
  codigo: "COMPLETAR — ej.: 6A70"
  nombre_cie: "COMPLETAR — nombre oficial en CIE-11 en español"
  descripcion_cie: >
    Paráfrasis de la descripción CIE-11. No copiar literalmente.
  nota_cie: >
    Diferencias clave respecto a la CIE-10 o respecto al DSM-5-TR.
  url_cie: "https://icd.who.int/browse/2024-01/mms/es#XXXXXXX"
  referencia_cie: >
    World Health Organization. (2019). International classification of
    diseases, eleventh revision (ICD-11). https://icd.who.int/

criterios_comparados:
  - dimension: "Código"
    dsm: "COMPLETAR"
    cie: "COMPLETAR"

  - dimension: "Nombre oficial"
    dsm: "COMPLETAR"
    cie: "COMPLETAR"

diagnostico_diferencial:
  - termino: "Trastorno relacionado 1"
    diferencia: >
      Descripción de la diferencia principal con este trastorno.
    clave_diferencial: "Elemento clave para diferenciar ambos."

no_confundir_con:
  - "Término parecido 1"
  - "Término parecido 2"

relaciones:
  - "Término relacionado 1"
  - "Término relacionado 2"

nivel_confianza: "A"

fuentes:
  - "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787"
  - "World Health Organization. (2019). International classification of diseases, eleventh revision (ICD-11). https://icd.who.int/"
  - "COMPLETAR — referencia adicional con DOI"

version:         "1.0.0"
fecha_revision:  "2026-03-28"
---
