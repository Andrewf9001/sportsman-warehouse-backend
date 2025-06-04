from flask import Blueprint
from controllers import store_locations_controller

store_location_routes = Blueprint("store_location_routes", __name__)

@store_location_routes.route("/", methods=["GET"])
def get_all_store_locations():
    return store_locations_controller.get_all_store_locations()