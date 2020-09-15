'''KMP ALGORITHM : inputs required are txt: the string in which we find the match and p which is the sequence to be matched via '''

txt = "abcdefghijklmnopqrstuvwxyz"
p = "defghij"

def KMPSearch(pattern, txt):
    M = len(pattern)
    N = len(txt)
    pat = [0] * M
    prefix(pattern, M, pat)
    i = 0 #counter for txt
    j=0 #counter for p

    while i<N:
        matches = 0
        if txt[i]==pattern[j]:
            if j == M-1:
                print("occurence at ", str(i - j))
                j = 0
                i+=1
            else:
                i+=1
                j+=1
                matches+=1
        elif matches!=0:
            skip=matches-pat[matches-1]
            if skip!=0:
                i=i-matches+skip
                j=0
        else:
            i+=1

def prefix(pattern,m,pat):
    i=1
    j=0
    while i<m and j<m :
        if pattern[i]==pattern[j]:
            pat[i]=j+1
            i+=1
            j+=1
        else:
            if j == 0:
                pat[i] = 0
                i+=1
            else:
                j = pat[j - 1]
    #print(pat)

KMPSearch(p, txt)