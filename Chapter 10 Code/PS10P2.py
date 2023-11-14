def exam(score1,score2,score3):
  exampoints=score1+score2+score3
  avgpoints=exampoints/3
  return avgpoints,exampoints

lastname=input("Enter the student's last name: ")
score1=float(input("Enter the Exam1 score: "))
score2=float(input("Enter the Exam2 score: "))
score3=float(input("Enter the Exam3 score: "))
avgpoints,exampoints=exam(score1,score2,score3)

print("The average points is: ",format(float (avgpoints),'10,.2f'))
print("The total points is: ",exampoints)
  
  