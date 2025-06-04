from flask import request, jsonify

from config import db
from models.store_locations import StoreLocations, store_locations_schema, store_location_schema


def get_all_store_locations():
    store_locations = StoreLocations.query.all()
    return jsonify({"results": store_locations_schema.dump(store_locations)})


def get_store_location_by_id(id):
    store_location = db.session.get(StoreLocations, id)

    if not store_location:
        return jsonify({"error": "Store location not found"}), 404
    
    return jsonify(store_location_schema.dump(store_location))


def create_store_location():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Store name required"}), 400
    
    address = data.get("address")
    city = data.get("city")
    state = data.get("state")
    zip_code = data.get("zip_code")
    phone = data.get("phone")

    new_store_location = StoreLocations(name=name, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
    db.session.add(new_store_location)
    db.session.commit()

    return jsonify(store_location_schema.dump(new_store_location))


def delete_store_location(id):
    store_location = StoreLocations.query.filter(StoreLocations.id == id).first()

    if not store_location:
        return jsonify({"error": "Store location not found"}), 404

    db.session.delete(store_location)
    db.session.commit()

    return jsonify({"message": "Store Location Deleted"})
