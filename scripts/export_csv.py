#!/usr/bin/env python3
"""
export_csv.py — Exporta el dataset JSONL a CSV.
Uso: python scripts/export_csv.py --input data/terms.jsonl --output data/terms.csv
"""
import argparse, csv, json, sys
from pathlib import Path

DEFAULT_FIELDS = ["term_id","termino","area","definicion_corta","definicion_tecnica",
                  "ejemplo","no_confundir_con","relaciones","nivel_confianza","fuentes","version","fecha_revision"]

def load_jsonl(path):
    entries = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try: entries.append(json.loads(line))
                except json.JSONDecodeError as e: print(f"  WARN línea {i}: {e}", file=sys.stderr)
    return entries

def flatten(value):
    if isinstance(value, list): return " | ".join(str(v) for v in value)
    return str(value) if value is not None else ""

def main():
    parser = argparse.ArgumentParser(description="Exporta JSONL a CSV.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--fields", default=None)
    args = parser.parse_args()
    fields = [f.strip() for f in args.fields.split(",")] if args.fields else DEFAULT_FIELDS
    entries = load_jsonl(args.input)
    if not entries:
        print("ERROR: dataset vacío."); sys.exit(1)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for e in entries:
            w.writerow({field: flatten(e.get(field, "")) for field in fields})
    print(f"OK: {len(entries)} términos exportados a '{args.output}'")

if __name__ == "__main__":
    main()
