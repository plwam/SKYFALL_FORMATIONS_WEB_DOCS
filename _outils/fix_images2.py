p = r'D:\smarta\gesi formation\_outils\images.py'
s = open(p, encoding='utf-8').read()
start = s.index('def mvt():')
end = s.index('# ---------------------------------------------------------------------\n# 2. Heritage')
new = '''def mvt():
    fig, ax = new_fig(11.2, 6.2)
    box(ax, 2, 38, 18, 16, "Navigateur\\nrequête HTTP", fc=AMBER_L, ec=AMBER, fs=10.5, bold=True)
    box(ax, 24, 6, 68, 88, "", fc="#FBFCFD", ec=TEAL, lw=1.2, ls=(0, (5, 4)), r=1.2)
    ax.text(26, 91, "Django", color=TEAL, fontsize=12, fontweight="bold", va="top")

    box(ax, 28, 72, 24, 12, "URLconf\\nurls.py", fc=TEAL_L, ec=TEAL, fs=10.2)
    box(ax, 28, 46, 24, 12, "Vue\\nviews.py", fc=NAVY, ec=NAVY, tc=WHITE, fs=10.2, bold=True)
    box(ax, 28, 20, 24, 12, "Gabarit\\ntemplates/", fc="#F1E9F5", ec=PURPLE, tc=PURPLE, fs=10.2)
    box(ax, 60, 72, 26, 12, "Modèle\\nmodels.py", fc=TEAL_L, ec=TEAL, fs=10.2)
    box(ax, 60, 44, 26, 12, "Base de données\\nSQLite", fc=GREY_L, ec=GREY, fs=10)

    arrow(ax, (20, 48), (28, 76), rad=-0.15, color=NAVY)
    label(ax, 22, 64, "1. requête", fs=8.5)
    arrow(ax, (40, 72), (40, 58), color=NAVY)
    label(ax, 46, 66, "2. routage", fs=8.5)
    arrow(ax, (52, 54), (60, 76), rad=0.12, color=NAVY)
    label(ax, 55, 64, "3. données", fs=8.5)
    arrow(ax, (73, 72), (73, 56), color=TEAL, lw=1.6)
    label(ax, 79, 64, "4. ORM", fs=8.5, color=TEAL)
    arrow(ax, (40, 46), (40, 32), color=PURPLE, lw=1.6)
    label(ax, 46, 39, "5. contexte", fs=8.5, color=PURPLE)
    arrow(ax, (44, 32), (44, 46), color=PURPLE, lw=1.4, ls=(0, (3, 2)))
    label(ax, 48, 38, "HTML", fs=8.5, color=PURPLE)
    arrow(ax, (28, 48), (20, 46), color=GREEN, lw=1.5, ls=(0, (4, 2)))
    label(ax, 23, 42, "6. réponse", fs=8.5, color=GREEN)
    save(fig, "mvt.png")


'''
s = s[:start] + new + s[end:]

# arborescence compacte
start = s.index('def arborescence():')
end = s.index('if __name__ == "__main__":')
new2 = '''def arborescence():
    lines = [
        ("gesibiblio/", TEAL),
        ("├── manage.py", NAVY),
        ("├── gesibiblio/", TEAL),
        ("│   ├── settings.py", NAVY),
        ("│   ├── urls.py", NAVY),
        ("│   └── wsgi.py", NAVY),
        ("├── catalogue/", TEAL),
        ("│   ├── models.py", NAVY),
        ("│   ├── views.py", NAVY),
        ("│   └── urls.py", NAVY),
        ("├── templates/", PURPLE),
        ("├── static/", "#B08968"),
        ("└── media/", GREY),
    ]
    fig, ax = new_fig(7.6, 6.6)
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 100)
    box(ax, 2, 2, 96, 96, "", fc="#FBFCFD", ec=GREY_L, lw=1.0, r=1.0)
    y = 92
    for txt, col in lines:
        ax.text(6, y, txt, ha="left", va="top", fontsize=12,
                color=col, family="DejaVu Sans Mono",
                fontweight="bold" if txt.rstrip().endswith("/") else "normal")
        y -= 6.6
    save(fig, "arborescence.png")


'''
s = s[:start] + new2 + s[end:]

# cycle : decaler Perdu et le label
s = s.replace('box(ax, 72, 58, 24, 22, "PERDU"', 'box(ax, 74, 58, 24, 22, "PERDU"')
s = s.replace('arrow(ax, (64, 63), (72, 63)', 'arrow(ax, (64, 63), (74, 63)')
s = s.replace('label(ax, 68, 59, "déclarer perdu"', 'label(ax, 69, 68, "déclarer perdu"')
open(p,'w',encoding='utf-8').write(s)
print('ok')
