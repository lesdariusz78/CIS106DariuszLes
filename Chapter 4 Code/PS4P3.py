print("Input the number of books ordered: ")
booksOrderedQty = int(input())
print("Enter the cost per book:")
costPerBook = float(input())
orderTotal = booksOrderedQty * costPerBook
if orderTotal > 50:
    shipp = 0
else:
    shipp = 25
print("The order total is $" + str(orderTotal))
print("The shipping cost is $" + str(shipp))
