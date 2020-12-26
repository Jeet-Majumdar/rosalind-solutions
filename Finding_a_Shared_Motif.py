import re

# Import and manipulate the given DNA strings
f = open("rosalind_lcsm.txt")
dna = f.read()
f.close()
dna = dna.split('>') # Number 0 is an empty string
for a in range(0, len(dna)):
    dna[a] = re.sub('[^GCAT]', '', dna[a])

string_1 = dna[1]
string_rest = dna[2:]
length = len(dna[1])
string = ''

#starts with the whole string and decrements from both ends
for i in range(1, length):
    for x in range(length, i+len(string), -1):
        s1 = string_1[i:x]
        match = True
        for s2 in string_rest:
            if s1 not in s2:
                match = False
                break
        if match:
            string = s1
            break

print(string)
