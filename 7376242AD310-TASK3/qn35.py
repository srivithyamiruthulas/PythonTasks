d={"a":2,"b":5,"c":3}
max_key=None
max_val=0
for k in d:
    if d[k]>max_val:
        max_val=d[k]
        max_key=k
print(max_key)
