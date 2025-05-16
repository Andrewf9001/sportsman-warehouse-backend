from database import db

class TestModel(db.Model):
    __tablename__ = "TestModel"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())

    def __init__(self, title):
        self.title = title