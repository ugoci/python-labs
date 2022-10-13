# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

invest_program = True

while invest_program:
    investment_amount = float(input("what amount would you like to invest in USD: "))
    interest = float(input("whaht are the current interest rates in %: "))
    interest_rates = float(interest / 100)
    investment_term = float(input("how long would you like to hold your investment in years: "))
    future_value = investment_amount + (investment_amount * (interest_rates * investment_term))
    print("the future value of your investment is: $", future_value,)
    new_investment = input("would you like to calculate another investment? type yes or no: ")
    print(new_investment)
    
    if new_investment == "yes":
        continue
    
    if new_investment == "no":
        print("thank you for using our service. the program will shut down now")
        break

