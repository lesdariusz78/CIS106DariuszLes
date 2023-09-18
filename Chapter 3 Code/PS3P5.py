#input phase
FixedCost=float(input("Enter the fixed cost of the product: "))
PricePerUnit=float(input("Enter the price per unit: "))
CostPerUnit=float(input("Enter the cost per unit: "))
#processing phase
BreakEvenPoint=FixedCost/(PricePerUnit-CostPerUnit)
#output phase
print("The break even point is: ",BreakEvenPoint)