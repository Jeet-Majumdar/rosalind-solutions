import codon_map

f = open("rosalind_orf.txt", "r")

DNAstring_main = ""
for line in f:
    x = line.strip(" \n")
    if (x[0]==">"):
        continue
    else:
        DNAstring_main = DNAstring_main + x

#print(DNAstring)

out = []

# Forward
for case in range(3):
    DNAstring = DNAstring_main[case:]

    RNAstring = ""
    for nuc in DNAstring:
        
        if(nuc == 'T'):
            RNAstring = RNAstring + 'U'
        else:
            RNAstring = RNAstring + nuc

    #print(RNAstring)


    codons = [RNAstring[i:i+3] for i in range(0, len(RNAstring), 3)]

    #print(codons)

    start_index = []

    for i in range(len(codons)):
        if(codons[i] == "AUG"):
            start_index.append(i)

    stop_index = []

    for i in range(len(codons)):
        if((codons[i] == "UAG") or (codons[i] == "UGA") or (codons[i] == "UAA")):
            stop_index.append(i)

    pairs=[]
    for i in start_index:
        for j in stop_index:
            if (i < j) and (i !=j):
                pairs.append(i)
                pairs.append(j)
                break


    p = 0 
    while (p < len(pairs)):
        start = pairs[p]
        stop  = pairs[p+1] 
        p = p + 2
        
        # start+1 to j should be extracted from codons list
        string = ''.join(list(map(codon_map.codon_function, codons[(start):stop])))
        out.append(string)

def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

# Reverse Complement:
for case in range(3):
    DNAstring = reverse_complement(DNAstring_main)[case:]

    RNAstring = ""
    for nuc in DNAstring:
        
        if(nuc == 'T'):
            RNAstring = RNAstring + 'U'
        else:
            RNAstring = RNAstring + nuc

    #print(RNAstring)


    codons = [RNAstring[i:i+3] for i in range(0, len(RNAstring), 3)]

    #print(codons)

    start_index = []

    for i in range(len(codons)):
        if(codons[i] == "AUG"):
            start_index.append(i)

    stop_index = []

    for i in range(len(codons)):
        if((codons[i] == "UAG") or (codons[i] == "UGA") or (codons[i] == "UAA")):
            stop_index.append(i)

    pairs=[]
    for i in start_index:
        for j in stop_index:
            if (i < j) and (i !=j):
                pairs.append(i)
                pairs.append(j)
                break


    p = 0 
    while (p < len(pairs)):
        start = pairs[p]
        stop  = pairs[p+1] 
        p = p + 2
        
        # start+1 to j should be extracted from codons list
        string = ''.join(list(map(codon_map.codon_function, codons[(start):stop])))
        out.append(string)




out = list(set(out))

for a in out:
    print(a)