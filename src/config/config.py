import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Base SQLite (db.db sera créé à la racine du projet)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "..", "db.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "changeme"  # optionnel, utile pour Flask
