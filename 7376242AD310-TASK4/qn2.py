#Movies recommendation overlap
num_user1=int(input("Enter how many no of movies to be added to the list: "))
num_user2=int(input("Enter how many no of movies to be added to the list: "))
list1=[]
list2=[]
for i in range(num_user1):
    inp=input("Enter movie name: ")
    list1.append(inp)

for i in range(num_user2):
    inp=input("Enter movie name: ")
    list2.append(inp)

movie_set1=set(list1)
movie_set2=set(list2)
common_movies=movie_set1.intersection(movie_set2)
unique=movie_set1.symmetric_difference(movie_set2)

print("The common movies",list(common_movies))
print("The list of movies that are unique to either",list(unique))