from flask import Blueprint
from controllers import store_locations_controller

store_location_routes = Blueprint("store_location_routes", __name__)


@store_location_routes.route("/", methods=["GET"])
def get_all_store_locations():
    return store_locations_controller.get_all_store_locations()


@store_location_routes.route("/<id>", methods=["GET"])
def get_store_location_by_id(id):
    return store_locations_controller.get_store_location_by_id(id)


@store_location_routes.route("/", methods=["POST"])
def create_store_location():
    return store_locations_controller.create_store_location()


@store_location_routes.route("/delete/<id>", methods=["DELETE"])
def delete_store_location(id):
    return store_locations_controller.delete_store_location(id)