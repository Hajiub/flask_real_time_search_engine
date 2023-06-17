from . import db
from flask import url_for
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    price = db.Column(db.String(50))

    def serialize(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'price': self.price,
            'url': url_for('main.detail_view', car_id=self.id)
        }
    def __repr__(self):
        return f"<Car {self.id} {self.make}>"