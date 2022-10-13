# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

num = range(0, 50)
guess_number = int(input("guess a number:    "))

for i in num:
    guess_number == num
    divide = guess_number % 3
    result = guess_number / 3
    
    if divide == 0 and (guess_number <= 50):
        print("yes, the input", guess_number, "is divisible by 3")
        print("the result is:", result)
        break
    
    elif (divide != 0) and (guess_number <= 50):
        print("unfortunately the input", guess_number, "is not divisible by 3")
          
    else:
        if guess_number > 50:
            print("user input is out of range.\n the program will stop running now")
            break
            


        
