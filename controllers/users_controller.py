from flask import request, jsonify
from flask_jwt_extended import create_access_token

from config import db
from models.users import Users, user_schema

def register():
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    user_name = data.get("user_name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if Users.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400
    
    new_user = Users(first_name, last_name, user_name, email, role)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))


def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    user = Users.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.user_id)

    return jsonify({"user": user_schema.dump(user), "token": access_token})