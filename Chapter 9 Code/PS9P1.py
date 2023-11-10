def CompNextMonthSales(month,sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    ForecastPercent=.1
  elif month== "Apr" or month == "May" or month == "Jun":
    ForecastPercent=.15
  elif month== "Jul" or month == "Aug" or month == "Sep":
    ForecastPercent=.20
  elif month== "Oct" or month == "Nov" or month == "Dec":
    ForecastPercent=.25

  NextMonthSales=sales*(1+ForecastPercent)
  return NextMonthSales

print("Do you want to calculate next month's sales(Y/N)")
response=input()
while response=="Y":
  lastname=input("Enter last name: ")
  month=input("Enter month: ")
  sales=float(input("Enter sales: "))
  NextMonthSales=CompNextMonthSales(month,sales)
  print("Next month's sales is: ",NextMonthSales)
  print("Do you want to calculate next month's sales(Y/N)")
  response=input()

else:
  print("Thank you for using this program")