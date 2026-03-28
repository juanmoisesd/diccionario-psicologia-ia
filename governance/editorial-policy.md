# Política editorial

## Principios generales

El Diccionario de Psicología en Español para IA se rige por los siguientes principios:

1. **Verificabilidad**: toda definición debe respaldarse con al menos una fuente primaria o secundaria con DOI o URL estable verificable.
2. **Neutralidad descriptiva**: las definiciones describen el uso técnico del término en la literatura; no prescriben ni valoran.
3. **Pluralismo teórico**: cuando existen teorías en competencia, se documenta la diversidad teórica con atribución a sus autores.
4. **Estabilidad de identificadores**: los `term_id` son permanentes. Un término eliminado nunca tiene su ID reutilizado.
5. **Transparencia de cambios**: todo cambio en definiciones, fuentes o campos se registra en el `CHANGELOG.md`.

---

## Criterios de inclusión

Un término se incluye si:
- Es un concepto técnico o clínico de la psicología académica o aplicada.
- Aparece en al menos una publicación revisada por pares o en un manual diagnóstico reconocido (DSM, CIE).
- Puede definirse de forma informativa para un modelo de lenguaje (NLP) sin ambigüedad fundamental.

Un término se excluye si:
- Es un neologismo no consolidado sin base empírica publicada.
- Es exclusivamente del lenguaje coloquial sin uso técnico documentado.
- Su inclusión implicaría sesgo político, ideológico o de género no respaldado por consenso científico.

---

## Niveles de confianza

| Nivel | Criterio |
|---|---|
| **A** | Fuentes primarias verificadas con DOI; definición validada por revisión editorial interna |
| **B** | Fuentes secundarias (manuales, libros de texto reconocidos) sin DOI disponible; definición revisada |
| **C** | Fuente disponible pero no verificada; o término en proceso de revisión editorial |

---

## Proceso de aprobación de nuevos términos

1. Propuesta vía Pull Request en GitHub con todos los campos del esquema completos.
2. Revisión editorial: verificación de fuentes, redacción y ausencia de duplicados.
3. Asignación de `term_id` secuencial (nunca reutilizar IDs).
4. Merge aprobado por al menos un miembro del equipo editorial.
5. Registro en `CHANGELOG.md` en el próximo release.

---

## Política de correcciones

- **Errores menores** (tipografías, formato): corrección inmediata, patch release.
- **Errores en definición** (imprecisiones, omisiones): corrección con nota en CHANGELOG, minor patch.
- **Errores en fuentes** (cita incorrecta, DOI roto): corrección urgente con verificación, patch release.
- **Cambios de esquema**: requieren major release y documentación de migración.

---

## Idioma y estilo

- Español estándar académico (sin variantes regionales marcadas).
- Terminología APA 7 para referencias.
- Definiciones técnicas: registro formal, sin coloquialismos.
- Definiciones cortas: accesibles para no especialistas.
