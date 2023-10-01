WidQty= float(input("Enter quantity of widgets: "))

if WidQty>10000:
  Price=10.00
elif WidQty>5000:
  Price=20.00
else:
  Price=30.00

ExtPrice=WidQty * Price
Tax= ExtPrice * 0.07
Total= ExtPrice + Tax

print("The extended price is $ ",ExtPrice)
print("Tax is $ {:.2f}".format(Tax))
print("Total is $ ", Total)

  