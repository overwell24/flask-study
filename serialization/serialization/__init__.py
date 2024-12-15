from flask import Flask
from .config.base import *
from .config.extensions import db, ma

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['DEBUG'] = DEBUG
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    
    db.init_app(app)
    ma.init_app(app)
    
    with app.app_context():        
        db.create_all()
        
    return app