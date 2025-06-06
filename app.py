import os
from flask import Flask
from flask_cors import CORS

from config import db, ma, jwt
from routes.store_routes import store_routes


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sportsman-warehouse.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    CORS(app, origins=["http://localhost:5173"])
    
    app.register_blueprint(store_routes, url_prefix="/api/stores")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__": 
    app = create_app()
    app.run(debug=True)