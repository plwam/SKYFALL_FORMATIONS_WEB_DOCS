# -*- coding: utf-8 -*-
"""Verifie l'equilibre des environnements LaTeX et signale les problemes."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:\smarta\gesi formation\module-django-gesibiblio")
FILES = [ROOT / "main.tex", ROOT / "preamble.tex"]
FILES += sorted((ROOT / "pages").glob("*.tex"))
FILES += sorted((ROOT / "chapitres").glob("*.tex"))
FILES += sorted((ROOT / "annexes").glob("*.tex"))

problems = 0
for path in FILES:
    if path.name.startswith("_test"):
        continue
    text = path.read_text(encoding="utf-8")
    # retirer les commentaires
    text = re.sub(r"(?<!\\)%.*", "", text)
    begins = Counter(re.findall(r"\\begin\{([^}]+)\}", text))
    ends = Counter(re.findall(r"\\end\{([^}]+)\}", text))
    for env in set(begins) | set(ends):
        if begins[env] != ends[env]:
            print(f"{path.name}: environnement {env} : "
                  f"{begins[env]} begin, {ends[env]} end")
            problems += 1
    # accolades : les listings sont exclus du comptage
    cleaned = re.sub(
        r"\\begin\{(?:codebox|terminal)\}(?:\[[^\]]*\])?(?:\{[^\n]*\})?"
        r".*?\\end\{(?:codebox|terminal)\}",
        "", text, flags=re.S,
    )
    cleaned = re.sub(r"\\[{}]", "", cleaned)
    depth = 0
    line = 1
    for ch in cleaned:
        if ch == "\n":
            line += 1
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                print(f"{path.name}: accolade fermante en trop vers la ligne {line}")
                problems += 1
                depth = 0
    if depth:
        print(f"{path.name}: {depth} accolade(s) non fermee(s)")
        problems += 1

print("Problemes detectes :", problems)
