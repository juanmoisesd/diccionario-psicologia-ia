# Guía de contribución

¡Gracias por tu interés en contribuir al Diccionario de Psicología en Español para IA!

---

## Cómo contribuir

### 1. Añadir o corregir términos

1. Haz un fork del repositorio.
2. Crea una rama descriptiva: `git checkout -b add/termino-autoeficacia`
3. Edita `data/terms.jsonl` siguiendo el esquema en `data/schema.json`.
4. Valida tu contribución:
   ```bash
   python scripts/validate_dataset.py --input data/terms.jsonl --schema data/schema.json
   ```
5. Abre un Pull Request con una descripción clara de los cambios.

### 2. Reportar errores

Usa el sistema de Issues de GitHub con la etiqueta `error-definicion` o `error-referencia`.

### 3. Proponer nuevas áreas o campos

Abre un Issue con la etiqueta `propuesta` y descripción detallada de la motivación.

---

## Estándares de calidad

Toda contribución debe cumplir:

- **Fuentes verificables**: Mínimo una referencia con DOI o URL estable.
- **Formato correcto**: Todos los campos obligatorios del esquema deben estar presentes.
- **Sin duplicados**: Verificar que el `term_id` y el `termino` no existan ya en el dataset.
- **Nivel de confianza**: Asignar A, B o C según la rúbrica en `governance/evidence-rubric.md`.
- **Neutralidad**: Las definiciones deben ser descriptivas, no prescriptivas ni valorativas.

---

## Licencia

[CC BY 4.0](LICENSE)