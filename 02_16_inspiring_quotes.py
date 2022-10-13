# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname



from posixpath import split


famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]
#go through each item in the famous quotes list 
#each item is a dictionary 
#identify the key and value of each dictionary 
#print them in a new order based on the key and value 

x = len(famous_quotes)

for i in range(x):
    each_quote = famous_quotes[i]
    name_organiser = split(each_quote["full_name"])
    #print(name_organiser)
    print(f"{each_quote['quote']}, {each_quote['full_name']}")

