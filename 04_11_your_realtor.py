# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def advert():
    place = input("say the location: ")
    num_rooms = input("how many rooms does it have?: ")
    price = input("how much does it cost?: ")
    return print(f"the apartmnet is in {place}, it has {num_rooms} rooms and is on the market for ${price}")

customer1 = advert()

