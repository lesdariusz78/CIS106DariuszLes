def CompExtPrice(qty,unitprice):
    extprice=qty*unitprice

    if extprice>10000:
      discountamount=extprice*0.1
    else:
      discountamount=0

    discextprice=extprice-discountamount
  
    
    return discextprice

totalextprice=0
response=input("Do you want to calculate extended price? (Y/N)")

while response=="Y":
  qty=float(input("Enter quantity: "))
  unitprice=float(input("Enter unit price: "))
  extprice=CompExtPrice(qty,unitprice)
  totalextprice=totalextprice + extprice
  print("Extended price: ",extprice)
  response=input("Do you want to calculate extended price? (Y/N)")

print("Total extended price is $",totalextprice)