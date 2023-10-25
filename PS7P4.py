f=open("P4D.txt", "r")

c=0
totalexprice=0.0

item=f.readline().rstrip('\n')

while item !="":
  qty=float(f.readline())
  price=float(f.readline())

  extprice=qty * price
  totalexprice=totalexprice + extprice
  c=c+1

  print("Item:               ",item)
  print("Quantity:            ",qty)
  print("Price:               ",price)
  print("Extended price:      ",extprice)
  print("   ")

  item=f.readline().rstrip('\n')


print("Total extended price:     ",totalexprice)
print("Nmber of orders:     ",c)
AverageOrder=totalexprice/c
print("Average order is:     ",AverageOrder)

  
  
  