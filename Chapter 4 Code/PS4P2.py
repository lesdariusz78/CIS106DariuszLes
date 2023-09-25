print("Item ordered: ")
item = input()
print("Enter the quantity ordered: ")
qty = float(input())
if item == "A":
    unitPrice = 10.0
else:
    unitPrice = 20.0
extPrice = qty * unitPrice
print("The item ordered is  " + item)
print("The price of the item is $" + str(unitPrice))
print("Extended price is $ " + str(extPrice))
