filename="data.txt"
original_data=[]
comp_data=[]
set_final=[]

def de_bruijn(set_final):
    set_final.sort()
    #print(set_final)
    size=len(set_final[0])
    for i in range(len(set_final)):
        print("(",set_final[i][0:size-1],",",set_final[i][1:size],")")

def add_rev_complements():
    #print("")
    for i in range(len(comp_data)):
        comp_data[i]=comp_data[i][::-1]
    #print(comp_data)
    set_final=list(set().union(original_data,comp_data))
    #print(set_final)
    de_bruijn(set_final)

def find_complement(size):
    for i in range(len(original_data)):
        str=''
        for j in range(size):
            if(original_data[i][j]=='A'):
                str+='T'
            elif(original_data[i][j]=='T'):
                str+='A'
            elif(original_data[i][j] == 'G'):
                str+= 'C'
            elif(original_data[i][j] == 'C'):
                str+= 'G'
        comp_data.append(str)
    #print(comp_data)
    add_rev_complements()

#read from file:
with open(filename) as file:
    for line in file:
        line = line.strip()
        original_data.append(line)
#print(original_data)

find_complement(len(original_data[0]))