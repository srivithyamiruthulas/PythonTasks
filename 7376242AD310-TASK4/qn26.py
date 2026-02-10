posts = [["#fun", "#coding"], ["#coding", "#python"], ["#fun", "#python"]]

unique_hashtags = set().union(*posts)

common_hashtags = set(posts[0]).intersection(*posts[1:])

print(unique_hashtags)
print(common_hashtags)
