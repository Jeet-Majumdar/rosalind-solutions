DNA_string1 = 'TAGGTTTCAGGGCGAGTATGAACATGTCCCCTGGTTCGATGCGACGTCCCAGGGGGGTTGTCGCAAGTCTGCTCGCATGTAATTGCGGGTATTTCACCGGTCGAACGATTAGTTGTCAACATCGCGGACACACGAGCTGGCATATGATTCTTCGATTTACGCGGAAGGACTTCCTCTGACGGTACCTGAAAAGGGATGATAGTCTAGATCTAAAAAATTCGACCTAACGGGTAGGTACCAGCTTCACCCCATTTATAGCAAAATCTTCCGCAATCGCCAATTCGATGCTTCTGGGTAAAGATCGGGGCAAACCTAATTAACGTAGTAAACCCACCAGAAAACGCTGTATTTACGAGAGCACAGTCGCCGGTTTCCGTTCTCTTAAAAAGTCGCCGGGAGCTTGAGTGTTGTGCTCGTTCCCGGGCTACCCGCTCTCTACAAATATAAAGTTCTTTGCCCACGCTATGCAGGTTAAATCTAGCACCTCGTCGATAGCTGTCAACCATCGCTAGATATTTGTACTTGGCCCTGGTACTTGTCCCCTGTCGTGTTTGCATAGGTGCTCTGGTGTACTCAGGCAGCGATGTGCTTGACGTTTGAGAATTGGCGCCCCCCGATATGCGGCTTGGGTTGATTCACCCTTAATTTGAGTCTTTCGGAATCGTCTGTGGGCAACATTATTACTAATGAGCTAATGAGGTAGAATGGAGGCAGGTGTCTTCCCGTGTCGTCCTTGCTCCGAACGGATATGAGCCACTCGTAATTATACATAGGATCAGGACATTCAGAGTAACCAGAGAATAGGATGCCCATGCGGTGCACCCTCAATACACCGGGTGCGAGACAATAGGATACCGTCATGCTGAGGACTCACTGTTCCTCGGATTCAAAGATGTTTCCAATGAATCGTCTAGACAACCCAACCCCGTTTTCGGTCAAGGCCTGGAACTTGTTCCTGCA'

DNA_string2 = 'TCATGAATAGGACGAATCAACATGTGGTGCCTGGTTGTAACTTTCGTCCGAGAATGGTCCGGGCCAGACCGATGGCCTGTATTGGGAAGTAACTACACACGTGAAGGAATATGTTCCAACACGGCCGTCGTATTTTCTGGCATATGGTTTTTTCATCTACGCCCAGTACACCGCAGTACTACAACCTTTTACTGTCTGGCAGTCTCCATCGCATAAATCCTGCCTCTCAGACAGCACACATGTAGTGTGCATCGAAACCGCAATCTGAAGCATACGGCTATAGAATGTTTTGCGGATTGCATCGGACCTAATACAAATCTATTCCTATTCATAACTGAACAAACAGTATTCACTAAAGCGCAATCGACCTTCACCGGACTCTCTAACTTCCGCGGGCCGACACAAAGGTGGGGTCGATCCGGAGAGAACAGCGGTCTCCCCAGGTAGTGATATTTCGCAACGATCTGTAGGTTGCTTTTAACACCGTAGAGATTACAAGCGGTCAGTACTATACGCGTTGTTCATGCCCGCGTTCATGTTACCTTTATACTTTAATGAGAGGATGTGCTGTATCCAGTTCACGATACTACTAACTAAAGATGTATGTCGACTCGCGCTTTCAGCCATCGGTCGAACCTCACGCAGATTGAGTCACACCGACCTGTAAGAGGGCAAAGTTATAGTGAGTCCCCTAATGGGGTATTACGCACGCTCGTGGCATTTGGAGCACTCCGTTCTATCAAGAACGCTGCGCAGCTGGAGACTATACCGCGTATTAGTGGTTTGCACATTGCCAGCGACAGAGGTCCCAAGTTTGTAAAATCAATCCACTGAGGGTTCGAGACTTTACAAGCTTTGGCCGAGCGGAAACCAACGTTACTCGCAATCAACGTTGGCAGGGTCCTATCTCCGTGGTCAACTAATCGCGATATAGGTTACACTGCGGAAAGTTTACCTAAT'

point_mutations = 0

for index in range(len(DNA_string1)):
    
    if(DNA_string1[index]!=DNA_string2[index]):
        point_mutations = point_mutations + 1

print(point_mutations)