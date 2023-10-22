def CompTuition(credits, districtcode):

  if districtcode == 'I':
    costpercredit = 250.00
  else:
    costpercredit = 550.00

  tuition = credits * costpercredit

  return tuition

totaltuition=0

lastname=input ("Enter student's last name:     ")

while lastname !="":
  districtcode=input("Enter the district code:         ")
  credits=float(input("Enter the number of credits:     "))

  tuition=CompTuition(credits, districtcode)

  print("")
  print(lastname,"'s tuition owed is:       ", tuition)
  print("")

  totaltuition=totaltuition + tuition
  
  lastname=input ("Enter student's last name:")

print("Total tuition owed is: ",totaltuition)
  


  