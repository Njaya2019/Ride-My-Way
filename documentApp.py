from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields,inputs,reqparse
from rmw import viewRides, view_a_ride, add_a_ride,requests,make_request
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
             'driver_id':2},
            { 'id':2,
              'ride_route':'Bamburi to Kilifi',
              'date_of_ride':'3/7/2018',
              'time':'11:00 am',
              'contacts':'0706714059',
              'driver_id':2
            }]

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
@new_api.route('/ridesOffered')
class rides(Resource):
    def get(self):        
        def viewRides():
            return jsonify({'rides':ride_offers})

    

#class to request a specific ride
parser = new_api.parser()
parser.add_argument('Ride to view', type=int, required=True, help='Ride id')

@new_api.doc(parser=parser)
@new_api.route('/rides/<int:id>')
class View_aride(Resource):
    def get(self, id):
        def view_a_ride(id):
            
            for ride_offer in ride_offers:
                
                ride_offer_id=ride_offer['id']
                if ride_offer_id==id:
                    
                    return jsonify({'rides':ride_offer})
        




# A class to add a ride
parser= new_api.parser()
parser.add_argument('id', type=int, required=True, help='id')
parser.add_argument('ride_route', type=str, required=True, help='route')
parser.add_argument('date_of_ride', type=str, required=True, help='date')
parser.add_argument('time', type=str, required=True, help='time')
parser.add_argument('contacts', type=int, required=True, help='contacts')



@new_api.doc(parser=parser)
@new_api.route('/rides')
class Add_aride(Resource):
    def put(self):
        
        global add_ride
        args = parser.parse_args()
        add_ride.update({'id':args['id'],'ride_route':args['ride_route'],'date_of_ride':args['date_of_ride'],'time':args['time'],'contacts':args['contacts']})
        rides=[]
        rides.append(add_ride)
        return jsonify({'Rides':rides})

# A class to add a ride
@new_api.route('/rides/<int:ride_id>/request')
class Make_ride_request(Resource):
    def put(self,ride_id):
        global users,requests,ride_offers
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
        
        
    
    
    
    
   

if __name__ == '__main__':
    app.run(debug=True)

