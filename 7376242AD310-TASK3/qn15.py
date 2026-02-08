lst1=[2,3,4,5,7,8]
lst2=[3,5,9,3,6,9]
lst3=[6,3,7,4,2,5]

common = list(set(lst1) & set(lst2) & set(lst3))
print(common)