# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"D:\smarta\gesi formation\module-django-gesibiblio\annexes\C-erreurs-frequentes.tex")
t = p.read_text(encoding="utf-8")

pairs = [
    (
        "\\code{ModuleNotFoundError: No module named 'django'} & Environnement virtuel\n"
        "inactif ou Django absent.",
        "\\code{ModuleNotFoundError} & Django absent de l'environnement virtuel\n"
        "ou environnement inactif.",
    ),
    (
        "\\code{No installed app with label 'catalogue'} & Application absente de\n"
        "\\code{INSTALLED\\_APPS}. & Ajoutez \\code{\"catalogue\"} ou\n"
        "\\code{\"catalogue.apps.CatalogueConfig\"}.",
        "\\code{No installed app} & Le label \\code{catalogue} est inconnu :\n"
        "application absente de \\code{INSTALLED\\_APPS}. & Ajoutez\n"
        "\\code{\"catalogue\"} dans les réglages, ou \\code{CatalogueConfig}\n"
        "dans \\code{apps.py}.",
    ),
    (
        "\\code{ModuleNotFoundError: catalogue} & Dossier mal placé ou\n"
        "\\code{\\_\\_init\\_\\_.py} absent.",
        "\\code{ModuleNotFoundError} & Le paquet \\code{catalogue} est\n"
        "introuvable : dossier mal placé ou \\code{\\_\\_init\\_\\_.py} absent.",
    ),
    (
        "\\code{ImproperlyConfigured: SECRET\\_KEY} & Clé absente ou vide.",
        "\\code{ImproperlyConfigured} & Clé \\code{SECRET\\_KEY} absente ou vide.",
    ),
    (
        "\\code{Error: That port is already in use} & Un serveur tourne déjà.",
        "Port déjà utilisé & Un serveur tourne déjà.",
    ),
    (
        "\\code{ImportError: cannot import name 'X'} & Import circulaire ou nom inexistant.",
        "\\code{ImportError} & Import circulaire ou nom \\code{X} inexistant.",
    ),
    (
        "\\code{TypeError: view must be callable} & Une classe est passée sans\n"
        "\\code{.as\\_view()}.",
        "\\code{TypeError} & Une classe de vue est passée sans\n"
        "\\code{.as\\_view()}.",
    ),
    (
        "\\code{AttributeError: module has no attribute 'urls'} & \\code{include} pointe vers\n"
        "un module sans \\code{urlpatterns}.",
        "\\code{AttributeError} & \\code{include} pointe vers un module sans\n"
        "\\code{urlpatterns}.",
    ),
    (
        "\\code{403 CSRF verification failed} & Jeton absent ou cookie bloqué.",
        "\\code{CSRF verification failed} & Jeton absent ou cookie bloqué\n"
        "(erreur 403).",
    ),
    (
        "\\code{TemplateSyntaxError: Unclosed tag} & \\code{\\{\\% if \\%\\}} sans\n"
        "\\code{\\{\\% endif \\%\\}}.",
        "\\code{TemplateSyntaxError} & Balise non fermée, par exemple\n"
        "\\code{\\{\\% if \\%\\}} sans \\code{\\{\\% endif \\%\\}}.",
    ),
    (
        "\\code{IntegrityError: FOREIGN KEY constraint failed} & Clé étrangère invalide.",
        "\\code{IntegrityError} & Clé étrangère invalide (contrainte\n"
        "\\code{FOREIGN KEY}).",
    ),
    (
        "\\code{cleaned\\_data.get(\"champ\")}. \\\\",
        "\\code{cleaned\\_data.get}. \\\\",
    ),
    (
        "\\code{ValueError: invalid literal for int()} & Conversion d'une chaîne non\n"
        "numérique.",
        "\\code{ValueError} & Conversion d'une chaîne non numérique en entier.",
    ),
    (
        "\\code{RelatedObjectDoesNotExist: user.membre} & Profil non créé.",
        "\\code{RelatedObjectDoesNotExist} & Profil membre absent pour\n"
        "\\code{user} (relation un à un).",
    ),
    (
        "\\code{Please enter a correct username and password} & Identifiants invalides ou\n"
        "compte inactif.",
        "Identifiants refusés & Nom d'utilisateur ou mot de passe invalide, ou\n"
        "compte inactif.",
    ),
]

missing = []
for old, new in pairs:
    if old in t:
        t = t.replace(old, new, 1)
    else:
        missing.append(old.splitlines()[0])

p.write_text(t, encoding="utf-8")
print("Appliquees :", len(pairs) - len(missing))
for m in missing:
    print("NON TROUVE :", m)
