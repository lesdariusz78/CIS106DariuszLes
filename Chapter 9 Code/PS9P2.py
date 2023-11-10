def CompSqFt(length,height,width):
  SqFt=(2*length*width)+(2*length*height)+(2*height*width)
  return SqFt

print("Do you want to calculate gallons needed to paint a room?Y/N")
response=input()
while response=="Y":
  print("Enter the length of the room in feet:")
  length=int(input())
  print("Enter the hight of the room in feet:")
  high=int(input())
  print("Enter the width of the room in feet:")
  width=int(input())
  SqFt=CompSqFt(length,high,width)
  print("The square footage of the room is:",SqFt)
  Gallons=SqFt/50
  print("The gallons needed to paint the room are:",Gallons)
  print("Do you want to calculate gallons needed to paint a room?Y/N")
  response=input()

else:
  print("Goodbye")




