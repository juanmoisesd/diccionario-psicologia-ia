---
layout: default
title: "Diccionario de Psicología en Español para IA"
---

# Diccionario de Psicología en Español

**3,002 términos** estructurados para inteligencia artificial y modelos de lenguaje.

Autor: **Dr. Juan Moisés de la Serna** · ORCID [0000-0002-8401-8018](https://orcid.org/0000-0002-8401-8018) · UNIR

---

## Áreas temáticas

| Código | Área |
|--------|------|
| CLI | Psicología Clínica |
| COG | Psicología Cognitiva |
| NEU | Neuropsicología |
| DES | Psicología del Desarrollo |
| SOC | Psicología Social |
| BIO | Psicología Biológica |
| MET | Metodología |
| PER | Personalidad |
| TER | Terapias |
| EDU | Psicología Educativa |
| ORG | Psicología Organizacional |
| FOR | Psicología Forense |
| SAL | Psicología de la Salud |
| FAR | Psicofarmacología |
| INV | Investigación |
| GEN | Psicología General |
| POS | Psicología Positiva |
| COM | Psicología Comunitaria |

## Navegar términos

{% assign sorted = site.terminos | sort: "title" %}
{% assign letters = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z" | split: "," %}

{% for letter in letters %}
### {{ letter }}
<ul>
{% for t in sorted %}
{% assign first = t.title | slice: 0 | upcase %}
{% if first == letter %}
<li><a href="{{ t.url | relative_url }}">{{ t.title }}</a> <small>({{ t.area }})</small></li>
{% endif %}
{% endfor %}
</ul>
{% endfor %}

---

Licencia: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
