from flask import request, jsonify

from config import db
from models.stores import Stores, store_schema, stores_schema


def get_all_stores():
    stores = Stores.query.all()
    return jsonify({"results": stores_schema.dump(stores)})


def get_store_by_id(store_id):
    store = db.session.get(Stores, store_id)

    if not store:
        return jsonify({"error": "Store location not found"}), 404
    
    return jsonify(store_schema.dump(store))


def create_store():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Store name required"}), 400
    
    address = data.get("address")
    city = data.get("city")
    state = data.get("state")
    zip_code = data.get("zip_code")
    phone = data.get("phone")

    new_store = Stores(name=name, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
    db.session.add(new_store)
    db.session.commit()

    return jsonify(store_schema.dump(new_store))


def delete_store(store_id):
    store = Stores.query.filter(Stores.store_id == store_id).first()

    if not store:
        return jsonify({"error": "Store not found"}), 404

    db.session.delete(store)
    db.session.commit()

    return jsonify({"message": "Store Deleted"})
