p=5000
p2=p**2
t=0
for a in range(-p-150,p+150,10):
    for b in range(-p-150,p+150,10):
        if a**2+b**2<=p2:t+=1
print(t)
