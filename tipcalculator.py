total_bill = float(input("What was the total bill? $ "))
people = int(input("How many people to split the bill? "))
tipinpercent = float(input("What percent tip would you like to give? Do not add any % sign, add only number "))

payable = (total_bill + ((tipinpercent*total_bill)/100))/people

print("Each person should pay: $" + str(format(payable,".2f")))