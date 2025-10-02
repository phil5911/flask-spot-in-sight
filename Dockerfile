# 1. Installation de python
FROM python:3.12.7-alpine3.20

WORKDIR /app

# 2. Installation des dépendances
COPY requirements.txt .
RUN pip3 install -r ./requirements.txt

# 4. Copier le reste de mon fichier
COPY . .

# 5. Démarrer mon serveur python
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "app.py"]

