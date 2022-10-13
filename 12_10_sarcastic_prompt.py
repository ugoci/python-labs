# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

statement = "Kim Kardashian and Saturday Night Live alum Pete Davidson have decided to break up and end their romantic relationship."
print(statement)

your_opinion = input("what is your opinion on this breaking news story?: ")

for char in your_opinion:
    num = your_opinion[0:]   #tried to turn the characters into int so that I can capitalize even numbers 
    even_number = num % 2
    print(num)
    
    if char is even_number:
        (your_opinion[num].upper())
    else:
        (your_opinion[num].lower())

    print(your_opinion)
   