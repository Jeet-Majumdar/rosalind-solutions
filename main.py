from DNAToolkit import *
import random

DNAstring = 'CTACGATCATGCGAGCGTGGGTAGGGGTCGCAGTCGCTGCAAGTGCGAATAAAGATATCATTCATATATATTCGTTCTTCGATGCATCCTCAATTATTATTCTGACATGGGCGGAGTCCCTTTGATGATACCCAGAGTGCGGGAGGCTACGTATGTTAGCGCCTAGTTAACACGCTTTCTGAGAGTATAAGGCCGGGGCTCCGGGATGTTATACTAAAGATTGCCCCGGAGCACTATTAATTCTTGGCGGGCCATCCAAGCGTCTGCCACAGTCCGGAAAGACACCCCTGTCTTTGGCATAAGACCCGCTCAGGACGTATAAGAGCACCGATAAGAGAGCGAACGTCAATATGAGCGCCTGACACCCTATCAAGAGGGTCGAAATCACCCTTAACGGGGAAGCATGCTTCGGGACTGCCTAATGATAATTATTCAGGCCGCTAAATTTCTACATGTCTTAGCGTATGTAAAATGACTAACTCAAGAAAAATAGTGGCAAAGCTTCGCTGGAATCCTAAGAATGCCAGGCGCTATATAGGCGGTCCTAAAAGTCAAGTTGCATACACCCGGATGCGATTAAGGGGGCAAAAGTGCGTTAGAAAGTTGTGTCCAGTCTGGAACTTTCCGCGGGTTAAACCACCGCGTGGTGTGGTTGATTATTCATAGCGCTTTTACTGGGTATAAGTAGGTTGTGGCGGAAAACAGACCATTAAGGCGTGGCTGGATATGTACGTACCAGTAAAGAACCCAAGTGCATTAGCAATCTGTTCTGACTGAACGCAGTGAATTTACAAACTTGCCGTCTAGTTCGCACATCA'

print(validateSeq(DNAstring))

#Creating a random DNA Sequence for testing
#randomDNA = ''.join([random.choice(Nucleotides) for nuc in range(20)])

print(validateSeq(DNAstring))

result = countNucFrequency(DNAstring)
print(' '.join([str(val) for key, val in result.items()]))