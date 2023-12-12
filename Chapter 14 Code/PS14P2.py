class Car:
  def __init__(self, make, model,sticker_price):
    self.make = make
    self.model = model
    self.sticker_price = sticker_price
    self.discounted_price = .9*sticker_price


class Sport(Car):
  def __init__(self, make, model,sticker_price):
    super().__init__(make, model,sticker_price)

    
  def SportWheels(self):
    pricewithoptions=self.discounted_price +1000
    return pricewithoptions
 
  def SportEngine(self):
    pricewithoptions=self.discounted_price +3000
    return pricewithoptions

  def SportInterior(self):
    pricewithoptions=self.discounted_price +2000
    return pricewithoptions

car1=Sport("Ford","Mustang",50000)
car1.SportEngine()
car2=Sport("Dodge", "Charger",60000)
car2.SportWheels()
car3=Sport("Chevrolet", "Corvette",70000)
car3.SportInterior()
car3.SportEngine()
car3.SportWheels()
car4=Car("Toyota", "Corolla",25000)

print (car1.discounted_price)
print (car1.SportEngine())
print (car2.discounted_price)
print (car2.SportWheels())
print (car3.discounted_price)
print (car3.SportInterior())
print (car3.SportEngine())
print (car3.SportWheels())
print (car4.discounted_price)
      

 