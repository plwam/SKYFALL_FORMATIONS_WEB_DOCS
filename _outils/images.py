# -*- coding: utf-8 -*-
"""Generation des illustrations du module Django / GesiBiblio."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Polygon, Ellipse
from matplotlib.lines import Line2D

OUT = r"D:\smarta\gesi formation\module-django-gesibiblio\images"
os.makedirs(OUT, exist_ok=True)

NAVY = "#1F3A5F"
NAVY2 = "#2E5077"
TEAL = "#2A9D8F"
TEAL_L = "#D9F0EC"
AMBER = "#E9C46A"
AMBER_L = "#FCF3D9"
CORAL = "#E76F51"
CORAL_L = "#FBE3DD"
GREY = "#5C677D"
GREY_L = "#EDF0F4"
WHITE = "#FFFFFF"
PURPLE = "#6D597A"
GREEN = "#2D6A4F"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["svg.fonttype"] = "none"


def new_fig(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax


def box(ax, x, y, w, h, text="", fc=WHITE, ec=NAVY, tc=NAVY, fs=11,
        bold=False, lw=1.4, r=0.9, ls="-", va="center", ha="center", z=3):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0.02,rounding_size={r}",
                       fc=fc, ec=ec, lw=lw, linestyle=ls, zorder=z)
    ax.add_patch(p)
    if text:
        ax.text(x + w / 2 if ha == "center" else x + 0.6,
                y + h / 2 if va == "center" else y + h - 0.8,
                text, ha=ha, va=va, color=tc, fontsize=fs,
                fontweight="bold" if bold else "normal", zorder=z + 1,
                linespacing=1.35)
    return p


def arrow(ax, p1, p2, color=GREY, lw=1.7, rad=0.0, ls="-", style="-|>",
          ms=13, z=4, shrinkA=1, shrinkB=1):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms,
                        color=color, lw=lw, linestyle=ls,
                        connectionstyle=f"arc3,rad={rad}", zorder=z,
                        shrinkA=shrinkA, shrinkB=shrinkB)
    ax.add_patch(a)


def label(ax, x, y, text, fs=9, color=GREY, bg=WHITE, bold=False, ha="center", va="center"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs, color=color,
            fontweight="bold" if bold else "normal", zorder=6,
            bbox=dict(boxstyle="round,pad=0.22", fc=bg, ec="none", alpha=0.95))


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=230, bbox_inches="tight", pad_inches=0.12,
                facecolor=WHITE)
    plt.close(fig)
    print("ecrit", path)


# ---------------------------------------------------------------------
# 1. Architecture MVT
# ---------------------------------------------------------------------
def mvt():
    fig, ax = new_fig(11.2, 6.2)
    box(ax, 2, 38, 18, 16, "Navigateur\nrequête HTTP", fc=AMBER_L, ec=AMBER, fs=10.5, bold=True)
    box(ax, 24, 12, 68, 82, "", fc="#FBFCFD", ec=TEAL, lw=1.2, ls=(0, (5, 4)), r=1.2)
    ax.text(26, 91, "Django", color=TEAL, fontsize=12, fontweight="bold", va="top")

    box(ax, 28, 72, 24, 12, "URLconf\nurls.py", fc=TEAL_L, ec=TEAL, fs=10.2)
    box(ax, 28, 46, 24, 12, "Vue\nviews.py", fc=NAVY, ec=NAVY, tc=WHITE, fs=10.2, bold=True)
    box(ax, 28, 20, 24, 12, "Gabarit\ntemplates/", fc="#F1E9F5", ec=PURPLE, tc=PURPLE, fs=10.2)
    box(ax, 60, 72, 26, 12, "Modèle\nmodels.py", fc=TEAL_L, ec=TEAL, fs=10.2)
    box(ax, 60, 44, 26, 12, "Base de données\nSQLite", fc=GREY_L, ec=GREY, fs=10)

    arrow(ax, (20, 48), (28, 76), rad=-0.15, color=NAVY)
    label(ax, 22, 64, "1. requête", fs=8.5)
    arrow(ax, (40, 72), (40, 58), color=NAVY)
    label(ax, 46, 66, "2. routage", fs=8.5)
    arrow(ax, (52, 54), (60, 76), rad=0.12, color=NAVY)
    label(ax, 54, 61, "3. données", fs=8.5)
    arrow(ax, (73, 72), (73, 56), color=TEAL, lw=1.6)
    label(ax, 79, 64, "4. ORM", fs=8.5, color=TEAL)
    arrow(ax, (40, 46), (40, 32), color=PURPLE, lw=1.6)
    label(ax, 47, 41, "5. contexte", fs=8.5, color=PURPLE)
    arrow(ax, (44, 32), (44, 46), color=PURPLE, lw=1.4, ls=(0, (3, 2)))
    label(ax, 35, 37, "HTML", fs=8.5, color=PURPLE)
    arrow(ax, (28, 48), (20, 46), color=GREEN, lw=1.5, ls=(0, (4, 2)))
    label(ax, 23, 42, "6. réponse", fs=8.5, color=GREEN)
    save(fig, "mvt.png")


# ---------------------------------------------------------------------
# 2. Heritage des gabarits
# ---------------------------------------------------------------------
def heritage():
    fig, ax = new_fig(10.8, 5.4)
    # base
    box(ax, 30, 68, 44, 20, "", fc=NAVY, ec=NAVY)
    ax.text(52, 84.5, "base.html", color=WHITE, fontsize=13, fontweight="bold", ha="center")
    ax.text(52, 81, "squelette commun : en-tête, navigation, pied de page",
            color="#DCE6F0", fontsize=7.8, ha="center")
    for i, (txt, col) in enumerate([("block titre", AMBER), ("block contenu", TEAL), ("block pied", CORAL)]):
        box(ax, 33 + i * 13.5, 70.5, 12.5, 5, txt, fc=col, ec=col, tc=NAVY if col == AMBER else WHITE, fs=7.8, r=0.4)

    # enfants
    kids = [("accueil.html", 4, 26), ("livre_liste.html", 37, 28), ("livre_detail.html", 72, 24)]
    for name, x, w in kids:
        box(ax, x, 30, w, 13, name, fc=TEAL_L, ec=TEAL, fs=10, bold=True)
        ax.text(x + w / 2, 33.5, "étend base.html", color=GREY, fontsize=7.5, ha="center")
        arrow(ax, (x + w / 2, 43), (52, 68), rad=0.0, color=TEAL, lw=1.3)
    label(ax, 24, 58, "extends", fs=9, color=TEAL, bold=True)
    label(ax, 64, 57, "extends", fs=9, color=TEAL, bold=True)

    # partials
    box(ax, 3, 62, 21, 12, "partials/\nnavbar.html", fc=AMBER_L, ec=AMBER, fs=8.8)
    arrow(ax, (24, 68), (30, 74), color=AMBER, lw=1.4, ls=(0, (3, 2)))
    label(ax, 26, 72.5, "include", fs=8, color="#B08968")
    box(ax, 80, 62, 17, 12, "partials/\nfooter.html", fc=AMBER_L, ec=AMBER, fs=8.8)
    arrow(ax, (80, 68), (74, 72), color=AMBER, lw=1.4, ls=(0, (3, 2)))
    label(ax, 78, 72.5, "include", fs=8, color="#B08968")
    save(fig, "heritage.png")


# ---------------------------------------------------------------------
# 3. Diagramme entite association
# ---------------------------------------------------------------------
def entity(ax, x, y, w, h, title, fields, color=TEAL, title_fs=10.2, field_fs=7.9):
    box(ax, x, y, w, h, "", fc=WHITE, ec=color, lw=1.3, r=0.7)
    hh = 5.2
    p = FancyBboxPatch((x, y + h - hh), w, hh,
                       boxstyle="round,pad=0.02,rounding_size=0.7",
                       fc=color, ec=color, lw=1.3, zorder=3)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h - hh / 2, title, ha="center", va="center",
            color=WHITE, fontsize=title_fs, fontweight="bold", zorder=4)
    ty = y + h - hh - 2.0
    for f in fields:
        ax.text(x + 1.2, ty, f, ha="left", va="center", fontsize=field_fs,
                color=NAVY, zorder=4, family="DejaVu Sans Mono")
        ty -= 2.05


def modele_bdd():
    fig, ax = new_fig(12.6, 6.6)
    entity(ax, 2, 62, 26, 30, "Auteur", [
        "id  PK", "prenom", "nom", "biographie", "date_naissance",
    ], color=TEAL)
    entity(ax, 2, 22, 26, 28, "Categorie", [
        "id  PK", "nom  unique", "slug  unique", "description",
    ], color=PURPLE)
    entity(ax, 39, 38, 30, 52, "Livre", [
        "id  PK", "titre", "slug  unique", "isbn  unique",
        "auteur_id  FK", "editeur", "annee_publication",
        "nombre_exemplaires", "statut", "couverture",
    ], color=NAVY, title_fs=11)
    entity(ax, 80, 46, 18, 40, "Emprunt", [
        "id  PK", "livre_id  FK", "membre_id  FK",
        "date_emprunt", "date_retour_prevue", "date_retour",
    ], color=CORAL, title_fs=10)
    entity(ax, 80, 12, 18, 26, "Membre", [
        "id  PK", "user_id  FK", "numero", "telephone", "actif",
    ], color=AMBER, title_fs=10)

    # Auteur 1..N Livre
    arrow(ax, (28, 77), (39, 77), color=GREY, lw=1.4, style="-")
    arrow(ax, (39, 77), (39, 77), color=GREY, lw=1.4, style="-|>", ms=11)
    label(ax, 33.5, 79.5, "1", fs=8.5, bold=True)
    label(ax, 37, 74.5, "N", fs=8.5, bold=True)

    # Categorie N..N Livre (pointilles)
    arrow(ax, (28, 36), (39, 50), color=PURPLE, lw=1.4, style="-", ls=(0, (3, 2)))
    label(ax, 31, 39, "N", fs=8.5, bold=True, color=PURPLE)
    label(ax, 36, 48, "N", fs=8.5, bold=True, color=PURPLE)
    label(ax, 31.5, 44.5, "M2M", fs=7.5, color=PURPLE)

    # Livre 1..N Emprunt
    arrow(ax, (69, 66), (80, 66), color=GREY, lw=1.4, style="-")
    label(ax, 72, 68.5, "1", fs=8.5, bold=True)
    label(ax, 77.5, 63.5, "N", fs=8.5, bold=True)

    # Membre 1..N Emprunt
    arrow(ax, (89, 38), (89, 46), color=GREY, lw=1.4, style="-")
    label(ax, 86.5, 41, "1", fs=8.5, bold=True)
    label(ax, 91.5, 43.5, "N", fs=8.5, bold=True)

    ax.text(50, 6, "Les clés étrangères sont matérialisées par les champs auteur_id, livre_id, membre_id et user_id.",
            ha="center", fontsize=8.2, color=GREY, style="italic")
    save(fig, "modele_bdd.png")


# ---------------------------------------------------------------------
# 4. Cycle d'un emprunt
# ---------------------------------------------------------------------
def cycle_emprunt():
    fig, ax = new_fig(10.6, 4.6)
    box(ax, 4, 58, 26, 22, "DISPONIBLE", fc=TEAL_L, ec=TEAL, tc=GREEN, fs=11, bold=True)
    ax.text(17, 64, "exemplaires > 0", ha="center", fontsize=7.8, color=GREY)
    box(ax, 38, 58, 26, 22, "EMPRUNTÉ", fc=AMBER_L, ec=AMBER, tc="#8A6D1F", fs=11, bold=True)
    ax.text(51, 64, "date_retour vide", ha="center", fontsize=7.8, color=GREY)
    box(ax, 74, 58, 24, 22, "PERDU", fc=GREY_L, ec=GREY, tc=GREY, fs=11, bold=True)

    arrow(ax, (30, 69), (38, 69), color=GREEN, lw=1.8)
    label(ax, 34, 73, "emprunter()", fs=8.2, color=GREEN, bold=True)
    arrow(ax, (38, 63), (30, 63), color=TEAL, lw=1.8)
    label(ax, 34, 59, "retourner()", fs=8.2, color=TEAL, bold=True)
    arrow(ax, (64, 63), (74, 63), color=CORAL, lw=1.8)
    label(ax, 69, 68, "déclarer perdu", fs=8.2, color=CORAL, bold=True)

    box(ax, 32, 14, 38, 24, "", fc="#FFF8F6", ec=CORAL, ls=(0, (4, 3)))
    ax.text(51, 33, "Retard", ha="center", fontsize=10.5, fontweight="bold", color=CORAL)
    ax.text(51, 27, "date_retour_prevue < aujourd'hui\net date_retour vide", ha="center",
            fontsize=8.2, color=NAVY, linespacing=1.4)
    ax.text(51, 19.5, "est_en_retard = True", ha="center", fontsize=8.2,
            color=CORAL, family="DejaVu Sans Mono")
    arrow(ax, (51, 58), (51, 38), color=CORAL, lw=1.4, ls=(0, (3, 2)))
    label(ax, 56, 48, "calculé à l'affichage", fs=7.8, color=CORAL)
    save(fig, "cycle_emprunt.png")


# ---------------------------------------------------------------------
# 5. Roles et permissions
# ---------------------------------------------------------------------
def permissions():
    fig, ax = new_fig(11.4, 5.2)
    roles = [
        ("Visiteur\nanonyme", "Consulter le catalogue", GREY_L, GREY),
        ("Lecteur\nconnecté", "Voir ses emprunts", TEAL_L, TEAL),
        ("Bibliothécaire\ngroupe", "Gérer livres et emprunts", AMBER_L, AMBER),
        ("Administrateur\nsuperuser", "Gérer utilisateurs et droits", "#F1E9F5", PURPLE),
    ]
    x0, w, gap = 2, 21, 4.5
    for i, (t, cap, fc, ec) in enumerate(roles):
        x = x0 + i * (w + gap)
        box(ax, x, 50, w, 22, t, fc=fc, ec=ec, fs=9.6, bold=True,
            tc=NAVY if ec != GREY else GREY)
        ax.text(x + w / 2, 42, cap, ha="center", va="top", fontsize=7.6, color=GREY,
                wrap=True)
        if i < 3:
            arrow(ax, (x + w, 61), (x + w + gap, 61), color=NAVY, lw=1.6)
    labels = ["connexion", "groupe ajouté", "is_superuser"]
    for i, txt in enumerate(labels):
        x = x0 + i * (w + gap) + w + gap / 2
        label(ax, x, 66, txt, fs=7.4, color=NAVY, bold=True)
    ax.text(51, 22, "Les droits sont vérifiés côté serveur, jamais uniquement dans le gabarit.",
            ha="center", fontsize=8.8, color=CORAL, style="italic")
    save(fig, "permissions.png")


# ---------------------------------------------------------------------
# 6. Maquette de l'administration
# ---------------------------------------------------------------------
def admin_mockup():
    fig, ax = new_fig(11.4, 6.4)
    # fenetre
    box(ax, 2, 4, 96, 92, "", fc=WHITE, ec=GREY, lw=1.2, r=1.2)
    ax.add_patch(Rectangle((2, 88), 96, 8, fc="#E9EDF2", ec="none", zorder=3))
    for i, c in enumerate(["#E76F51", "#E9C46A", "#2A9D8F"]):
        ax.add_patch(Circle((6 + i * 3, 92), 0.9, fc=c, ec="none", zorder=4))
    box(ax, 17, 89.5, 62, 5, "127.0.0.1:8000/admin/catalogue/livre/", fc=WHITE, ec=GREY_L, fs=7.2, r=0.4)
    # sidebar
    ax.add_patch(Rectangle((2, 4), 26, 84, fc=NAVY, ec="none", zorder=3))
    ax.text(15, 82, "GESIBIBLIO", color=WHITE, fontsize=10.5, fontweight="bold", ha="center", zorder=4)
    ax.text(15, 78, "Administration", color="#AFC3D8", fontsize=7.4, ha="center", zorder=4)
    items = ["Livres", "Auteurs", "Catégories", "Membres", "Emprunts"]
    for i, it in enumerate(items):
        yy = 68 - i * 7
        if i == 0:
            ax.add_patch(Rectangle((4, yy - 2.4), 22, 5, fc=TEAL, ec="none", zorder=4))
        ax.text(6, yy, it, color=WHITE, fontsize=8.2, va="center", zorder=5)
    # contenu
    ax.text(32, 80, "Livres", color=NAVY, fontsize=15, fontweight="bold", zorder=4)
    ax.text(32, 76.5, "Accueil  >  Catalogue  >  Livres", color=GREY, fontsize=6.8, zorder=4)
    box(ax, 78, 76, 16, 5, "+ Ajouter livre", fc=TEAL, ec=TEAL, tc=WHITE, fs=7.4, r=0.5)
    # entete tableau
    ax.add_patch(Rectangle((32, 68), 62, 5, fc="#E9EDF2", ec="none", zorder=3))
    heads = [("Titre", 33), ("Auteur", 55), ("Statut", 72), ("Ex.", 81), ("", 87)]
    for h, x in heads:
        ax.text(x, 70.5, h, color=NAVY, fontsize=7.2, fontweight="bold", zorder=4)
    rows = [
        ("Le Petit Prince", "Saint-Exupéry", "Disponible", "3"),
        ("Une si longue lettre", "Mariama Bâ", "Emprunté", "1"),
        ("L'Étranger", "Albert Camus", "Disponible", "2"),
        ("Le Monde s'effondre", "Chinua Achebe", "Disponible", "1"),
        ("Crépuscule des temps", "A. Kourouma", "Réservé", "2"),
    ]
    for i, (t, a, s, n) in enumerate(rows):
        yy = 63 - i * 6.4
        if i % 2 == 0:
            ax.add_patch(Rectangle((32, yy - 2.2), 62, 6.4, fc="#F8FAFC", ec="none", zorder=3))
        ax.text(33, yy, t, color=NAVY, fontsize=7.1, va="center", zorder=4)
        ax.text(55, yy, a, color=GREY, fontsize=7.1, va="center", zorder=4)
        col = GREEN if s == "Disponible" else (CORAL if s == "Emprunté" else "#8A6D1F")
        ax.text(72, yy, s, color=col, fontsize=6.9, va="center", fontweight="bold", zorder=4)
        ax.text(82, yy, n, color=NAVY, fontsize=7.1, va="center", zorder=4)
    save(fig, "admin_mockup.png")


# ---------------------------------------------------------------------
# 7. Architecture de deploiement
# ---------------------------------------------------------------------
def deploiement():
    fig, ax = new_fig(11.0, 4.4)
    box(ax, 2, 48, 18, 24, "Navigateur\n(HTTPS)", fc=AMBER_L, ec=AMBER, fs=9.2, bold=True)
    box(ax, 27, 48, 20, 24, "Nginx\nreverse proxy", fc=TEAL_L, ec=TEAL, fs=9.2, bold=True)
    box(ax, 54, 48, 20, 24, "Gunicorn\nworkers", fc="#F1E9F5", ec=PURPLE, fs=9.2, bold=True)
    box(ax, 81, 48, 17, 24, "Django\nGesiBiblio", fc=NAVY, ec=NAVY, tc=WHITE, fs=9.2, bold=True)
    box(ax, 54, 14, 20, 18, "PostgreSQL", fc=GREY_L, ec=GREY, fs=9.2, bold=True)
    box(ax, 27, 14, 20, 18, "Fichiers statiques\net media", fc=WHITE, ec=TEAL, fs=8.4)
    arrow(ax, (20, 60), (27, 60), color=NAVY, lw=1.7)
    arrow(ax, (47, 60), (54, 60), color=NAVY, lw=1.7)
    arrow(ax, (74, 60), (81, 60), color=NAVY, lw=1.7)
    arrow(ax, (89, 48), (64, 32), color=TEAL, lw=1.5, rad=-0.05)
    label(ax, 79, 38, "ORM", fs=8, color=TEAL)
    arrow(ax, (37, 48), (37, 32), color=TEAL, lw=1.5, ls=(0, (3, 2)))
    label(ax, 42, 40, "sert /static\net /media", fs=7.4, color=TEAL)
    save(fig, "deploiement.png")


# ---------------------------------------------------------------------
# 8. Arborescence compacte
# ---------------------------------------------------------------------
def arborescence():
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


if __name__ == "__main__":
    mvt()
    heritage()
    modele_bdd()
    cycle_emprunt()
    permissions()
    admin_mockup()
    deploiement()
    arborescence()
