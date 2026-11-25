# 🐍 Initiation au développement web avec Django

> **Module de formation** — Niveau débutant  
> **Projet fil rouge** : gestion d'une bibliothèque municipale  
> **Public** : développeurs débutants ayant des bases en Python et HTML

---

## 📋 Table des matières

- [Objectifs pédagogiques](#-objectifs-pédagogiques)
- [Public visé et prérequis](#-public-visé-et-prérequis)
- [Projet fil rouge](#-projet-fil-rouge)
- [Plan du module](#-plan-du-module)
- [Organisation du dépôt](#-organisation-du-dépôt)
- [Installation et mise en route](#-installation-et-mise-en-route)
- [Bonnes pratiques Django abordées](#-bonnes-practices-django-abordées)
- [Évaluation et livrables](#-évaluation-et-livrables)
- [Ressources complémentaires](#-ressources-complémentaires)
- [Contribution](#-contribution)

---

## 🎯 Objectifs pédagogiques

À l'issue de ce module, le stagiaire sera capable de :

- Comprendre l'architecture **MVT** (Modèle-Vue-Template) de Django.
- Créer un **projet** Django et y organiser ses **applications**.
- Concevoir des **modèles de données** relationnels avec l'ORM Django.
- Écrire des **vues** (fonctionnelles et génériques) et configurer le **routage d'URLs**.
- Utiliser le **langage de gabarits** (balises, filtres, héritage).
- Gérer les **fichiers statiques** (CSS, JS, images).
- Personnaliser l'**administration Django**.
- Créer des **formulaires** sécurisés avec `ModelForm`.
- Mettre en place l'**authentification** et les **permissions**.
- Appliquer les **bonnes pratiques** Django dès le premier projet.

---

## 👥 Public visé et prérequis

| Élément | Détail |
|---|---|
| **Public** | Développeurs juniors, étudiants, reconversion |
| **Python** | 3.10 ou supérieur |
| **Base HTML/CSS** | Notions suffisantes |
| **Ligne de commande** | Savoir naviguer et exécuter des commandes |
| **Éditeur** | VS Code, PyCharm ou équivalent |
| **Système** | Windows, macOS ou Linux |

---

## 📚 Projet fil rouge

Tout au long du module, le stagiaire développe **une application de gestion de bibliothèque** nommée `catalog`, dans un projet Django nommé `monprojet`.

### Fonctionnalités couvertes

- 📖 Consultation du catalogue de livres
- ✍️ Fiche détail par livre (auteur, ISBN, résumé, exemplaires)
- ➕ Ajout de livres via formulaire
- 🔐 Espace administrateur protégé
- 🧑‍💼 Gestion des utilisateurs et permissions (bibliothécaires / membres)
- 🎨 Interface HTML héritée d'un gabarit de base commun

### Modèles de données

- `Author` — auteur d'un livre
- `Genre` — catégorie littéraire
- `Book` — livre (relation Many-to-Many avec `Genre`, ForeignKey vers `Author`)
- `BookInstance` — exemplaire physique d'un livre (statut, date de retour)

---

## 🗺️ Plan du module

| # | Chapitre | Contenu clé |
|---|---|---|
| 1 | **Introduction à Django** | Qu'est-ce que Django, MVT, installation |
| 2 | **Structure d'un projet** | Rôle de `manage.py`, `settings.py`, `urls.py`, `wsgi.py`, `asgi.py` |
| 3 | **Création d'une application** | `startapp catalog`, rôle de `models.py`, `views.py`, `admin.py`, `apps.py` |
| 4 | **Chargement d'un gabarit** | `base.html`, héritage `{% extends %}`, contexte de vue |
| 5 | **Fichiers statiques** | `STATIC_URL`, `STATICFILES_DIRS`, balise `{% static %}` |
| 6 | **Balises et filtres** | `{% if %}`, `{% for %}`, `{% url %}`, `{% csrf_token %}`, filtres courants |
| 7 | **Modèles de données** | ORM, migrations, `ForeignKey`, `ManyToManyField`, `__str__`, `get_absolute_url` |
| 8 | **Gestion des requêtes** | Vues fonctionnelles, `ListView`, `DetailView`, routage avec `app_name` |
| 9 | **Admin Django** | `admin.site.register`, `list_display`, `list_filter`, `fieldsets` |
| 10 | **Formulaires Django** | `ModelForm`, validation, rendu `{{ form.as_p }}`, CSRF |
| 11 | **Authentification** | `LoginView`, `LogoutView`, `@login_required`, `createsuperuser` |
| 12 | **Permissions** | `@permission_required`, `perms` dans les templates, groupes |
| 13 | **Conclusion** | Récapitulatif, pistes d'approfondissement |

📄 **Contenu détaillé** : voir [`module_initiation_django.txt`](./module_initiation_django.txt)

---

## 📂 Organisation du dépôt

```
formations/django/
├── README.md                          ← ce fichier
└── module_initiation_django.txt       ← module pédagogique complet
```

Le module contient, pour chaque chapitre :

- 🎯 un objectif pédagogique,
- 💡 une explication simple du concept,
- 💻 des exemples de code réels (prêts à copier),
- ✅ une ou plusieurs bonnes pratiques Django.

---

## ⚙️ Installation et mise en route

### 1. Créer un environnement virtuel

```bash
python -m venv .venv
```

**Activation :**

- **Windows (PowerShell)** : `.venv\Scripts\Activate.ps1`
- **macOS / Linux** : `source .venv/bin/activate`

### 2. Installer Django

```bash
pip install django
python -m django --version    # doit afficher la version installée
```

### 3. Créer le projet et l'application

```bash
django-admin startproject monprojet
cd monprojet
python manage.py startapp catalog
```

### 4. Configurer la base de données et les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un administrateur

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

Ouvrir [http://127.0.0.1:8000/catalog/](http://127.0.0.1:8000/catalog/) et [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

---

## ✅ Bonnes pratiques Django abordées

- 🔐 Ne jamais exposer `SECRET_KEY` en production ; utiliser des variables d'environnement.
- 📁 Utiliser `BASE_DIR / "..."` pour les chemins (et non des chaînes en dur).
- 🧩 Déclarer les apps par leur classe `AppConfig` dans `INSTALLED_APPS`.
- 🏷️ Utiliser `app_name` et `{% url 'app:name' %}` pour éviter les collisions.
- 🧱 Préférer `on_delete=SET_NULL` ou `RESTRICT` plutôt que `CASCADE` par défaut.
- 🎨 Limiter la logique dans les templates (calculs dans les vues/modèles).
- 📝 Toujours inclure `{% csrf_token %}` dans les formulaires POST.
- 🧪 Écrire des tests unitaires pour les modèles et vues critiques.
- 👥 Gérer les rôles via des **groupes** plutôt que des permissions individuelles.

---

## 📝 Évaluation et livrables

### Livrables attendus

1. **Dépôt Git** contenant le projet `monprojet` complet.
2. **Application fonctionnelle** avec :
   - Au moins 3 modèles reliés.
   - Une page liste + une page détail.
   - Un formulaire d'ajout.
   - Un espace admin personnalisé.
   - Une zone protégée par authentification.
3. **Un fichier `README.md`** de projet expliquant l'installation et les fonctionnalités.

### Grille d'évaluation indicative

| Critère | Poids |
|---|---|
| Modèles corrects et relationnels | 20 % |
| Vues et routage | 20 % |
| Templates et héritage | 15 % |
| Admin personnalisé | 10 % |
| Formulaires et validation | 15 % |
| Authentification et permissions | 10 % |
| Respect des bonnes pratiques | 10 % |

---

## 📚 Ressources complémentaires

- 📘 [Documentation officielle Django (FR)](https://docs.djangoproject.com/fr/stable/)
- 📘 [Tutoriel MDN Django — LocalLibrary](https://developer.mozilla.org/fr/docs/Learn/Server-side/Django)
- 📘 [Django Girls Tutorial](https://tutorial.djangogirls.org/fr/)
- 📘 [Django Best Practices](https://django-best-practices.readthedocs.io/)
- 🎥 [Chaîne YouTube Django Software Foundation](https://www.youtube.com/@djangoproject)

---

## 🤝 Contribution

Ce module fait partie du dépôt **SKYFALL_FORMATIONS_WEB_DOCS**.

### Proposer une amélioration

1. Créer une branche depuis `main` :
   ```bash
   git checkout -b docs/django-ma-modif
   ```
2. Faire ses modifications puis committer (Conventional Commits) :
   ```bash
   git commit -m "docs(django): correction typo chapitre 7"
   ```
3. Pousser et ouvrir une **Pull Request** en assignant un relecteur.

### Signaler une erreur

Ouvrir une [issue](https://github.com/plwam/SKYFALL_FORMATIONS_WEB_DOCS/issues) avec le tag `django` en précisant :

- Le chapitre concerné,
- La nature de l'erreur (code, typo, lien cassé),
- Une suggestion de correction si possible.

---

## ✨ Remerciements

Merci à tous les formateurs et stagiaires qui contribuent à améliorer ce module.

**Bonne formation et bon code ! 🚀**
