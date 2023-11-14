def sales_report(sales):
  if sales>100000:
    percent=.10
  elif sales<=100000:
    percent=.05
  
  commission=sales*percent
  nextyearsales=sales*1.05
  return commission,nextyearsales

lastname=input("Enter sales person's last name: ")
sales=float(input("Enter the sales amount: "))
commission,nextyearsales=sales_report(sales)
print("The commission is: ",commission)
print("The next year's sales is: ",nextyearsales)
  

   