def needleman_wunsch(s1,s2):
    row=len(s1)+1
    col=len(s2)+1

    C={}
    C[0,0]=0
    for i in range(1,col):
        C[0,i]=C[0,i-1]+2
    for j in range(1,row):
        C[j,0]=C[j-1,0]+2
    for i in range(1,row):
        for j in range(1,col):
            # C[i,j]=0
            #print(s1[i-1],s2[j-1])
            if (s1[i-1] == s2[j-1]):
                C[i, j] = C[i - 1, j - 1] - 2
            else:
               C[i, j] = min(C[i - 1, j] + 2, C[i, j - 1] + 2, C[i - 1, j - 1] - 1)

    print(C)
    print(C[row-1, col-1])
    compute_alignment(C,s1,s2,i,j)

def compute_alignment(C,s1,s2,i,j):
    str1=''
    str2=''
    length=max(len(s1),len(s2))
    while(length):
        if(s1[i-1]!=s2[j-1]):
            if(C[i,j]==C[i - 1, j] + 2):
                #s2[j-1].replace('-')
                str2+='-'
                str1+=s1[i-1]
                #s2=s2[:j-1]+'-'+s2[j:]
                i=i-1
            elif(C[i,j]==C[i, j - 1] + 2):
                #s1[i-1].replace('-')
                str1+='-'
                str2+=s2[j-1]
                #s1=s1[:i-1]+'-'+s1[i:]
                j=j-1
            else:
                str1 += s1[i - 1]
                str2 += s2[j - 1]
                i = i - 1
                j = j - 1
        else:
            str1+=s1[i-1]
            str2+=s2[j-1]
            i=i-1
            j=j-1
        length=length-1

    print(''.join(reversed(str1)))
    print(''.join(reversed(str2)))




needleman_wunsch('TCCA','TCGCA')