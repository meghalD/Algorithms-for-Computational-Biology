val=[]

def kmers(k):
    for i in range(n - k + 1):
        val.append(text[i:i + k])
    #return val

def overlap(str1,str2):
    max=-99
    s=""
    len1=len(str1)
    len2=len(str2)

    for i in range(min(len1,len2)+1):
        if(str1[len1-i-1:len1]==str2[0:i+1]):
            if max < i:
                max = i
                s=str1+str2[i+1:len2]

    for i in range(min(len1,len2)+1):
        if(str2[len2-i-1:len2]==str1[0:i]):
            if max < i:
                max = i
                s=str2+str1[i+1:len1]

    return max,s


def find_shortest_superstring(nt):
    while(nt!=1):
        max=-99
        res=""
        l=0
        r=0
        for i in range(nt):
            for j in range(i+1,nt):

                max_len,some=overlap(temp[i],temp[j])
                if max<max_len:
                    max=max_len
                    res=some
                    l=i
                    r=j
        nt=nt-1
        if max==-99:
            temp[0]+=temp[nt]
        else:
            temp[l]=res
            temp[r]=temp[nt]

    return temp[0]

k= int(input(""))
text = input("")
n=len(text)
kmers(k)
print("k-mers are:",val)
temp=val
nt=len(val)
ss=find_shortest_superstring(nt)
print("the shortest superstring is:",ss)