NumOfEmployees=0
SumOfGrossPay=0
print("Do you want to participate in this program? ")
Response=input()

while Response=="Yes":
  NumOfEmployees=NumOfEmployees + 1
  LastName=input("Enter employee's last name: ")
  PayRate=float(input("Enter employee's pay rate: "))
  HoursWorked=float(input("Enter hours worked: "))
  if HoursWorked>40:
    GrossPay=(40*PayRate) + (HoursWorked-40)*1.5*PayRate 
  else:
    GrossPay=HoursWorked * PayRate

  print("Gross pay is ", GrossPay)
  SumOfGrossPay=SumOfGrossPay + GrossPay
  print("Do you want to participate in this program? ")
  Response=input()

print("Sum of all gross pay is: ",SumOfGrossPay)
print("Number of employees that participated: ", NumOfEmployees)
AvgGrossPay=SumOfGrossPay/NumOfEmployees
print("Average gross pay is: ", AvgGrossPay)