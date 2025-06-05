from flask import Blueprint
from controllers import stores_controller

store_routes = Blueprint("store_routes", __name__)


@store_routes.route("/", methods=["GET"])
def get_all_stores():
    return stores_controller.get_all_stores()


@store_routes.route("/<store_id>", methods=["GET"])
def get_store_by_id(store_id):
    return stores_controller.get_store_by_id(store_id)


@store_routes.route("/", methods=["POST"])
def create_store():
    return stores_controller.create_store()


@store_routes.route("/delete/<store_id>", methods=["DELETE"])
def delete_store(store_id):
    return stores_controller.delete_store(store_id)