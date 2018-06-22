from flask import Flask, request, jsonify
from data import ride_offers
app=Flask(__name__)




@app.route('/rides', methods=['GET'])
def viewRides():
    return jsonify({'rides':ride_offers})

if __name__=='__main__':
    app.run(debug=True)