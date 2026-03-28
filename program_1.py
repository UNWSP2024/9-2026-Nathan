# By Nathan Nelsen
# Written 3/27/26
# Item Counter

# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

def count_file_lines():
    try:
        # Open the file in read mode
        with open("names.txt", "r") as file:
            lines = file.readlines()
            count = len(lines)
        print(f"The number of names in the file is: {count}")
    except FileNotFoundError:
        print("Error: 'names.txt' not found on disk.")


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
