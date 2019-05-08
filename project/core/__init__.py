from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()


def setup_app(app):
    db.init_app(app)
