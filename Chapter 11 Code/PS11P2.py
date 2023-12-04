def displayarray(lname,score):
  for i in range(0,10,1):
    print(lname[i],"has a score of", score[i])


lname=["Adams","Baker","Clark","Davis",
       "Evans", "Frank", "Ghosh", "Hills", "Irwin", "Jones"]
score= [85,68,94,97,45,76,12,78,89,98] 
displayarray(lname,score)