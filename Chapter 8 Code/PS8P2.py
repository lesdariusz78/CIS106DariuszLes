def CompBattAvg(hits,at_bats):
  battavg=hits/at_bats
  return battavg

c=0
  
lastname=input("Enter player's last name: ")
while lastname!="":
  hits=int(input("Enter the number of hits:  "))
  at_bats=int(input("Enter the number of at bats: "))
  battavg=CompBattAvg(hits,at_bats)

  c=c+1
  print("Player's last name: ",lastname)
  print(lastname,"has a batting average: ",battavg)
  print("")
  
  lastname=input("Enter  player's last name: ")
  
print("Number of players entered: ",c)