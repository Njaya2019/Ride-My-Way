from flask import Flask, request, jsonify
from data import ride_offers,add_ride,users
app=Flask(__name__)



@app.route('/rides', methods=['POST'])
def add_a_ride():
    global add_ride
    ride_id_to_add=add_ride['id']
    for ride_offer in ride_offers:
        ride_offer_id=ride_offer['id']
        if ride_offer_id==ride_id_to_add:
            return 'ride exists'
        else:
            for user in users:
                if user['usertype']=='driver':
                    add_ride.update({'driver_id':user['id']})
                    ride_offers.append(add_ride)
                    return jsonify({'rides':ride_offers})
    
    

if __name__=='__main__':
    app.run(debug=True)