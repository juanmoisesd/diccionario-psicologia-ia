# Historial de cambios

Todos los cambios notables de este proyecto se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/)
y el versionado sigue [Semantic Versioning](https://semver.org/lang/es/).

---

## [Unreleased]

### Pendiente
- Expansión a 7,000 términos (Mes 2)
- Publicación en Hugging Face Datasets
- Espejo en OSF

---

## [1.0.0] — 2026-03-28

### Añadido
- Estructura completa del repositorio
- 3,000 términos iniciales revisados con nivel de confianza A o B
- Esquema JSON formal (`data/schema.json`)
- Dataset en formato JSONL y CSV
- GitHub Pages con índice alfabético
- Política editorial y rúbrica de evidencia
- Scripts de automatización (generación, validación, exportación, build docs)
- GitHub Actions para CI/CD
- Integración con Zenodo para DOI automático por release
- Formatos de cita: APA 7, BibTeX, IEEE

### DOI
`10.5281/zenodo.19297225`

---

## Formatos de versionado

- **Patch** (x.x.N): correcciones de errores en definiciones o metadatos
- **Minor** (x.N.0): adición de nuevos términos sin cambios de esquema
- **Major** (N.0.0): cambios de esquema o reestructuración del dataset