from parking import Parking
import numpy as np

parking = Parking()
cars = np.zeros(40) # the drivers wants to park their cars
cars[10:15] = 1 # the drivers who wants to leave the parking 

for i in range(len(cars)):
  if cars[i] == 0:
    permission = parking.check_availability()
    if permission is True:
      print("Welcome")
    else:
      print("Parking is Full")
  else:
    parking.leave_parking()
    print("Good bye!")
