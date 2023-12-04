def loadarrays(lname3,battavg):
  with open("battavg.txt", "r") as f:
     for _i in range(0,10,1):

       lname3.append(f.readline().rstrip("\n"))  
       battavg.append(f.readline().rstrip("\n"))


def darrays(lname3,battavg):
    for i in range(0,10,1):
        print (lname3[i],"has a batting average of",battavg[i])

def searchname(lname3,battavg,searchlname):
  foundsub=-1
  for i in range(0,10,1):
    if lname3[i]==searchlname:
      foundsub=i

  if foundsub==-1:
      print("Name not found")
  else:
      print (lname3 [foundsub],"has a batting average of",battavg[foundsub])
lname3=[]
battavg=[]
loadarrays(lname3, battavg)
darrays(lname3, battavg)

response=input("Do you want to search for last name? (Yes or No)")
while (response=="Yes"):
  searchlname=input("Enter last name to search for: ")
  searchname(lname3,battavg,searchlname)
  response=input("Do you want to search for last name? (Yes or No)")
