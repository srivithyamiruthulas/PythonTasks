tup=((1,2),(2,4),(2,1),(2,9))
tup1=[]
seen=[]
tup=list(tup)
n=len(tup)

for i in range(n):
    pair=tuple(sorted(tup[i]))
    if pair not in seen:
        seen.append(pair)
        tup1.append(tup[i])

tup1=tuple(tup1)
print(tup1)



