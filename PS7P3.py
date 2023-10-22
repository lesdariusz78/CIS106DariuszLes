f=open("PS7P3.txt", "r")

c=0
totalbonus=0.0

lastname = str(f.readline().rstrip('\n'))

while lastname != "":
  salary =float(f.readline())
  
  if salary >= 100000.00 :
    bonusrate = .20
  elif salary > 50000.00:
     bonusrate = .15
  else:
    bonusrate=  .10

  bonus = salary * bonusrate
  totalbonus = totalbonus + bonus
  c = c + 1 

  print("Employee:", lastname)
  print("Bonus:", bonus)
  print("  ")

  lastname = str(f.readline().rstrip('\n'))

print("Sum of paid bonuses:",totalbonus)
