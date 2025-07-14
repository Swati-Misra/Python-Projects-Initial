#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.You can download the sample data at http://www.py4e.com/code3/romeo.txt

#filename enter
fname=input("Enter the flename: ")

try:
    fhand=open(fname)
except FileNotFoundError:
    print("File not found!", fname)

word_list=[]

#read file line by line
for line in fhand:
    words=line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)

#alphabetical order
word_list.sort()

print(word_list)