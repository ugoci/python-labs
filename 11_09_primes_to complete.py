# Print out every prime number between 1 and 1000.

#go through the range of numbers from 1 - 1000
#identify the prime numbers (prime numbers are numbers that are divisible by 1 and themselves)
#display the prime numbers 

prime = True 
num = range(1,1000)

while prime:
    even = (num % 2 == 0)
    if num != even:
        print(num)

    elif num == even and num > 1000:
        prime = False
        print("end")

