#!/usr/bin/env bash
set -o errexit  # Arrête le script en cas d'erreur

# Installer les dépendances
pip install -r requirements_global.txt

# Collecter les fichiers statiques
python manage.py collectstatic --no-input

# Appliquer les migrations
python manage.py migrate
