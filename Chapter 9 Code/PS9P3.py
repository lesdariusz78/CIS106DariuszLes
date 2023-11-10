def CompDiscountPrice(MSRP,Make,Model):
  if Make == "Honda" and Model == "Accord":
      PercentOff=.10
  elif Make == "Toyota" and Model=="RAV4":
      PercentOff=.15
  else:
      PercentOff=.05
    
  DiscountPrice=MSRP-(MSRP*PercentOff)+.07*(MSRP-         (MSRP*PercentOff))
  return DiscountPrice

SumMSRP=0
SumDiscountPrice=0
print("Do you want to calculate out the door price of the vehicle?(Y/N)")
response=input()
while response=="Y":
  print("What is the MSRP of the vehicle?")
  MSRP=float(input())
  print("What is the make of the vehicle?")
  Make=input()
  print("What is the model of the vehicle?")
  Model=input()
  DiscountPrice= CompDiscountPrice(MSRP,Make,Model)
  print("The discounted price of the vehicle is $",DiscountPrice)
  print("Do you want to calculate out the door price of the vehicle?(Y/N)")
  response=input()

  SumMSRP=SumMSRP+MSRP
  SumDiscountPrice=SumDiscountPrice+DiscountPrice
print("The sum of all MSRPs is $",SumMSRP)
print("The sum of discount prices is $",SumDiscountPrice)
print("Thank you for using our dealership. Have a nice day.")
