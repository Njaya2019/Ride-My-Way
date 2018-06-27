from rmw import app, jsonify,add_ride
from flask_restplus import Api, Resource, fields,inputs,reqparse
from rmw import viewRides, view_a_ride, add_a_ride
new_api=Api(app, version='1.0', title='Ride my way api',
    description='Shows how users will View a ride, add a ride,view all rides available and request for a ride')




@new_api.route('/ridesOffered')
class rides(Resource):
    def get(self):
        return viewRides()
    


parser = new_api.parser()
parser.add_argument('Ride to view', type=int, required=True, help='Ride id')

@new_api.doc(parser=parser)
@new_api.route('/rides/<int:id>')
class View_aride(Resource):
    def get(self, id):
        return view_a_ride()





parser= new_api.parser()
parser.add_argument('id', type=int, required=True, help='id')
parser.add_argument('ride_route', type=str, required=True, help='route')
parser.add_argument('date_of_ride', type=str, required=True, help='date')
parser.add_argument('time', type=str, required=True, help='time')
parser.add_argument('contacts', type=str, required=True, help='contacts')



@new_api.doc(parser=parser)
@new_api.route('/rides')
class Add_aride(Resource):
    def put(self):
        global add_ride
        args = parser.parse_args()
        add_ride.update({'id':args['id'],'ride_route':args['ride_route']})
        return add_ride
        
    
    
    
    
   

if __name__ == '__main__':
    app.run(debug=True)

