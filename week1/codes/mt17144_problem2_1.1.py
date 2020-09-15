
import timeit

start = timeit.default_timer()

l=['-','A','C','G','T']
set=[]

def permutation(lst,i):
    if len(lst)-1 == i:
        print(lst)
    else:
        for j in range(i,len(lst)):
            lst[i],lst[j]=lst[j],lst[i]
            permutation(lst,i+1)
            lst[i], lst[j] = lst[j], lst[i]

def powerset(xs):
    result=[[]]
    for x in xs:
        newsubsets = [subset + [x] for subset in result ]
        result.extend(newsubsets)
    return result

k=(int)(input(""))
set=powerset(l)
for i in range(len(set)):
    if len(set[i])==k:
        permutation(set[i],0)


stop = timeit.default_timer()
print()
print("time taken:"+str(stop - start))