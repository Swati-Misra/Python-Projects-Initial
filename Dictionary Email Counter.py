#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#ask filename
fname= input("Enter a filename: ")

#open a filename
try:
    fhandle=open(fname)
except:
    print("Filename nout found: ", fname)
    quit()

#dictionary
counts= {}

for line in fhandle:
    if line.startswith("From "):
        words=line.split()
        email= words [1]
        counts[email]=counts.get(email, 0)+1

#highest number of sender
maxsender=0
maxcount=0
for sender, count in counts.items():
    if maxcount is None or count>maxcount:
        maxsender=sender
        maxcount=count

print("Maxsender is ", maxsender)
print("maxcount is ", maxcount)
