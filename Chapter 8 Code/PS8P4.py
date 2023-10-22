def CompPayRate(jobcode):
  payrate = 0
  if jobcode == 'L':
    payrate=25.00
  elif jobcode == 'A':
    payrate=30.00
  elif jobcode == 'J':
    payrate=50.00

  return payrate


totalgrosspay=0

lastname=input("Enter employee's last name:     ")

while lastname !="" :
  hoursworked=float(input("Enter hours worked:    "))
  jobcode=input("Enter employee's job code:    ")
  payrate=CompPayRate(jobcode)
  if hoursworked>40:
    grosspay=(40*payrate)+((hoursworked-40)*(payrate*1.5))
  else:
    grosspay=hoursworked*payrate

  totalgrosspay=totalgrosspay+grosspay

  print("Employee's last name:",lastname)
  print(lastname,"'s gross pay is:  ",grosspay)
  print("")

  lastname=input("Enter employee's last name:     ")

print("The total gross pay is: ",totalgrosspay )
    
  


    
    
  
  
  