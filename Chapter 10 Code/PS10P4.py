def bowlscore(score1,score2,score3,handicap):
  total=score1+score2+score3
  avgscore=total/3
  haverage=(total+handicap)/3
  return avgscore,haverage

lastname=input("Enter bowler's last name: ")
score1=float(input("Enter bowler's first score: "))
score2=float(input("Enter bowler's second score: "))
score3=float(input("Enter bowler's third score: "))
handicap=float(input("Enter bowler's handicap: "))
avgscore,haverage=bowlscore(score1,score2,score3,handicap)
print("Bowler's last name: ",lastname)
print("Bowler's average score: ",avgscore)
print("Bowler's handicap average score: ",format(float(avgscore),'10,.2f'))