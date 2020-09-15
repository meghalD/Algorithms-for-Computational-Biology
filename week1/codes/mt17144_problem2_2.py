str1 ='TGTAGAAAA'

def kmers(string,k):
    count_dict = {}
    n=len(string)
    for i in range(n - k + 1):
        kmer=string[i:i + k]
        if kmer not in count_dict:
            count_dict[kmer]=1
        else:
            count_dict[kmer]+=1
    return count_dict

with open('con_seq.fa') as f:
    index = 1
    for line in f:
        sequence=(f.readline().rstrip("\n"))
        for i in range(1,len(sequence)+1):
            print(kmers(sequence,i))

#print(val)'''