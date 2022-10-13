# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

collector = True 
counter = 0 
empty_list = [ ]

while collector:
    user_numbers = input("Give a number:")
    counter = counter + 1 
    adder = empty_list.append(user_numbers)
    print(empty_list)
    if counter == 10:
        collector = False 
        for n in empty_list:
            print(empty_list[1])
            print(empty_list[3])
            print(empty_list[5])
            print(empty_list[7])
            print(empty_list[9])
            print(empty_list[8])
            print(empty_list[6])
            print(empty_list[4])
            print(empty_list[2])
            print(empty_list[0])
    

