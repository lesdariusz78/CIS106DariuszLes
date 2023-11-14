def Discount(qty, price, discrate):
  total = qty * price
  discamt = total * discrate
  discprice = total - discamt

  return discprice, discamt


qty = float(input("Enter quantity:  "))
price = float(input("Enter price:  "))
discrate = float(input("Enter discount rate:  "))

discprice, discamt = Discount(qty, price, discrate)

print("The unit price is: ", price)
print("The quantity ordered is: ", qty)
print("Discount amount: ", discamt)
print("Discounted price: ", discprice)
