print("Enter user's last name")
LastName=input()
print("Input the number of dependents")
NumOfDep=float(input())
print("Enter the gross income")
GrossIncome=float(input())

AdjGrossIncome=float(GrossIncome)-float(NumOfDep)*12000

if float(AdjGrossIncome)>50000:
 IncomeTax=AdjGrossIncome*.20
else:
  IncomeTax=AdjGrossIncome * .10

if IncomeTax<0:
  IncomeTax=100

print("Last name:",LastName)
print("Gross income is $", GrossIncome)
print("The number of dependents: ", NumOfDep)
print("Adjusted Gross Income is $ ", AdjGrossIncome)
print("Income tax is $ ", IncomeTax)