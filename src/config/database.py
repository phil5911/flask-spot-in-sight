from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    ### Initialise la base de données avec l'application Flask ###
    db.init_app(app=app)
    with app.app_context():
        db.create_all()