import uuid
from config import db, ma

class StoreLocations(db.Model):
    __tablename__ = "store_locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), unique=True)
    city = db.Column(db.String(), unique=True)
    state = db.Column(db.String())
    zip_code = db.Column(db.String())
    phone = db.Column(db.String())

    def __init__(self, name, address, city, state, zip_code, phone):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

class StoreLocationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StoreLocations


store_location_schema = StoreLocationsSchema()
store_locations_schema = StoreLocationsSchema(many=True)

# , default=lambda: str(uuid.uuid4())