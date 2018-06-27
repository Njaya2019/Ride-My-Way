from flask import Flask, jsonify,request
from flask_restplus import Api, Resource, fields,inputs,reqparse

#create instance of flask
app=Flask(__name__)
#create class Api instance and pass instance of flask and other constructor 
#values relevant
new_api=Api(app, version='1.0', title='Ride my way api',
    description='Shows how users will View a ride, add a ride,view all rides available and request for a ride')
#data structures holding data to be accessed by the endpointS
ride_offers=[{'id':1,
             'ride_route':'Mtwapa to Mazeras',
             'date_of_ride':'26/6/2018',
             'time':'9:00 am',
             'contacts':'0727645367',
             'driver_id':2}]
users=[{'id':1,
        'email':'njayaandrew@gmail.com',
        'usertype':'passenger',
        'password':'a1990n'
       },
       {
         'id':2,
         'email':'njayaandrew@gmail.com',
         'usertype':'driver',
         'password':'w1986k'
       }
       ]
add_ride={}
requests=[]


#view all rides
@new_api.route('/ridesAvailable')
class rides(Resource):
    def get(self):    
        return {'rides':ride_offers}

    

#class to request a specific ride



@new_api.route('/rides/<int:id>')
class View_a_ride(Resource):
    def get(self, id):
        for ride_offer in ride_offers:
            ride_offer_id=ride_offer['id']
            if ride_offer_id==id:
                return {'rides':ride_offer}
     
a_ride=new_api.model('ride',{'id':fields.Integer,'ride_route':fields.String,
'date_of_ride':fields.Date,'time':fields.DateTime,'contacts':fields.Integer,
 'driver_id':fields.Integer
})

@new_api.route('/rides')
class Add_Ride(Resource):
    @new_api.expect(a_ride)
    def post(self):
        ride_offers.append(new_api.payload)
        return {'ride':ride_offers}
     









@new_api.route('/rides/<int:requested_ride_id>/request')
class Make_ride_request(Resource):
    global users,requests,ride_offers
    def post(self,requested_ride_id):
        for ride_offer in ride_offers:
            ride_offer_id=ride_offer['id']
            if ride_offer_id==requested_ride_id:
                for user in users: 
                    if user['usertype']=='passenger':
                        request={'id':1,
                            'passenger_id':user['id'],
                            'driver_id':ride_offer['driver_id'],
                            'rideoffered_id':ride_offer['id']}
                        requests.append(request)
                        return {'Rides requsted':requests}
        
        
    
    
    
    
   

if __name__ == '__main__':
    app.run(debug=True)

