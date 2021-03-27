
import urllib.request
import re

file = open("rosalind_mprt.txt", "r")
for uniId in file:
    target_url = "http://www.uniprot.org/uniprot/" + uniId.strip(' \n') + ".fasta"
    data = urllib.request.urlopen(target_url)
    seq = ""
    for line_raw in data:
        line = line_raw.decode("utf-8")
        if (line[0] == ">"):
            continue
        else:
            seq = seq + str(line).strip(" \n")
        
    

    # Now check for Motif locations
    loc = ""
    for i in range(len(seq) - 4 + 1):
        motif = seq[i:i+4]
        
        if(motif[0]=="N" and motif[1] != "P" and (motif[2] == "S" or motif[2] == "T") and motif[3] != "P"):
            loc = loc + str(i+1) + " "
    if(len(loc)>0):
        print( uniId.strip(' \n'))
        print(loc)

