from flask import request, jsonify

from config import db
from models.users import Users, user_schema

def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if Users.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400
    
    new_user = Users(email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))