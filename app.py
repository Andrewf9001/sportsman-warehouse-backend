from flask import Flask
from flask_cores import CORS

from database import db
from routes import routes

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sportsman-warehouse.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app()
    CORS(app, origins=["http://localhost:5173"])
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)