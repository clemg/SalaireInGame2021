import hashlib
for x in range(-5000,5010,10):
    for y in range(-5000,5010,10):
        if y==0 or x==0: continue
        if y%x!=0: continue
        for day in range(1,32):
            for month in range(2,4):
                c=f"{day}/{month}@{x},{y}"
                if hashlib.sha256(c.encode()).hexdigest()=="ccee0f6b78bba5eff19a89678252a0fcece57d3b80458ceeb41c92bfdfa645ce":
                    print(c)
                    0/0
print("no match!!!")
