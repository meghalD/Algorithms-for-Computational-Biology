genbank={}
str=[]
fileD=open("mtb.gb",'r')
while True:
    data = fileD.readline()
    if data == '':
        break

    else:
        s = data.split()
        print(s)