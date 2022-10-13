# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

empty_list = []

user_input = input("say something:")

for e in user_input:
    turnit = user_input.split()
    print(turnit)
    for i in turnit:
        tuplit = tuple(i)
        #print(tuplit)
    #breakwhats
        empty_list.append(tuplit)
        print(empty_list)
    break
