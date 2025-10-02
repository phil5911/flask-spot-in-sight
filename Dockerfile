# Étape 1 : utiliser Python Alpine léger
FROM python:3.12.7-alpine3.20

# Étape 2 : définir le dossier de travail
WORKDIR /app

# Étape 3 : copier les fichiers de dépendances et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : copier le reste de l’application
COPY . .

# Étape 5 : exposer le port
EXPOSE 5000

# Étape 6 : lancer Gunicorn avec 4 workers et binding
# "app" = nom du fichier app.py
# "app" = variable Flask dans app.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "-w", "4"]
