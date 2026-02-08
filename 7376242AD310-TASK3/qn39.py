lst=list(map(int,input().split()))
k=int(input())
freq={}
for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
res=sorted(freq,key=freq.get,reverse=True)
print(res[:k])
