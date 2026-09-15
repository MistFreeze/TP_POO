# TP0 — Programmation Python

Ce dossier contient les exercices du TP0 autour des structures de données
Python et de la robotique.

## Fichiers

- `tuples.py` : gestion des relevés de capteurs avec des tuples.
- `dictionnaire.py` : gestion du stock de pièces des robots.
- `ensemble.py` : opérations sur les ensembles de robots et de missions.
- `code_quality.py` : calcul du coût d'un trajet selon le terrain.
- `test_unit.py` : tests unitaires avec le module standard `unittest`.
- `environment.yml` : environnement Conda du projet.

## Prérequis

- Python 3.11 ou une version compatible.
- Conda, si vous souhaitez utiliser l'environnement fourni.

## Installer l'environnement

Depuis la racine du dépôt :

```bash
conda env create -f tp0/environment.yml
conda activate tp_poo
```

Pour mettre à jour un environnement existant :

```bash
conda env update -f tp0/environment.yml --prune
conda activate tp_poo
```

## Lancer les exercices

Depuis la racine du dépôt :

```bash
python tp0/tuples.py
python tp0/dictionnaire.py
python tp0/ensemble.py
python tp0/code_quality.py
```

## Lancer les tests

Pour exécuter les tests unitaires :

```bash
python -m unittest discover -s tp0 -p "test_*.py" -v
```

Les assertions présentes dans les fichiers d'exercices peuvent également être
exécutées directement avec les commandes de la section précédente.

## Qualité du code

Si Pylint est installé :

```bash
pylint tp0/*.py
```
