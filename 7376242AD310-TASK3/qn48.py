cfg={}
n=int(input())
for i in range(n):
    k=input()
    v=input()
    cfg[k]=v
req=set(input().split())
missing=req-set(cfg.keys())
extra=set(cfg.keys())-req
print(missing)
print(extra)
