# -*- coding: utf-8 -*-
"""Convertit le module LaTeX en une version texte lisible."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"D:\smarta\gesi formation\module-django-gesibiblio")
OUT = Path(r"D:\smarta\gesi formation\Module_Django_GesiBiblio.txt")

FILES = [
    "pages/avant-propos.tex",
    "chapitres/00-introduction.tex",
    "chapitres/01-structure-projet.tex",
    "chapitres/02-creation-app.tex",
    "chapitres/03-gabarits.tex",
    "chapitres/04-fichiers-statiques.tex",
    "chapitres/05-balises-filtres.tex",
    "chapitres/06-modeles.tex",
    "chapitres/07-requetes.tex",
    "chapitres/08-admin.tex",
    "chapitres/09-formulaires.tex",
    "chapitres/10-authentification.tex",
    "chapitres/11-permissions.tex",
    "chapitres/12-conclusion.tex",
    "annexes/A-installation.tex",
    "annexes/B-aide-memoire.tex",
    "annexes/C-erreurs-frequentes.tex",
    "annexes/D-donnees-demonstration.tex",
]

ACCENTS = [
    (r"\\'e", "é"), (r"\\`e", "è"), (r"\\^e", "ê"), (r'\\"e', "ë"),
    (r"\\'E", "É"), (r"\\`E", "È"), (r"\\^E", "Ê"),
    (r"\\`a", "à"), (r"\\^a", "â"), (r'\\"a', "ä"),
    (r"\\^i", "î"), (r'\\"i', "ï"), (r"\\^o", "ô"), (r'\\"o', "ö"),
    (r"\\`u", "ù"), (r"\\^u", "û"), (r"\\c c", "ç"), (r"\\c C", "Ç"),
    (r"\\~n", "ñ"), (r"\\oe", "oe"), (r"\\OE", "OE"),
    (r"\\og", "«"), (r"\\fg", "»"), (r"\\ldots", "..."),
    (r"\\%", "%"), (r"\\&", "&"), (r"\\_", "_"), (r"\\#", "#"),
    (r"\\\$", "$"), (r"\\{", "{"), (r"\\}", "}"),
]

ENV_LABELS = {
    "retenir": "A RETENIR",
    "bonne": "BONNE PRATIQUE",
    "attention": "ATTENTION",
    "piege": "ERREUR FREQUENTE",
    "note": "NOTE",
    "correction": "CORRECTION",
}


def find_command(text: str, name: str) -> list[tuple[int, int, str]]:
    """Retourne (debut, fin, contenu) pour chaque \\name{...}."""
    results = []
    for m in re.finditer(r"\\" + re.escape(name) + r"\{", text):
        start = m.start()
        i = m.end()
        depth = 1
        while i < len(text) and depth:
            if text[i] == "\\":
                i += 2
                continue
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        if depth == 0:
            results.append((start, i, text[m.end():i - 1]))
    return results


def inline(text: str) -> str:
    text = re.sub(r"\\href\{([^{}]*)\}\{([^{}]*)\}", r"\2 (\1)", text)
    text = re.sub(r"\\url\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:code|texttt|fichier)\{((?:\\[{}]|[^{}])*)\}",
                  r"`\1`", text)
    text = re.sub(r"\\(?:textbf|textit|emph|textsf|underline)\{((?:\\[{}]|[^{}])*)\}",
                  r"\1", text)
    text = text.replace("\\gesibiblio", "GesiBiblio")
    text = text.replace("\\django", "Django")
    text = text.replace("\\cle", "")
    for pattern, replacement in ACCENTS:
        text = re.sub(pattern, replacement, text)
    text = re.sub(r"\\label\{[^{}]*\}", "", text)
    text = re.sub(r"\\index\{[^{}]*\}", "", text)
    text = re.sub(r"\\vspace\*?\{[^{}]*\}", "", text)
    text = re.sub(r"\\addcontentsline\{[^{}]*\}\{[^{}]*\}\{[^{}]*\}",
                  "", text)
    text = re.sub(r"\\markboth\{[^{}]*\}\{[^{}]*\}", "", text)
    text = text.replace("\\quad", " ").replace("\\,", " ")
    text = text.replace("~", " ")
    text = text.replace("---", "-")
    text = text.replace("\\\\", " ")
    text = re.sub(r"\\(?:begin|end)\{[^{}]*\}", "", text)
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    text = re.sub(r"\{\}", "", text)
    return text


def clean_text_block(text: str) -> str:
    lines = []
    for raw in text.splitlines():
        line = inline(raw)
        line = line.replace("&", " | ")
        line = re.sub(r"\\\\\s*$", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def convert_table(block: str) -> str:
    rows = []
    for raw in block.splitlines():
        s = raw.strip()
        if not s:
            continue
        if re.match(r"\\(?:toprule|midrule|bottomrule|centering|small|"
                    r"begin\{tabularx\}|end\{tabularx\}|begin\{longtable\}|"
                    r"end\{longtable\})", s):
            continue
        if s.startswith("\\caption"):
            cap = re.search(r"\\caption\{((?:[^{}]|\{[^{}]*\})*)\}", s)
            if cap:
                rows.append("")
                rows.append("Tableau : " + inline(cap.group(1)))
            continue
        if s.startswith("\\label"):
            continue
        line = inline(s)
        line = line.replace("&", " | ")
        line = re.sub(r"\\\\\s*$", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            rows.append(line)
    return "\n".join(rows)


def convert_figure(block: str) -> str:
    cap = re.search(r"\\caption\{((?:[^{}]|\{[^{}]*\})*)\}", block, re.S)
    title = inline(cap.group(1)) if cap else "Illustration"
    title = re.sub(r"\s+", " ", title).strip()
    return "\n[FIGURE] " + title + "\n"


def convert_list_block(lines: list[str], start: int) -> tuple[str, int]:
    """Convertit un itemize/enumerate/description jusqu'a sa fin."""
    out = []
    depth = 1
    ordered = "enumerate" in lines[start]
    desc = "description" in lines[start]
    counter = 0
    i = start + 1
    while i < len(lines):
        s = lines[i].strip()
        if re.match(r"\\begin\{(?:itemize|enumerate|description)\}", s):
            depth += 1
            sub, i = convert_list_block(lines, i)
            out.append(sub)
            continue
        if re.match(r"\\end\{(?:itemize|enumerate|description)\}", s):
            depth -= 1
            i += 1
            if depth == 0:
                break
            continue
        if s.startswith("\\item"):
            counter += 1
            item = s[5:].strip()
            label = ""
            m = re.match(r"\[([^\]]*)\](.*)", item)
            if m:
                label = inline(m.group(1)).strip()
                item = m.group(2).strip()
            if label:
                out.append("  - " + label + " : " + inline(item))
            elif ordered:
                out.append(f"  {counter}. " + inline(item))
            else:
                out.append("  - " + inline(item))
            i += 1
            continue
        if s and not re.match(
            r"\\(?:begin|end|item|caption|label|toprule|midrule|bottomrule)",
            s,
        ):
            out.append("    " + inline(s))
        i += 1
    return "\n".join(out), i


def convert_file(path: Path, chapter_no: list[int], appendix: list[bool]) -> str:
    text = path.read_text(encoding="utf-8")

    # Supprimer les commentaires LaTeX sans toucher au contenu des listings.
    lignes = []
    dans_code = False
    for ligne in text.splitlines():
        if re.search(r"\\begin\{(?:codebox|terminal)\}", ligne):
            dans_code = True
        if not dans_code:
            ligne = re.sub(r"(?<!\\)%.*", "", ligne)
        lignes.append(ligne)
        if re.search(r"\\end\{(?:codebox|terminal)\}", ligne):
            dans_code = False
    text = "\n".join(lignes)

    # Extraire les resumes avant le traitement ligne a ligne.
    summaries = []
    for start, end, content in reversed(find_command(text, "chapitreresume")):
        summaries.append(inline(re.sub(r"\s+", " ", content)).strip())
        text = text[:start] + "\n[[RESUME]]\n" + text[end:]
    summaries.reverse()

    lines = text.splitlines()
    out: list[str] = []
    i = 0
    resume_index = 0
    list_stack: list[str] = []

    while i < len(lines):
        raw = lines[i]
        s = raw.strip()

        if s == "[[RESUME]]":
            if resume_index < len(summaries):
                out.append("")
                out.append(summaries[resume_index])
                out.append("")
                resume_index += 1
            i += 1
            continue

        m = re.match(r"\\chapter\*?\{(.*)\}", s)
        if m:
            title = inline(m.group(1)).strip()
            if title.lower().startswith("avant-propos"):
                label = "AVANT-PROPOS"
            elif appendix[0]:
                letter = chr(ord("A") + chapter_no[0])
                label = f"ANNEXE {letter} : {title}"
                chapter_no[0] += 1
            else:
                chapter_no[0] += 1
                label = f"CHAPITRE {chapter_no[0]} : {title}"
            out.extend(["", "", "=" * 78, label.upper(), "=" * 78, ""])
            i += 1
            continue

        m = re.match(r"\\(section|subsection|subsubsection)\*?\{(.*)\}", s)
        if m:
            level, title = m.group(1), inline(m.group(2)).strip()
            prefix = {"section": "\n## ", "subsection": "\n### ",
                      "subsubsection": "\n#### "}[level]
            out.extend(["", prefix + title, ""])
            i += 1
            continue

        if re.match(r"\\begin\{codebox\}", s):
            m = re.match(r"\\begin\{codebox\}\[[^\]]*\]\{(.*)\}", s)
            title = inline(m.group(1)) if m else "Code"
            body = []
            i += 1
            while i < len(lines) and "\\end{codebox}" not in lines[i]:
                body.append(lines[i].rstrip())
                i += 1
            out.extend(["", "-" * 78, f"CODE : {title}", "-" * 78])
            out.extend(body)
            out.extend(["-" * 78, ""])
            i += 1
            continue

        if re.match(r"\\begin\{terminal\}", s):
            body = []
            i += 1
            while i < len(lines) and "\\end{terminal}" not in lines[i]:
                body.append(lines[i].rstrip())
                i += 1
            out.extend(["", "TERMINAL :"])
            out.extend(["  $ " + b for b in body if b.strip()])
            out.append("")
            i += 1
            continue

        if s.startswith("\\begin{table}") or s.startswith("\\begin{longtable}"):
            env = "table" if s.startswith("\\begin{table}") else "longtable"
            body = []
            i += 1
            while i < len(lines) and f"\\end{{{env}}}" not in lines[i]:
                body.append(lines[i])
                i += 1
            out.extend(["", convert_table("\n".join(body)), ""])
            i += 1
            continue

        if s.startswith("\\begin{figure}"):
            body = []
            i += 1
            while i < len(lines) and "\\end{figure}" not in lines[i]:
                body.append(lines[i])
                i += 1
            out.append(convert_figure("\n".join(body)))
            i += 1
            continue

        if re.match(r"\\begin\{objectifs\}", s):
            out.extend(["", "OBJECTIFS DU CHAPITRE", ""])
            i += 1
            continue

        if re.match(r"\\begin\{exercice\}", s):
            m = re.match(r"\\begin\{exercice\}\[(.*)\]", s)
            extra = inline(m.group(1)).strip() if m else ""
            out.extend(["", "=" * 60,
                        f"EXERCICE {extra}".strip(), "=" * 60, ""])
            i += 1
            continue

        env_match = re.match(r"\\begin\{(retenir|bonne|attention|piege|note|correction)\}", s)
        if env_match:
            label = ENV_LABELS[env_match.group(1)]
            out.extend(["", f"[{label}]", ""])
            i += 1
            continue

        end_match = re.match(r"\\end\{(retenir|bonne|attention|piege|note|correction)\}", s)
        if end_match:
            label = ENV_LABELS[end_match.group(1)]
            out.extend(["", f"[/{label}]", ""])
            i += 1
            continue

        if re.match(r"\\begin\{(itemize|enumerate|description)\}", s):
            block, i = convert_list_block(lines, i)
            out.append("")
            out.append(block)
            out.append("")
            continue

        if re.match(r"\\(begin|end)\{", s):
            i += 1
            continue

        if s.startswith("\\item"):
            out.append(inline(s))
            i += 1
            continue

        if s.startswith("\\includegraphics"):
            i += 1
            continue

        if s in ("\\frontmatter", "\\mainmatter", "\\backmatter",
                 "\\appendix", "\\tableofcontents", "\\end{document}"):
            if s == "\\appendix":
                appendix[0] = True
                chapter_no[0] = 0
            i += 1
            continue

        line = inline(raw).strip()
        if line:
            out.append(line)
        elif out and out[-1] != "":
            out.append("")
        i += 1

    return "\n".join(out)


def main() -> None:
    parts = []
    header = [
        "=" * 78,
        "INITIATION AU DÉVELOPPEMENT WEB AVEC DJANGO",
        "Projet fil rouge : GesiBiblio",
        "",
        "Auteur : LWANZO PATERNE",
        "Formation propulsée par GESITECHNOLOGIES",
        "Durée : 48 heures de formation guidée",
        "",
        "Version texte du module. Le document complet, mis en page avec les",
        "illustrations et le code coloré, se trouve dans le fichier PDF.",
        "=" * 78,
    ]
    parts.append("\n".join(header))
    chapter_no = [0]
    appendix = [False]
    for rel in FILES:
        path = ROOT / rel
        if rel.startswith("annexes/") and not appendix[0]:
            appendix[0] = True
            chapter_no[0] = 0
        parts.append(convert_file(path, chapter_no, appendix))
    parts.append("\n\nFIN DU MODULE\n")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Ecrit : {OUT} ({OUT.stat().st_size} octets)")


if __name__ == "__main__":
    main()
