#!/usr/bin/env python3
"""
build_docs_index.py — Genera páginas Markdown por término para GitHub Pages.
Uso: python scripts/build_docs_index.py --input data/terms.jsonl --output docs/terminos
"""
import argparse, json, os, re, sys
from collections import defaultdict
from datetime import date
from pathlib import Path

def slugify(text):
    text = text.lower().strip()
    for src, dst in {"á":"a","é":"e","í":"i","ó":"o","ú":"u","ü":"u","ñ":"n"}.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")

def load_jsonl(path):
    entries = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try: entries.append(json.loads(line))
                except: pass
    return entries

def render_page(entry, base_url=""):
    t = entry.get("termino","")
    tid = entry.get("term_id","")
    area = entry.get("area","")
    nc = "\n".join(f"- {x}" for x in entry.get("no_confundir_con",[])) or "_(ninguno)_"
    rel = "\n".join(f"- {x}" for x in entry.get("relaciones",[])) or "_(ninguno)_"
    fts = "\n".join(f"- {x}" for x in entry.get("fuentes",[])) or "_(sin fuentes)_"
    return f"""---
layout: term
title: {t} — Diccionario de Psicología en Español
description: "{entry.get('definicion_corta','')}"
term_id: {tid}
area: {area}
nivel_confianza: {entry.get('nivel_confianza','C')}
---

# {t}

**ID**: {tid} | **Área**: {area} | **Confianza**: {entry.get('nivel_confianza','C')}

## Definición breve

{entry.get('definicion_corta','')}

## Definición técnica

{entry.get('definicion_tecnica','')}

## Ejemplo

{entry.get('ejemplo','')}

## No confundir con

{nc}

## Términos relacionados

{rel}

## Fuentes

{fts}

---

*Última revisión: {entry.get('fecha_revision', str(date.today()))}*
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-url", default="")
    args = parser.parse_args()
    entries = load_jsonl(args.input)
    if not entries:
        print("ERROR: dataset vacío."); sys.exit(1)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for e in entries:
        t = e.get("termino","")
        if not t or t == "COMPLETAR": continue
        (out / f"{slugify(t)}.md").write_text(render_page(e, args.base_url), encoding="utf-8")
        n += 1
    print(f"OK: {n} páginas generadas en '{args.output}'")

if __name__ == "__main__":
    main()
