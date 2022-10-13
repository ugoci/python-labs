# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

num = range(0, 1000000000)
your_number = int(input("guess a number:    "))

while your_number:
    if your_number in num:
        print(your_number)
        print("your number is in here")
        break
    
    else:
        print("your number is not in here")
