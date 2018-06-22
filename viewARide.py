from flask import Flask, request, jsonify
from data import ride_offers
app=Flask(__name__)





@app.route('/rides/<int:id>',methods=['GET'])
def view_a_ride(id):
    for ride_offer in ride_offers:
        ride_offer_id=ride_offer['id']
        if ride_offer_id==id:
            return jsonify({'rides':ride_offer})
            
    



if __name__=='__main__':
    app.run(debug=True)