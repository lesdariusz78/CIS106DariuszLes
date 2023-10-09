NumOfStudents=0
print("Do you want to participate in the program? ")
Response=input()

while Response=="Yes":
  NumOfStudents=NumOfStudents + 1
  LastName=input("Enter student's last name: ")
  ScoreExam1=float(input("Enter your score for Exam1: "))
  ScoreExam2=float(input("Enter your score for Exam2: "))
  AvgExScore=(ScoreExam1 + ScoreExam2)/2
  print(LastName, " average exam score is ", AvgExScore)
  print("Do you want to participate in the program? ")
  Response=input()

print("Number of students that participated in the program: ", NumOfStudents)
  
  
  
  

