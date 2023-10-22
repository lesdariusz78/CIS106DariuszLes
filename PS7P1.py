totalInterest = 0.0
print("Do you want to calculate interest?")
response = input()
while response == "Yes":
    print("Enter the principle amount:")
    principle = float(input())
    print("Enter interest rate ")
    rate = float(input())
    print("Year    " + "Beg Balance    " + "End Balance    ")
    for year in range(1, 5 + 1, 1):
        intAmount = principle * rate
        endBalance = principle + intAmount
        print(str(year) + "              " + str(principle) + "              " + str(endBalance))
        totalInterest = totalInterest + intAmount
        principle = endBalance
    print("Do you want to continue (Yes or No)")
    response = input()
print("Total Interest Earned: " + str(totalInterest))
