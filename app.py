from flask import Flask, jsonify
from models import db, Vehicle
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

@app.route('/')
def index():
    return jsonify({"message": "Vehicle Service Running ✅"})

@app.route('/vehicles')
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{
        "id": v.id,
        "title": v.title,
        "type": v.type,
        "area": v.area,
        "price_per_day": v.price_per_day,
        "contact": v.contact
    } for v in vehicles])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
