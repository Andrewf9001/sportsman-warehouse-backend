from flask import Blueprint, request, jsonify
from models import TestModel
from database import db

routes = Blueprint("routes", __name__)

@routes.route("/test-add", methods=["POST"])
def add_test_item():
    return 