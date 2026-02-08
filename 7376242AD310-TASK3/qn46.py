exp=set(input().split())
n=int(input())
docs=[]
for i in range(n):
    docs+=input().lower().split()
used=set(docs)
covered=len(exp&used)/len(exp)*100
missing=exp-used
print(covered)
print(missing)
