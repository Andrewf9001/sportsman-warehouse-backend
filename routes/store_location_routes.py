from flask import Blueprint
from controllers import store_locations_controller

todo_routes = Blueprint("todo_routes", __name__, url_prefix="/api/store-locations")

@todo_routes.route("/", methods=["GET"])
def get_store_locations():
    return store_locations_controller.get_all_store_locations()