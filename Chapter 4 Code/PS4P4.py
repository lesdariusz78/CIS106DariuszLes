print("Input the appliance name:")
AppName=input()
print("Enter the cost of the appliance:")
AppCost=float(input())
if AppCost <= 1000:
  Warranty=AppCost*.05
else:
  Warranty=AppCost*.10
Total=AppCost + Warranty
print("The aplliance:" , AppName)
print("The cost of the appliance is $ ",AppCost)
print("The warranty cost is $", Warranty)
print("The total cost is $", Total)