def CompAV(MV, AVp):
  AV = AVp * MV
  return AV


TotalMV = 0
TotalAV = 0

print("Do you want to calculate assessed value of your home?(Y/N)")
response = input()
while response == "Y":
  print("Enter the county name: ")
  County = input()
  if County == "Cook":
    AVp = .9
  elif County == "DuPage":
    AVp = .8
  elif County == "McHenry":
    AVp = .75
  elif County == "Kane":
    AVp = .6
  else:
    AVp = .7

  print("Enter the market value of your home: ")
  MV = float(input())
  AV = CompAV(MV, AVp)

  TotalMV = TotalMV + MV
  TotalAV = TotalAV + AV

  print("The assessed value of your home is: ", AV)
  print("Do you want to calculate assessed value of your         home?(Y/N)")
  response = input()

else:
  print("The sum of market values is: ", TotalMV)
  print("The sum of assessed values is: ", TotalAV)
  print("Thank you for using this program.")
