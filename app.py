from flask import Flask
from src.api.api import api_bp
from src.api.task import tasks_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(api_bp, url_prefix="/api")
    CORS(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)




