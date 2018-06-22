#data of all users,rides offered and requests made on rides offered
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
requests=[{'id':1,'passenger_id':2,'rideoffered_id':1}]

ride={
             'id':3,
             'ride_route':'Malindi to Mombasa',
             'date_of_ride':'29/6/2018',
             'time':'9:00 am',
             'contacts':'0727645367',
             'driver_id':2
}