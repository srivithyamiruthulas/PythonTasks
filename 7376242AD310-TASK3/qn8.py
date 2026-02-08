#leader_lst
lst=[1,2,3,4,3,2,1]

leader_lst=[]
lst1=sorted(lst,reverse=True)
for i in range(len(lst1)-1):
    if lst[i]<lst[i+1]:
        temp=lst[i+1]
        leader_lst.append(temp)
        
leader_lst.append(lst[-1])
rev_leader_lst=sorted(leader_lst,reverse=True)
print(rev_leader_lst)   

