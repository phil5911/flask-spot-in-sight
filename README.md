## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- **Python 3.11 ou supérieur** : [Télécharger Python](https://www.python.org/downloads/)
- **Virtualenv** (optionnel mais recommandé) : `pip install virtualenv`
- **Git** : [Télécharger Git](https://git-scm.com/downloads)

## Installation

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/nderhore/flask-to-do-list.git
   cd flask-to-do-list
   ```

2. **Créer un environnement virtuel**

   ```bash
   virtualenv venv
   source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
   ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Lancer l'application**

   ```bash
   flask run
   ```

   L'application sera accessible sur `http://localhost:5000`.

2. **Accéder à l'application**

   Ouvrez votre navigateur web et rendez-vous sur `http://localhost:5000`.