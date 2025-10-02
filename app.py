import os
from flask import Flask
from flask_cors import CORS
from src.api.api import api_bp
from src.api.task import tasks_bp
from src.config.config import Config
from src.config.database import db


def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join("src", "templates"),  # chemin des templates
        static_folder=os.path.join("src", "static")  # si tu as des fichiers CSS/JS
    )
    app.config.from_object(Config)

    # Active CORS pour toutes les routes
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


    print("➡️ DB URI:", app.config["SQLALCHEMY_DATABASE_URI"])  # debug

    # Initialisez db avec l'application
    db.init_app(app)

    # Importez les modèles et créez les tables
    with app.app_context():
        from src.model.Task import Task
        db.create_all()

    # Importez et enregistrez les blueprints
    from src.api.api import api_bp
    from src.api.task import tasks_bp
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(api_bp, url_prefix="/api")
    return app

# ⚠️ rendre l'instance globale pour gunicorn
app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)






