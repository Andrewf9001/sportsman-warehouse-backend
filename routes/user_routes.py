from flask import Blueprint
from controllers import users_controller

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/register", methods=["POST"])
def register():
    return users_controller.register()


@user_routes.route("/login", methods=["POST"])
def login():
    return users_controller.login()