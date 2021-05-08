import re
filename = input("enter file name: ")
print(sum([int(n) for n in re.findall('[0-9]+', open(filename, 'r').read())]))
