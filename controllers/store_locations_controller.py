from flask import request, jsonify

from config import db
from models.store_locations import StoreLocations, store_locations_schema

def get_all_store_locations():
    store_locations = StoreLocations.query.all()

    return jsonify({"stores": store_locations_schema.dump(store_locations)})