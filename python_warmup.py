##WARM UP EXERCISES
#write the code that takes a single string string containing the make and model of a vehicle.
#first part of te string before the space is the make
#the last part of the string after the space is a model
#we can assume that the strings will only have one space
#assume the input string is completely lowercased

#ex: truck = "toyota tacoma"
#sedan = "hyundai sonata"
#sports_car = "lambourgini diablo"

truck = "toyota tacoma"
make_and_model = truck.split()
vehicle_make = truck.split()[0]
vehicle_model = truck.split()[1]
print(make_and_model)

##Exercise #1
#Write the code to take a string and produce a dictionary out of that string.
#such that the output looks like the following:
#-you'll need a way to get the first part of the string and a way to get the second part of the string
#-feel free to make new variables/ data types in between the string and the output dictionary

#input:
#truck = "toyota tacoma"

#output 
#truck = {
    #"make": "Toyota"
    #"model": "Tacoma"
#}

truck = dict(vehicle_make = 'toyota', vehicle_model = 'tacoma')
print(truck)

## Exercise #2
#Write the code that takes a dictionary contraining make/mode for a vehicle and capitalizess the first character of the make and the mode;

#input
#truck = {
    #"make": "toyota"
    #"model": "tacoma"
#}

#output
#truck = {
    #"make": "Toyota"
    #"model": "Tacoma"
#}

truck["make"] = truck["make"].capitalize()
truck["model"] = truck["model"].capitalize()
print(truck)

## Exercise #3
#create a list of 3 dictionaries where each dictionary represents a vehicle, as above
#write the code that operates on the list of dictionaries in order to uppercase the entire make and model values.

#input
#trucks = [{
 #   "make": "toyota",
  #  "model": "tacoma"
#},
#{
 #   "make": "ford",
  #  "model": "fusion"
#},
#{
 #   "make": "mazda",
  #  "model": "miata"
#}]

for truck in trucks:
    truck["make"] = truck["make"].upper()
    truck["model"] = truck["model"].upper()
trucks




