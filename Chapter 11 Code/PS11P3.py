def loadarrays(lname2,score):
  with open("scorefile.txt", "r") as f:
     for i in range(0,10,1):

       lname2.append(f.readline().rstrip("\n"))  
       score.append(f.readline().rstrip("\n"))

    
def darrays(lname2,score):
    for i in range(0,10,1):
        print (lname2[i],"has a score of",score[i])
      

lname2=[]
score=[]

def hilow(lname2,score):
  hiscore=0
  lowscore=101
  lowsub=0
  hisub=0
  for i in range(0,10,1):
    if float(score[i])>float(hiscore):
      hiscore=score[i]
      hisub=i
    elif float(score[i])<float(lowscore):
      lowscore=score[i]
      lowsub=i
  print("Highest score is",hiscore,"by",lname2[hisub])
  print("Lowest score is",lowscore,"by",lname2[lowsub])

loadarrays(lname2, score)
darrays(lname2, score)
hilow(lname2, score)