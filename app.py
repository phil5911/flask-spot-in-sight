from flask import Flask
from flask_cors import CORS
from src.api.api import api_bp
from src.api.task import tasks_bp
from src.config.database import init_db

def create_app():
    app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(api_bp, url_prefix="/api")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    return app

if __name__ == "__main__":
    app = create_app()
    init_db(app)
    app.run(debug=True)







