# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:

#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

#option 1
count10 = (" 0  1  2  3  4  5  6  7  8  9")
count20 = ("10 11 12 13 14 15 16 17 18 19")
count30 = ("20 21 22 23 24 25 26 27 28 29")
count40 = ("30 31 32 33 34 35 36 37 38 39")
count50 = ("40 41 42 43 44 45 46 47 48 49")
print(count10, count20, count30, count40, count50, sep= "\n")

#option 2
numtab = """
  0  1  2  3  4  5  6  7  8  9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49 
"""
print(numtab)

#option 3
stringer = range(50)

for char in stringer:
  if char % 10 == 9:
    print(char)

  else:
    print(char, end= " ")
    

  


