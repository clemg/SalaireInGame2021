from collections import Counter
s=""

with open("liste.txt","r") as fi:
    file = fi.readlines()
    ls=[]
    for line in file: ls.append(line.split(",")[2].ljust(12," ")[:12])
    for i in range(12):
        c=Counter(e[i]for e in ls if e[i]!=" ")
        #print(c)
        #0/0
        s+=max(c, key=c.get)

print(s)
print(len(s))
