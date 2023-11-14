total=0
tax=0
def comptotal(qty,price):
    global total
    total=qty*price
    global tax
    tax=total*.07
    return  
  

qty=float(input("Enter ordered quantity: "))
price=float(input("Enter price per unit: "))
comptotal(qty,price)
print("Total: ",total)
print("Tax: ",format(float(tax),'10,.2f'))