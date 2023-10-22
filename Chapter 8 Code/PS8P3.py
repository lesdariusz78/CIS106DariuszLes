def CompMPG(MilesTraveled, GallonsUsed):
  MPG = MilesTraveled / GallonsUsed
  return MPG

c=0

DestCity=input("Enter Destination City: ")

while DestCity !="" :
 MilesTraveled=float(input("Enter Miles Traveled: "))
 GalonsUsed=float(input("Enter Gallons Used: "))
 MPG=CompMPG(MilesTraveled, GalonsUsed)

 print("Destination city:", DestCity)
 print("Miles traveled:", MilesTraveled)
 print("Miles per gallon:  ", MPG)
 print("")

 c=c+1
 DestCity=input("Enter Destination City: ")

print("Number of trips: ", c)