# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")


try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found error", fname)
    quit()
count=0
t=0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        colon=line.find(":")
        number=float(line[colon+1:].strip())
        count=count+1
        t=t+number

if count>0:
    average=t/count
    print ("Average spam confidence:", average)
else:
    print("No 'X-DSPAM-Confidence' lines found.")