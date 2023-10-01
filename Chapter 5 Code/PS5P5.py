LastName=input("Enter employee's last name:  ")
Salary=float(input("Enter employee's salary:  "))
JobLevel=int(input("Enter employee's job level:  "))

if JobLevel>10:
  BonusRate=0.25
elif JobLevel>5:
  BonusRate=0.20
else:
  BonusRate=0.10

Bonus=Salary * BonusRate

print("Employee's last name:  ",LastName)
print("Employee's bonus is $ ", Bonus)