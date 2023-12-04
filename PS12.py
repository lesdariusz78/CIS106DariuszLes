def dl1(mylist):
  n=int(input("Enter the number of elements in the list: "))
  for n in range(0,n,1):
    s=int(input("Enter an integer: "))
    mylist.append(s)
  return(mylist)
def displaylist(mylist):
  for item in mylist:
      print(item)  

mylist=[]
mylist=dl1(mylist)
print(mylist)

"dl2"
mylist.insert(0,99)
print(mylist)

"dl3"
mylist[0]=100
print(mylist)

"dl4"
mylist2=[500,600,700,800,900]
print(mylist2)
mylist.extend(mylist2)
print(mylist)

"dl5"
mylist.remove(800)
print(mylist)

"dl6"
mylist.pop(2)
print(mylist)

"dl7"
grades= ["A", "B", "C", "A", "A", "C"]
print(grades)

"dl8"
print("A appears", grades.count("A"), "times")

"dl9"
print("The position of the first B is",grades.index("B"))

"dl10"
look_for= "F"
if look_for in grades:
  print(look_for, "was found in the list")
else:
  print(look_for, "was not found in the list")

"dl11"
mylist2.clear()
print(mylist2)

"dl12"
del mylist2
#print(mylist2)

"dl13"
players= ["Rizzo", "Davis", "Baez", "Happ" ,"Bryan"]
print(players)

"dl14"
players.sort()
print(players)

"dl15"
players2=players.copy()
print(players2)

"dl16"
players2.reverse()
print(players)
print(players2)

