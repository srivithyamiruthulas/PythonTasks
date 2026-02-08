#to print the second minimun value in the given list
list=[19,44,68,25,83,99,43,87,29,46,74,85,97,34,87,38,47,63,53,70,89,24,58,54,43,84,57,8,79,90,45,34,58,65,87]
min_num=min(list)
print("the 1st min value:")
print(min_num)
list.remove(min_num)
sec_min=min(list)
print("the 2nd min value:",sec_min)
print(list)