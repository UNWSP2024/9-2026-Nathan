# By Nathan Nelsen
# Written 3/27/26
# Random Number File Writer

# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

import random

import random

try:
    num_count = int(input("Enter a number of random numbers to generate (1-1000): "))
    if not (1 <= num_count <= 1000):
        print("Error. Please enter a number between 1 and 1000")
    else:
        filename = "random_numbers.txt"
        with open(filename, "w") as file:
            for _ in range(num_count):
                rand_num = random.randint(1, 500)
                file.write(str(rand_num) + "\n")
        print(f"{num_count} random numbers have been written to {filename}.")
except ValueError:
    print("Error. Please enter a number between 1 and 1000")
