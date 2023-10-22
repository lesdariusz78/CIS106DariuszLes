f = open("data1.txt", "r")

c = 0
totaltuition = 0.0

lastname = str(f.readline().rstrip('\n'))
while lastname != "":
  dcode = f.readline()
  credits = float(f.readline())

  if dcode == "I\n":
    costpercredit = 250.00
  else:
    costpercredit = 500.00

  tuition = costpercredit * credits
  c = c + 1
  totaltuition = totaltuition + tuition

  print("Student:", lastname)
  print("Credits taken:", credits)
  print("Tuition:", tuition)
  print("  ")

  lastname = str(f.readline().rstrip('\n'))

f.close()

print("Number of students: ", c)
print("Total tuition: ", totaltuition)
