from collections import defaultdict
adj_list=defaultdict(list)
vert=[]

def trav_check(val):
    print(val)


def find_path(key):
    i=0
    while(i!=len(adj_list[key])):
        #print(i,len(adj_list[key]),key)
        t=adj_list[key][i]

        #check for bridge
        if(len(adj_list[t])==1):
            i=i+1
            continue
        else:
            print(key+"-"+t,end=" ")
            #trav_check(adj_list[t])
            adj_list[t].remove(key)
            adj_list[key][i]
            key=t
            #print("key changed to :"+key)
            i=0
    if(i==0):
        del adj_list[t][0]
        del adj_list[key][0]
        print("done")


def check_euler():
    count =0
    for key in adj_list.keys():
        if(count==0):
            local_key0=key
        if (len(adj_list[key]) % 2 != 0):
            count=count+1
            if(count==2):
                local_key2=key
    if(count==0):
        find_path(local_key0)
    elif(count==2):
        find_path(local_key2)
    else:
        print("euler path does not exist")

def take_input():
    vertices=int(input(""))
    edges=int(input(""))
    #print(vertices,edges)
    for i in range(edges):
        u,v = input("").split(" ")
        adj_list[u].append(v)
        adj_list[v].append(u)
    print(adj_list)
    for key in adj_list.keys():
        vert.append(key)
    print(vert)
    check_euler()


take_input()