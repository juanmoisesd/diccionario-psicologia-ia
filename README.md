# Diccionario de Psicología en Español para IA

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19297225.svg)](https://doi.org/10.5281/zenodo.19297225)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow)](https://huggingface.co/datasets/juanmoisesdelas/diccionario-psicologia-es)

Dataset léxico-conceptual de psicología en español, diseñado para entrenamiento y fine-tuning de modelos de lenguaje (LLMs/NLP). Contiene **3,002 términos únicos** con 12 campos estructurados, cubriendo 18 áreas de la psicología.

**Autor:** Dr. Juan Moisés de la Serna · ORCID: [0000-0002-8401-8018](https://orcid.org/0000-0002-8401-8018) · [juanmoisesdelaserna.es](https://juanmoisesdelaserna.es/) · UNIR

**DOI:** [10.5281/zenodo.19297225](https://doi.org/10.5281/zenodo.19297225) · **Licencia:** CC BY 4.0

---

## Estadísticas del dataset (v2.0.0)

| Métrica | Valor |
|---|---|
| Términos únicos | 3,002 |
| Áreas de psicología | 18 |
| Campos por término | 12 |
| Formato principal | JSONL |
| Formato alternativo | CSV |
| Idioma | Español |
| Versión | 2.0.0 |
| Última actualización | 2026-03-29 |

## Áreas cubiertas

| Código | Área | Términos |
|---|---|---|
| CLI | Psicología Clínica | ~167 |
| COG | Psicología Cognitiva | ~167 |
| NEU | Neuropsicología | ~167 |
| DES | Psicología del Desarrollo | ~167 |
| SOC | Psicología Social | ~167 |
| BIO | Psicobiología | ~167 |
| MET | Metodología de Investigación | ~167 |
| PER | Psicología de la Personalidad | ~167 |
| TER | Psicoterapia | ~167 |
| EDU | Psicología Educativa | ~167 |
| ORG | Psicología Organizacional | ~167 |
| FOR | Psicología Forense | ~167 |
| SAL | Psicología de la Salud | ~167 |
| FAR | Psicofarmacología | ~167 |
| INV | Investigación Psicológica | ~167 |
| GEN | Psicología General | ~167 |
| POS | Psicología Positiva | ~167 |
| COM | Psicología Comunitaria | ~166 |

## Estructura de datos (12 campos)

Cada término incluye los siguientes campos:

| Campo | Tipo | Descripción |
|---|---|---|
| `term_id` | string | Identificador único (PSY-00001 a PSY-03002) |
| `termino` | string | Nombre del término en español |
| `area` | string | Área de psicología |
| `definicion_corta` | string | Definición breve del término |
| `definicion_tecnica` | string | Definición técnica extendida |
| `ejemplo` | string | Ejemplo de uso clínico/aplicado |
| `no_confundir_con` | string | Términos similares que pueden confundirse |
| `relaciones` | array | Términos semánticamente relacionados |
| `nivel_confianza` | string | Nivel de confianza de la definición |
| `fuentes` | array | Referencias bibliográficas (APA 7) |
| `version` | string | Versión del registro |
| `fecha_revision` | string | Fecha de última revisión (ISO 8601) |

## Archivos

```
data/
├── terms.jsonl          # Dataset principal (3,002 términos, ~1.8 MB)
├── terms.csv            # Formato tabular (3,002 términos, ~1.3 MB)
├── quality_flags.jsonl  # Flags de calidad
└── schema.json          # Esquema JSON del dataset
```

## Ejemplo de uso

```json
{
  "term_id": "PSY-00001",
  "termino": "Depresión mayor",
  "area": "Psicología Clínica",
  "definicion_corta": "Trastorno del estado de ánimo con tristeza persistente y pérdida de interés",
  "definicion_tecnica": "Desde la perspectiva clínica, trastorno del estado de ánimo...",
  "ejemplo": "Un paciente presenta depresión mayor y requiere evaluación clínica...",
  "no_confundir_con": "",
  "relaciones": [],
  "nivel_confianza": "alto",
  "fuentes": ["APA (2022). DSM-5-TR.", "Beck (2011). Cognitive Therapy."],
  "version": "2.0.0",
  "fecha_revision": "2026-03-29"
}
```

## Cómo cargar el dataset

### Python
```python
from datasets import load_dataset
ds = load_dataset("juanmoisesdelas/diccionario-psicologia-es")
```

### Python (JSONL directo)
```python
import json
with open("data/terms.jsonl", "r", encoding="utf-8") as f:
    terms = [json.loads(line) for line in f if line.strip()]
print(f"Total términos: {len(terms)}")
```

## Citación

```bibtex
@dataset{delaserna2026diccionario,
  author       = {De la Serna, Juan Moisés},
  title        = {Diccionario de Psicología en Español para IA},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19297225},
  url          = {https://doi.org/10.5281/zenodo.19297225},
  version      = {2.0.0},
  license      = {CC-BY-4.0}
}
```

## Licencia

Este dataset se distribuye bajo la licencia [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Usted es libre de compartir y adaptar el material, siempre que se otorgue la atribución apropiada al autor.

## Plataformas de distribución

- **GitHub:** [juanmoisesd/diccionario-psicologia-ia](https://github.com/juanmoisesd/diccionario-psicologia-ia)
- **Hugging Face:** [juanmoisesdelas/diccionario-psicologia-es](https://huggingface.co/datasets/juanmoisesdelas/diccionario-psicologia-es)
- **OSF:** [osf.io/83wvp](https://osf.io/83wvp/)
- **Zenodo:** [DOI 10.5281/zenodo.19297225](https://doi.org/10.5281/zenodo.19297225)

## Contacto

Dr. Juan Moisés de la Serna — [juanmoisesdelaserna.es](https://juanmoisesdelaserna.es/) — UNIR
