print("Enter the quantity ordered")
Qty = float(input())

UnitPrice = 3.0 if Qty >= 1000.0 else 5.0

ExtPrice = UnitPrice * Qty
Tax = ExtPrice * .07
Total = ExtPrice + Tax

print("Quantity ordered: ", Qty)
print("The price of the unit is $", UnitPrice)
print("Extended price is $", ExtPrice)
print("The tax is equal to $", Tax)
print("The total cost is $", Total)
