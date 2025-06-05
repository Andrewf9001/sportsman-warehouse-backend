import uuid
from config import db, ma

class Stores(db.Model):
    store_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, unique=True)
    city = db.Column(db.String, unique=True)
    state = db.Column(db.String)
    zip_code = db.Column(db.String)
    phone = db.Column(db.String)

    def __init__(self, name, address, city, state, zip_code, phone):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

class StoresSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stores
        load_instance = True


store_schema = StoresSchema()
stores_schema = StoresSchema(many=True)