#!/usr/bin/env python3
"""
generate_terms_template.py — Genera plantillas JSONL vacías.
Uso: python scripts/generate_terms_template.py --count 500 --output data/terms_batch.jsonl
"""
import argparse, json, os
from datetime import date

TEMPLATE = {
    "term_id": "", "termino": "COMPLETAR",
    "area": "COMPLETAR — ver lista de áreas válidas",
    "definicion_corta": "COMPLETAR — 1-2 oraciones, máx. 300 caracteres",
    "definicion_tecnica": "COMPLETAR — definición técnica completa",
    "ejemplo": "COMPLETAR — ejemplo de uso clínico o teórico",
    "no_confundir_con": ["COMPLETAR"], "relaciones": ["COMPLETAR"],
    "nivel_confianza": "C",
    "fuentes": ["COMPLETAR — Apellido, N. (año). Título. https://doi.org/XXXXX"],
    "version": "1.0.0", "fecha_revision": str(date.today()),
}

def get_last_id(path):
    if not os.path.exists(path): return 0
    last = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                entry = json.loads(line)
                tid = entry.get("term_id", "")
                if tid.startswith("PSY-"):
                    last = max(last, int(tid.replace("PSY-", "")))
            except (json.JSONDecodeError, ValueError): pass
    return last

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--output", default="data/terms_template.jsonl")
    parser.add_argument("--start-id", type=int, default=None)
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.output) if os.path.dirname(args.output) else ".", exist_ok=True)
    start = args.start_id if args.start_id is not None else get_last_id(args.output) + 1
    print(f"Generando {args.count} plantillas desde PSY-{start:06d}...")
    with open(args.output, "w", encoding="utf-8") as f:
        for i in range(args.count):
            e = {**TEMPLATE, "term_id": f"PSY-{start+i:06d}",
                 "no_confundir_con": ["COMPLETAR"], "relaciones": ["COMPLETAR"],
                 "fuentes": ["COMPLETAR — Apellido, N. (año). https://doi.org/XXXXX"]}
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"Listo. IDs: PSY-{start:06d} — PSY-{start+args.count-1:06d}")

if __name__ == "__main__":
    main()
