The proposal is to make an android based mobile application meant for the user to identify nearby parking spots, be it dedicated or roadside parking spots and concurrently develop a new software meant for use by the authorities in charge of parking facilities. The database used by the suppliers and the clients however would be the same, and thus real time updates for dedicated parking spots can be obtained, whilst the roadside/local parking spots are monitored via satellite imaging.

Supplier Software : 

This includes a dynamic website to be used by the authorities managing the dedicated parking spots. The website will have a credential-based single factor authentication and initially the suppliers will have to register themselves on it. This minimalistic process involves the suppliers receiving their credentials (username, password) through email/sms upon successful verification of their Corporate Identity Number (CIN). They can login and upload information about their respective facilities (eg: Total capacity, vehicle specific spots, running hours, whether or not valet service is available). There would be provisions to upload photos as well thus enabling a compact selling platform for the suppliers. The only requirement from the supplier side is to install devices on entry which will have 2 options, either to enter booking id, or to generate a ticket. There would be a difference in the color of the tickets generated for a booked ticket and a normal ticket (say white background for normal, and yellow for booked). The time, date, ticket Id is inserted into the database upon ticket generation.
Additionally, whether or not spots are available can be tracked based on the number of tickets issued [ total capacity - number of tickets issued ]. Again, if a booking is made, we reduce the total capacity by 1, so even though a spot would be empty, we close the gates to stop any other vehicle from entering, expect for the one that had made the booking. Upon exit the entries made in the database are deleted, the number of vacant spots, the capacity are readjusted appropriately and payment is asked for from the white colored ticket holders, and the yellow colored ones who have exceeded their time limit. 



Client Side (people looking to park their vehicles) : 
The following details are expected from the user : 
When the app is first installed (one time)  -  1.  User details

On opening the app, the user has to enter the following fields -
1.  Destination [ An option to show results using the current location present as well]
2.  Premium / free parking [ Optional, if provided options specific to the choice displayed ] 
3.  Vehicle category ( to get an idea about the car size, example - Sedan/SUV/Bike) [ Optional, if provided search results factor the size  ]

Premium Parking : 

The user is shown all the nearest dedicated secure parking facilities (for example: the ones in shopping malls) which have vacant parking spots, with the details of the parking fee, photos of the facility, a star rating(based on user feedback) being displayed. The user can choose where they want to park their car amongst the options available. All of this information is based on the real time updates provided by the software used at the facility itself.
There will be an option to book a parking spot, the number of hours for which the booking is needed has to be entered too. since a service is being availed, some money on top of the rental fee will have to be paid by the user. The amount will be subject to the rush expected, time of the day, and certain other factors all under the jurisdiction of the authorities in charge of the facility. The booking is rendered complete only after payment of the fee, thereafter a booking ID is generated, which needs to be entered upon arrival at the facility. If the number of hours are exceeded, a fine is also levied, to be paid using the application itself, or upon exit at the counter. 
It should be noted that booking the spot is not mandatory, in which case the user is simply guided to the facility, there is no guarantee as to whether the parking spot would finally be occupied by the user since if a 3rd party (someone not using our application) comes up at the facility they cannot be refuted a spot, however the user would be notified of such events, and if need be, redirected to a new location. The information in regards to the availability of the spots is expected from the supplier software. 

Local Parking :

To identify local parking spots, records available in the public domain like city plans or traffic police department would be used. If such records are not available, small survey teams could be sent to mark these spots on the map. Once these spots have been identified, they will be monitored using satellite imagery, ONLY if it is in the vicinity of the user's destination. To ensure reduced computational cost, once the user inputs the location for parking, a perimeter of certain radius is set up around the same, the algorithm looks for local parking spots in that radius. Once found, using satellite imagery the spot is monitored, and just as in the case of non booking of premium spots, no guarantee is taken in regards to whether anyone else would beat the user to the spot, and in that case the user is notified. 

The main challenge here is to handle multiple requests for free parking spots, for which we use the following factors : 
1.  Request submission time 
2.  Proximity to the parking spot.

Request submission time is given higher priority since suggestions have to be made to people requesting our service. However these suggestions will only pop up if the customer is sufficiently close to the parking spot. This will take care of cases where a customer far from the destination has submitted a request but another customer much closer to the spot gets deprived.

Future extensions possible :

1. Making IOS, web based applications to garner more users.  
2. Expanding our outreach to multiple cities. 

Note : To develop the app some public APIs (eg: Google's API) providing functionality pertaining to Maps, and a database is required both of which although free for the prototype submission phase, would be subject to payment in case of increased usage, and possible release to the market.

