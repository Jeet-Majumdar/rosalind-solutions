DNA_string = 'ACGATGGTCTCTGAGTTCTTTATATTGTTGGCTTCGATGCGCGTATCAAATCGAACTTATGTCGGTGAAATGAGTGGCACAAGTGTGCACGACGCGCTTCCATTGCTGTTTTCATCGCTGGATGCATAGCCATTGGTGCACGGATCGTACATCATCCTAGTCTCCGTCGGTCACGGTTGGCTACTTTGTTGGCAAATTGACGACCCTGTGGGTCTTCTAACACCCATGACATGTAAAGGGCCTACATAGTACGCGGAAGGGTCTCTTCTAGTTGCTCGGACATGACAAGCTGGCTAATCGAGTATTGTTTACTGGGGCACTACGTCCGCTAATGAAAGTCTGGTCTAAGTCTGCATATTGTAGAGGTCTCGGGATACCTGCATAGCTCTTGAATCATCAAAGTACCTGTGTCGGAAGTCGGGTTCCATAAAAGGTCCTGCCGAGGCAAGCGTGGCCGGACGCCTGAGCTGTAGCCGTCGGACCAAAGGAAAACGAATCATGTGCACTGCCGGCTTAGGGCTTCAACCAGGTGTCGAACTTTGCGAGATATGTCGAGATGCCAAACATCCCCACACACACAAAAATTGCGAAGTAACCTCTCTCGTCCCAGAAGGCACTTGTCAAGTCCTCGTAGAGGTCATCCTGTCCTAAAGTCACCGCGATGATGTCTCTTTGGCGTTCGACTATACCGGGGACCAGCCTTCTTTAAACCTACCAAGTTTGGACTAGTAACGCCCGAATCCTAGCGCATTTGAAACGCTGATGTGTGTAATCACTTGGTTCGTTTACGCTGATCCTCTACTGATGTAGCCATGGTTTTATGCGTATGGCACAAATATTGCGACCACTCGTACCGAACAGACATGGACCCGATGACTTCCGCCACCATTAAGTGTGTAAGATATCCGTGTCTAGTAAAGCGAACTAGGGTGCTGCATTTTATGTGTTCATCTGATTACGGTTGTCACAGCTACCTAGATGCAAC'

result = ''
for nuc in DNA_string:
    
    if(nuc == 'T'):
        result = result + 'U'
    else:
        result = result + nuc

print(result)
