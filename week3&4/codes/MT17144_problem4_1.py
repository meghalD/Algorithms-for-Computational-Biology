from collections import defaultdict

filename="q4_data"
val=[]
sequence=defaultdict(list)

def hamming_dist(str1,str2):
    min=999

    for j in range(len(str2)):
        counter=0
        diff = 0
        for i in str1:
            print(i,str2[j][counter])
            if i != str2[j][counter]:
                diff=diff+1
            counter=counter+1
        if(diff < mutation):
            diff=0
        else:
            diff=diff-mutation
        if(diff<min):
            min=diff
    print(min)
    return min

def score(motif,sequence):
    min_score=0
    for key in sequence.keys():
        min_score+=hamming_dist(motif,sequence[key])
    print(min_score)

def kmers(text,k,j):
    for i in range(n - k + 1):
        sequence[j].append(text[i:i + k])
    #j=j+1

def pattern_branching():
    score(motif,sequence)

motif=input("enter the motif")
mutation=int(input("enter the no. of mutations allowed"))
l=len(motif)
j=0
with open(filename) as file:
    for line in file:
        line = line.strip()
        n=len(line)
        kmers(line,l,j)
        j=j+1
print(sequence)
pattern_branching()

