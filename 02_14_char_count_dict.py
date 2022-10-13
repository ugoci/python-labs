# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

# Hello Ugo :)  
# Here we do not necessarily need the while loop here , but it is actually fine , so I guess 
# you want it to run continiously for the gamer. But then you should also find how to stop it 
# , maybe you can ask the user if they want to continue. 
# So for the below code; when you split the user input you are getting a list of words ( strings ) like below
['hello', 'Ugo']
# And the instructions are asking to map the characters ( not the words ) to the number of times they occur. 
# As you know we can loop through a string 
# also you need to initialize an empty dictionary  after you get the user input , but definitely before you start looping through the input.
# and finally you might need nested for loops , first for your list , second for the strings 
# And during the loop you need to check if your letter is already in the dictionary , if yes increase the frequency , if not just add it to the dictionary.
# At the end , when the looping is over , print the dictionary you have created ! 


user_input = input("say something:")
my_dict = {} 

for i in user_input:
    #print(i)
    frequency = user_input.count(i)
    my_dict[i] = frequency

print(my_dict)










