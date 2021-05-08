# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the
# counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    if not line.startswith("From") or line.startswith("From:"): continue
    words = line.split()
    hour = words[5].split(":")[0]
    count[hour] = count.get(hour, 0) + 1

lst = list()
for k, v in count.items():
    lst.append((k, v))
lst.sort()

for pair in lst:
    print(f"{pair[0]} {pair[1]}")
