fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

d = dict()
lst = list()

for lines in fh:
    line = lines.rstrip().lower()
    words = line.split()
    for w in words:
        for char in w:
            if char.isalpha():
                d[char] = d.get(char,0) + 1


newsort = sorted(d.items())
for v, k in newsort:
    print(v, k)

print(' ')


##code to sort dictionary by value
sortchar = sorted(d.items(), key=lambda item: item[1])
for v, k in sortchar:
    print(v, k)
