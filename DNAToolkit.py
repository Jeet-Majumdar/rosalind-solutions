import collections

Nucleotides = ['A', 'C', 'G', 'T']

#Check the sequence to make sure that it is a DNA string
def validateSeq(dna_seq):
    tempSeq = dna_seq.upper()
    for nuc in tempSeq:
        if nuc not in Nucleotides:
            return False
    return tempSeq


def countNucFrequency(seq):
    tempFreqDict = {'A':0, 'C':0, 'G':0, 'T':0}

    for nuc in seq:
        tempFreqDict[nuc] += 1
    
    return tempFreqDict 
    #return dict(collections.Counter(seq))

    