# Use a list comprehension to create a list that contains the individual
# letters of the word "codingnomads":
# ['c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's']
#
# Note: You can solve this more quickly with a call to `list()`
# but try to do it using a list comprehension.

word = "codingnomads"
empty_li = []

for i in word:
    #print(i)
    empty_li.append(i)
#print(empty_li)

comp = [empty_li.append(i) for i in word]
comp2 = [i for i in word if empty_li.append(i)]

print(comp2)
