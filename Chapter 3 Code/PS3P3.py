#input phase
Total=float(input("Enter the total cost of the meal: "))
#process phase
Fifteen=Total * .15
Eighteen=Total * .18
Twenty=Total * .20
#output phase
print("For 15% tip:")
print("Total:",Total)
print("Tip:",Fifteen)
print("Total with tip:",Total+Fifteen)
print(" ")
print("For 18% tip:")
print("Total:",Total)
print("Tip:",Eighteen)
print("Total with tip:",Total+Eighteen)
print(" ")
print("For 20% tip:")
print("Total:",Total)  
print("Tip:",Twenty)
print("Total with tip:",Total+Twenty)
