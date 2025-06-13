import uuid
from config import db, ma

class Products(db.Model):
    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    category = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    brand = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __init__(self, category):
        self.category = category

class ProductsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        load_instance = True


store_schema = ProductsSchema()
stores_schema = ProductsSchema(many=True)