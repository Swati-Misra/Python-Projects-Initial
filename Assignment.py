#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. 
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Open the file
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

# Create a dictionary to hold hour counts
hour_counts = {}

# Loop through each line in the file
for line in fhand:
    line = line.strip()
    if line.startswith("From "):
        parts = line.split()
        time = parts[5]  # Time is the 6th part in 'From ' lines
        hour = time.split(":")[0]  # Split time at ':' and take the hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort the dictionary by hour and print the counts
for hour, count in sorted(hour_counts.items()):
    print(hour, count)
 

