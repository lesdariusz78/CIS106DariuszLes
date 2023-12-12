class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self,rate):
        b = float(rate) * float(self.pay)
        return b
class Manager(Employee):
    def __init__(self,first,last,pay):
        super().__init__(first,last,pay)

    def bonus(self):
      b=.40*float(self.pay)
      return b 


empl1=Employee('Dariusz','Les',50000)
man1=Manager('John','Smith',100000)

print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.bonus(0.10))
print("")
print(man1.email)
print(man1.first)
print(man1.last)
print(man1.pay)
print(man1.bonus())
                  



      