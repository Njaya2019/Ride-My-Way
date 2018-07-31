from flask import Flask, request, jsonify
from data import ride_offers, users, requests

app=Flask(__name__)


add_ride={}

@app.route('/ridesOffered', methods=['GET'])
def viewRides():
    return jsonify({'rides':ride_offers})


@app.route('/rides/<int:id>',methods=['GET'])
def view_a_ride(id):
    for ride_offer in ride_offers:
        ride_offer_id=ride_offer['id']
        if ride_offer_id==id:
            return jsonify({'rides':ride_offer})

@app.route('/rides', methods=['POST'])
def add_a_ride():
    global add_ride
    for user in users:
        if user['usertype']=='driver':
            add_ride.update({'driver_id':user['id']})
            ride_offers.append(add_ride)
            return jsonify({'rides':ride_offers})

@app.route('/rides/<int:ride_id>/request', methods=['POST'])
def make_request(ride_id):
    global requests
    for ride_offer in ride_offers:
        ride_offer_id=ride_offer['id']
        if ride_offer_id==ride_id:
            for user in users:
                if user['usertype']=='passenger':
                    request={'id':1,
                    'passenger_id':user['id'],
                    'driver_id':ride_offer['driver_id'],
                    'rideoffered_id':ride_offer['id']}
                    requests.append(request)
                    return jsonify({'Rides requsted':requests})

# execute the project

if __name__=='__main__':
    app.run(debug=True)
