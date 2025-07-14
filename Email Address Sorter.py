#filename enter
fname=input("Enter the filename: ")

try:
    fhand=open(fname)
except FileNotFoundError:
    print("File not found!", fname)

count=0

#process each line
for line in fhand:
    line = line.strip()             # line is a string
    if line.startswith('From '):    # check before splitting
        words = line.split()        # now split into a list
        if len(words) >= 2:
            print(words[1])         # second word is the email
            count += 1

print("There were", count, "lines in the file with From as the first word")