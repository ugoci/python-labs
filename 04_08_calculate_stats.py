# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(l):
  largest_num = max(l)
  smallest_num = min(l)
  the_sum = sum(l)
  avgerage = sum(l) / len(l) 
  return largest_num, smallest_num, the_sum, avgerage

# call the function below here
print(stats(example_list))
