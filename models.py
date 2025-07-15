from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # e.g., car, tuk, van
    area = db.Column(db.String(100)) # e.g., Ahangama, Galle
    price_per_day = db.Column(db.Float, nullable=False)
    contact = db.Column(db.String(100), nullable=False)