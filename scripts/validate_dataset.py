#!/usr/bin/env python3
"""
validate_dataset.py
Valida el dataset JSONL contra el esquema JSON y detecta duplicados.

Uso:
    python scripts/validate_dataset.py --input data/terms.jsonl --schema data/schema.json
    python scripts/validate_dataset.py --input data/terms.jsonl --schema data/schema.json --strict
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("ERROR: Instala jsonschema con: pip install jsonschema")
    sys.exit(1)


def load_jsonl(path: str) -> list[dict]:
    entries = []
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entries.append((lineno, json.loads(line)))
            except json.JSONDecodeError as e:
                print(f"  ERROR línea {lineno}: JSON inválido — {e}")
    return entries


def load_schema(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_entries(entries: list[tuple], schema: dict, strict: bool = False) -> tuple[int, int]:
    errors = 0
    warnings = 0
    term_ids = defaultdict(list)
    terminos = defaultdict(list)

    print(f"\nValidando {len(entries)} entradas...\n")

    for lineno, entry in entries:
        term_id = entry.get("term_id", f"(sin ID, línea {lineno})")
        try:
            validate(instance=entry, schema=schema)
        except ValidationError as e:
            print(f"  [ERROR] {term_id} (línea {lineno}): {e.message}")
            errors += 1

        for field, value in entry.items():
            if isinstance(value, str) and "COMPLETAR" in value:
                print(f"  [WARN]  {term_id} (línea {lineno}): campo '{field}' sin completar")
                warnings += 1

        fuentes = entry.get("fuentes", [])
        if not fuentes:
            print(f"  [ERROR] {term_id}: 'fuentes' vacío")
            errors += 1

        term_ids[term_id].append(lineno)
        termino = entry.get("termino", "").strip().lower()
        if termino:
            terminos[termino].append(lineno)

    for tid, lines in term_ids.items():
        if len(lines) > 1:
            print(f"  [ERROR] term_id duplicado '{tid}' en líneas: {lines}")
            errors += 1

    for termino, lines in terminos.items():
        if len(lines) > 1:
            if strict:
                print(f"  [ERROR] término duplicado '{termino}' en líneas: {lines}")
                errors += 1
            else:
                print(f"  [WARN]  término duplicado '{termino}' en líneas: {lines}")
                warnings += 1

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Valida el dataset JSONL de psicología.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    schema = load_schema(args.schema)
    entries = load_jsonl(args.input)
    errors, warnings = validate_entries(entries, schema, strict=args.strict)

    print(f"\n{'='*50}")
    print(f"Total: {len(entries)} | Errores: {errors} | Advertencias: {warnings}")
    print(f"{'='*50}")
    if errors > 0:
        print(f"\nFALLO: {errors} error(es). Corrígelos antes de publicar.")
        sys.exit(1)
    else:
        print("\nOK: Validación completada sin errores.")


if __name__ == "__main__":
    main()
