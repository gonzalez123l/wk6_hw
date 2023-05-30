
from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required
from car_inventory.models import db,User,Cars,Car_Schema,Cars_Schema
from datetime import date

api = Blueprint('api',__name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata():
    return {'some':'value'}


#Create Car Endpoint
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(our_user):
    
    model = request.json['model']
    make = request.json['make']
    year = date(request.json['year'], 1, 1)
    color = request.json['color']
    image_url = request.json.get('image_url', None)
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    car = Cars(model=model, make=make, year=year, color=color, image_url=image_url, user_token=user_token)

    db.session.add(car)
    db.session.commit()

    response = Car_Schema.dump(car)

    return jsonify(response)

# RETRIEVE(READ) ALL CARs ENDPOINT
@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(our_user):
    owner = our_user.token
    cars = Cars.query.filter_by(user_token = owner).all()
    response = Cars_Schema.dump(cars)
    
    return jsonify(response)

#Reteieve Car by id endpoint
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(our_user, id):
    if id:
        car = Cars.query.get(id)
        response = Car_Schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({"message": "Car not found"}),401
    
# UPDATE Car ENDPOINT
@api.route('/cars/<id>', methods = ['PUT'])
@token_required
def update_car(our_user, id):
    car = Cars.query.get(id)
    car.model = request.json['model']
    car.make = request.json['make']
    car.year = date(request.json['year'], 1, 1)
    car.color = request.json['color']
    car.image_url = request.json.get('image_url', None)
    car.user_token = our_user.token

    db.session.commit()

    response = Car_Schema.dump(car)

    return jsonify(response)


# DELETE Car ENDPOINT
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(our_user, id):
    car = Cars.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = Car_Schema.dump(car)
    return jsonify(response)