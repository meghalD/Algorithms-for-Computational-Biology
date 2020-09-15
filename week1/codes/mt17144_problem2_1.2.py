import timeit
start = timeit.default_timer()

mono=['-','A','C','G','T']
di=[]
k=int(input(""))
l1=mono
l2=mono
if(k==1):
    print(mono)
else:
    #for iter in range(k-):
        for i in range(len(l1)):
            for j in range(len(l2)):
                s = l1[i]+l2[j]
                l2.append(s)

for i in range(len(l2)):
    if len(l2[i])==k:
        print(l2[i],end=',')
stop = timeit.default_timer()
print()
print("time taken:"+str(stop - start))