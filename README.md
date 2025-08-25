# Explorateur Mathématique – Backend (Django REST)

API Django REST pour analyser des expressions/nombres et retourner leurs propriétés mathématiques (ensembles, définitions, explications, etc.) avec support multilingue (fr/en).

## Sommaire
- Prérequis
- Installation (local)
- Variables d'environnement
- Lancement (dev)
- Endpoints principaux
- Internationalisation (fr/en)
- Exemples de requêtes
- Déploiement (Render.com)
- Arborescence

## Prérequis
- Python 3.9+
- pip

## Installation (local)
```bash
# Cloner le dépôt
git clone <repo-url>
cd explorateur-mathematique

# (Optionnel) Créer un venv
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
# source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate
```

## Variables d'environnement
Créer un fichier `.env` (ou configurer vos variables dans l'environnement d'exécution) avec au minimum:
```
SECRET_KEY=remplacez_par_une_cle_secrete
```

Optionnel (prod):
```
ALLOWED_HOSTS=explorateur-mathematique.onrender.com
CORS_ALLOWED_ORIGINS=https://explo-math-front.vercel.app
```

## Lancement (dev)
```bash
python manage.py runserver
# API racine : http://127.0.0.1:8000/
# Endpoints API : http://127.0.0.1:8000/api/
```

## Endpoints principaux
- `GET /api/analyse-nombre/?nombre=<expr>&lang=<fr|en>`
  - Analyse une expression/nombre et retourne l'appartenance aux ensembles, les définitions et explications.
- `GET /api/nombres/` et `POST /api/nombres/`
  - Liste / crée des entrées `Nombre` (exemple d'entité stockée).

## Internationalisation (fr/en)
- Langue par défaut: `fr`
- Paramètre de requête: `lang=fr` ou `lang=en`
- Les libellés/explications proviennent de `translations/en.py` et `translations/fr.py`.
- Les traductions Django (po/mo) sont sous `api/locale/`.

## Exemples de requêtes
```bash
# Expression irrationnelle (pi)
curl "http://127.0.0.1:8000/api/analyse-nombre/?nombre=pi&lang=fr"

# Addition
data="2+3"
curl "http://127.0.0.1:8000/api/analyse-nombre/?nombre=$data&lang=en"
```

Extrait de réponse typique:
```json
{
  "language": "fr",
  "original_expression": "pi",
  "calculated_value": "3.141592653589793",
  "analysis": {
    "irrationnel": {
      "name": "Nombre irrationnel",
      "belongs": true,
      "definition": "ℝ \\ ℚ",
      "description": "Réel qui n'est pas rationnel.",
      "explanation": "pi est irrationnel"
    }
  }
}
```

## Déploiement (Render.com)
- Build Command:
```bash
pip install -r requirements.txt
```
- Start Command:
```bash
gunicorn enm.wsgi:application
```
- Variables Render à définir:
```
SECRET_KEY=remplacez_par_une_cle_secrete
ALLOWED_HOSTS=explorateur-mathematique.onrender.com
CORS_ALLOWED_ORIGINS=https://explo-math-front.vercel.app
```

## Arborescence (backend)
```
explorateur-mathematique/
  api/
    locale/
    migrations/
    math_engine.py
    math_utils.py
    models.py
    operations.py
    serializers.py
    urls.py
    utils.py
    views.py
  enm/
    settings.py
    urls.py
    wsgi.py
  manage.py
  requirements.txt
  translations/
    en.py
    fr.py
```
