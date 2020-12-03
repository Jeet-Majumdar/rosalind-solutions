#import numpy as np

def gen_profile_matrix(DNA_array):
    str_len = len(DNA_array[0])
    A = [0 for i in range(str_len)]
    C = [0 for i in range(str_len)]
    G = [0 for i in range(str_len)]
    T = [0 for i in range(str_len)]
    As=""; Cs=""; Gs=""; Ts = ""
    for i in range(str_len):
        for j in range(len(DNA_array)):
            if(DNA_array[j][i]=='A'):
                A[i] = A[i] + 1
            if(DNA_array[j][i]=='C'):
                C[i] = C[i] + 1
            if(DNA_array[j][i]=='G'):
                G[i] = G[i] + 1
            if(DNA_array[j][i]=='T'):
                T[i] = T[i] + 1
        As = As + str(A[i]) + " "
        Cs = Cs + str(C[i]) + " "
        Gs = Gs + str(G[i]) + " "
        Ts = Ts + str(T[i]) + " "
    return A, C, G, T, As, Cs, Gs, Ts

def gen_consensus(A, C, G, T):
    length = len(A)
    seq = ""
    for i in range(length):
        temp = ""
        max = -1
        if(max<A[i]):
            max = A[i]
            temp = "A"
        if(max<C[i]):
            max = C[i]
            temp = "C"
        if(max<G[i]):
            max = G[i]
            temp = "G"
        if(max<T[i]):
            max = T[i]
            temp = "T"
        seq = seq + temp
    
    return seq

#strr = ["ATCCAGCT", "ATGGATCT", "GGGCAACT", "AAGCAACC", "TTGGAACT", "ATGCCATT", "ATGGCACT"]
strr=[]
with  open('rosalind_cons.txt') as fp:
    contents = fp.read()
    for entry in contents.split():
        if(entry[:9]!=">Rosalind"):
            #print(entry)
            strr.append(entry)

A, C, G, T, As, Cs, Gs, Ts = gen_profile_matrix(strr)
consensus = gen_consensus(A, C, G, T)

print(consensus)
print("A: "+As)
print("C: "+Cs)
print("G: "+Gs)
print("T: "+Ts)