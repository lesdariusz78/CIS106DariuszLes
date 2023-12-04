def displayarray(lname):
  for i in range(0,10,1):
    print(lname[i])

def reversedisplay(lname):
  for i in range(9,-1,-1):
    print(lname[i])


lname=["Adams","Baker","Clark","Davis",
       "Evans", "Frank", "Ghosh", "Hills", "Irwin", "Jones"]
 
displayarray(lname)
print()
print ("Names in reverse order:")
reversedisplay(lname)