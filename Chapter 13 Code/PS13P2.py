class Student:
    def __init__(self,first,last,distcode,credits):
        self.first = first
        self.last = last
        self.distcode = distcode
        self.credits = credits

    def tuition(self):
     if self.distcode == "I":
            tuition = self.credits * 250.00
     elif self.distcode=="O":  
            tuition=self.credits * 500.00
     else:
       tuition=0.00

     return tuition  
      
stu1 = Student("John","Smith","I",15)
stu2 = Student("Dariusz","Les ","O",12)

print(stu1.first,stu1.last,stu1.distcode,stu1.credits)
print(stu1.tuition())
print(stu2.first,stu2.last,stu2.distcode,stu2.credits)
print(stu2.tuition())
          