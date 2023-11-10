def CompTicketPrice(MilesFromChicago):
  if MilesFromChicago >= 30:
    return 12
  elif MilesFromChicago >= 20:
    return 10
  elif MilesFromChicago >= 10:
    return 8
  else:
    return 5
  
Total=0
print("Do you want to buy a ticket?(Y/N)")
response=input()
while response=="Y":
  lastname=input("Enter last name: )
  print("How many miles from Chicago?")
  milesFromChicago=float(input())
  TicketPrice=CompTicketPrice(milesFromChicago)
  print("The ticket price is $",TicketPrice)
  print("Do you want to buy another ticket?(Y/N)")
  response=input()
  Total=Total+TicketPrice
else:
  print("The total for your tickets today is: $",Total)
  print("Thank you and have a nice day")
