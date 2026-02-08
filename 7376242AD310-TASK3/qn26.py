marks=list(map(int,input().split()))
res={"<50":[],"50-74":[],">=75":[]}
for m in marks:
    if m<50:
        res["<50"].append(m)
    elif m<=74:
        res["50-74"].append(m)
    else:
        res[">=75"].append(m)
print(res)
