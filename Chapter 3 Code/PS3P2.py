#input phase
PurchasePricePerShare=float(input("Enter the purchase price per share: "))
CurrentStockPrice=float(input("Enter the current stock price: "))
StockQty=int(input("Enter the quantity of shares: "))
#process phase
StockValue=(CurrentStockPrice-PurchasePricePerShare) * StockQty
#output phase
#Check if value is positive
if StockValue > 0:
    print("I am earning money")
else:
    print("I am losing money")