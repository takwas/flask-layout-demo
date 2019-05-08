from flask import Flask 


def create_app(env):
    from project.core import setup_app
    
    app = Flask(__name__)
    setup_app(app)

    return app
