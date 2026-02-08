req=set(input().split())
stu=set(input().split())
missing=req-stu
extra=stu-req
print("Missing:",missing)
print("Extra:",extra)
