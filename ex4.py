# exercise 4: variables and names

# variables for use later
cars = 100
# the .0 makes this a float number for added precision
space_in_car = 4.0
drivers = 30
passangers = 90
# divides the value stored in cars with the value in drivers
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passanger_per_car = passangers / cars_driven

print "there are", cars, "cars avalible"
print "there are only", drivers, "drivers avalible"
print "there will be", cars_not_driven, "empty cars today"
print "we can transport", carpool_capacity, "people today"
print "we have", passangers, "to carpool today"
print "we need to put about", average_passanger_per_car, "in each car"




