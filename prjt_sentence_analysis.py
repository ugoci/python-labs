#Sentence Analysis Tool
#Write a script that takes a sentence from the user and returns:

#the number of lower case letters
#the number of uppercase letters
#the number of punctuations characters
#the total number of characters
#Use a dictionary to store the count of each of the above.

#Note: ignore all spaces.

#Example input:

#I love to work with dictionaries!
#Example output:

#Upper case: 1
#Lower case: 26
#Punctuation: 1
#Total chars: 28

#user_input = input("say something:")


the_word = input("say something:")
dict1 = {"Upper case": ""}
dict2 = {"Lower case": ""}
dict3 = {"Punctuation": ""}
dict4 = {"Total chars": ""}
total_chars = 0
upper_counter = 0
lower_counter = 0
dict_list = []

for i in the_word:
    total_chars = total_chars + 1
    if i.isupper():
        upper_counter = upper_counter + 1
    if i.islower():
        lower_counter = lower_counter + 1

dict1["Upper case"] = upper_counter
dict_list.append(dict1)
dict2["Lower case"] = lower_counter
dict_list.append(dict2)
dict4["Total chars"] = total_chars
dict_list.append(dict4)

print(dict_list)
    