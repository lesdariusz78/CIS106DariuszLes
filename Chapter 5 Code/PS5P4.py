Qty=int(input("Input the quantity of concert tickets:  "))

if Qty>=25:
  TicketPrice=50.00
elif Qty>10:
  TicketPrice=60.00
elif Qty>5:
  TicketPrice=70.00
else:
  TicketPrice=75.00

Total=TicketPrice * Qty

print("The number of tickets:  ",Qty)
print("Ticket price is $  ",TicketPrice)
print("Your total cost is $  ",Total)