SumOfDiscounts=0
NumOfOrders=0
print("Do you want to participate in our discount program? ")
Response=input()

while Response=="Yes":
  Qty=float(input("Enter the quantity ordered: "))
  Price=float(input("Enter the price of the item: "))
  ExtPrice=Qty*Price
  if ExtPrice>10000.00:
    DiscountAmt=ExtPrice * .25
  else:
    DiscountAmt=ExtPrice * .10

  Total=ExtPrice - DiscountAmt
  SumOfDiscounts=SumOfDiscounts + DiscountAmt
  NumOfOrders=NumOfOrders + 1
  print("Extended price is $ ", ExtPrice)
  print("Discount amount is $ ", DiscountAmt)
  print("Total amount ordered is $ ", Total)
  print("Do you want to participate in our discount program? ")
  Response=input()

print("Sum of all of discounts given is $ ", SumOfDiscounts)
print("Number of orders: ", NumOfOrders)

  
    