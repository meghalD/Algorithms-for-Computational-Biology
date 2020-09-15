fasta={}

fileD = open("con_seq.fa",'r')
while True:
    data = fileD.readline()
    if data == '':
        break
    s1 = data[1:len(data)-1]
    data = fileD.readline()
    fasta[s1] = data[:len(data)-1]
print(fasta)

"""
with open('con_seq.fa') as f:
    index = 1
    for line in f:
        if line[0]=='>':
            fasta[id]=line[0]
        seq_DNA.append(f.readline().rstrip("\n"))

s1=''
s2=''
fileD = open("con_seq.fa",'r')
data = fileD.readlines()
for i in data:
    if " >" in i:
        s1 = i[1:len(i)]
    else:
        s2 = i
        #tup = (s1,s2)
        fasta[s1]=s2
"""
