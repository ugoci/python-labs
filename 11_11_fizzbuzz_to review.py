# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

#n = str(input("any number: "))

for char in range(20):
    print(char)
    
    if char % 3 == 0:
        print("Fizz")
        continue

    if char % 5 == 0:
        print("Buzz")
        continue

    if char % 3 and char % 5: 
        print("FizzBuzz")
        continue
