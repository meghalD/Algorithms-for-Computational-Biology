lengths=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]
solution=[]*len(lengths)

def max_profit_rod():
    n=len(lengths)
    T={}
    T[0,0]=0
    for i in range(1,n+1):
        T[i,0]=0
        #print(T[i,0])
    for j in range(1,n+1):
        T[1,j]=T[1,j-1]+price[0]
        #print(T[1,j])
    for i in range(2,n+1):
        for j in range(1,n+1):
            if(j>=i):
                T[i,j]=max(T[i-1,j],price[i-1]+T[i,j-i])
            else:
                T[i,j]=T[i-1,j]
    print(T[i,j])
    backtrack_profit(T,i,j,n)

def backtrack_profit(T,i,j,n):

    while(T[i,j]!=0):
        #print("in while")
        if(j>=i):
            if(T[i,j]==T[i,j-i]+price[i-1]):
                j=j-i
                solution.append(str(i))
            elif(T[i,j]==T[i-1,j]):
                i=i-1
        else:
            if (T[i, j] == T[i,0] + price[i - 1]):
                j = j - i
                solution.append(str(i))
            elif (T[i, j] == T[i - 1, j]):
                i = i - 1

    print(solution)

max_profit_rod()
