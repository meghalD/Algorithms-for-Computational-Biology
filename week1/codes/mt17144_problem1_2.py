dna=input("enter the DNA sequence")
rna=''
for c in dna:
    if c=='T':
       rna+='U'
    else:
        rna+=c

print(dna, rna)
