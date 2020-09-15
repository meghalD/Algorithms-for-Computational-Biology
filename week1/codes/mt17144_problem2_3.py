seq_DNA = []

with open('con_seq.fa') as f:
    index = 1
    for line in f:
        seq_DNA.append(f.readline().rstrip("\n"))
n=len(seq_DNA[0])
A=[0]*n
C=[0]*n
G=[0]*n
T=[0]*n
for i in range(n):
    for j in range(len(seq_DNA)):
        if seq_DNA[j][i]== 'A':
            A[i]+=1
        elif seq_DNA[j][i]== 'C':
            C[i]+=1
        elif seq_DNA[j][i]== 'G':
            G[i]+=1
        else:
            T[i]+=1
str=''
for i in range(n):
    if(max(A[i],C[i],G[i],T[i]) == A[i]):
        str+='A'
    elif (max(A[i], C[i], G[i], T[i]) == C[i]):
        str +='C'
    elif (max(A[i], C[i], G[i], T[i]) == G[i]):
        str += 'G'
    else:
        str += 'T'
print("Consensus: "+str)
print("Frequency Matrix:\n[%s,\n%s,\n%s,\n%s]" % (A,C,G,T))