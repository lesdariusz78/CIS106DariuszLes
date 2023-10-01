Principle=float(input("Enter the principle amount:"))
Maturity= float(input("Enter the maturity:"))

if Principle>100000 and Maturity==5:
  IntRate=0.06
elif Principle>50000 and Maturity==10:
  IntRate=0.05
elif Principle>50000 and Maturity==5:
  IntRate=0.04
else:
  IntRate=0.02

FirstYearInt=IntRate * Principle

print("Your principle is $ ",Principle)
print("Your interest rate is ",IntRate)
print("Your interest for first year is ",FirstYearInt)