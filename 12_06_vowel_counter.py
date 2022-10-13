# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

story = input("tell a story: ")
vowel = ("a", "e", "i", "o", "u")

for vowel in story:
    if vowel in story:
        print(vowel)
        appearances = story.count(vowel)
        print(appearances)
