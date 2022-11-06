n=[]
for i in range(10,151):
    if(i%15==0 and i%5==0):
        n.append(str(i))
print(",".join(n))