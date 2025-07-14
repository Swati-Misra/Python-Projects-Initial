# Prompt the user for the file name
filename = input("Enter file name: ")

try:
    # Open the file
    with open(filename, 'r') as file:
        # Read through the file and print contents in upper case
        for line in file:
            print(line.upper().strip())
except FileNotFoundError:
    print("File cannot be opened:", filename)