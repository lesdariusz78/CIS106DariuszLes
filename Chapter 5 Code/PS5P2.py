Qty=float(input("Enter the quantity: "))
PartNum=int(input("Part number: "))

if PartNum==10 or PartNum==55:
 UnitCost=1.00
elif PartNum==99:
 UnitCost=2.00
elif PartNum==70 or PartNum==80:
 UnitCost=3.00
else:
 UnitCost=5.00
  
Total=UnitCost * Qty

print("Part number is: ",PartNum)
print("Cost per unit equals $ ",UnitCost)
print("Your total is $ ",Total)







