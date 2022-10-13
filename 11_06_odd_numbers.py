# Using a `for` loop, print out all odd numbers from 1 to 100.

for num in range(100):
    even_number = num % 2
    
    if (num != even_number) and (even_number != 0):
        print(num)

