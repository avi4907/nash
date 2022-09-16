movies=['sholay','rrr','ddlj','dewaar','radhey','wanted','super30','batman','spiderman','dabangg']
print(len(movies))
print(movies)

movies.sort()
print(movies)

movies.reverse()
print(movies)

print('first movie',movies[0])
print('last movie',movies[-1])
print('first 3 movies',movies[:3])
print('all movies except first 3',movies[4:])
print('movies with even index',movies[::2])