from flask import Flask, request, jsonify
from data import ride_offers,add_ride,users,requests
app=Flask(__name__)



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
       
    
    

if __name__=='__main__':
    app.run(debug=True)