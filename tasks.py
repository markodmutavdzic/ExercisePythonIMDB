from movies import movies


# Write a function that takes a single movie and
# returns True if its IMDB score is above 5.5
print(1)

for movie in movies:
   if movie['imdb']>5.5:
       print(movie['name'], True)


# Write a function that returns a sublist of movies
# with an IMDB score above 5.5.
print(2)

lista = []
for movie in movies:
    if movie['imdb']>5.5:
        lista.append(movie['name'])
print(lista)

# Write a function that takes a category name and returns
# just those movies under that category.
print(3)


categories_movies={}

for movie in movies:
    if movie['category'] not in categories_movies:
        categories_movies[movie['category']]=[]

    categories_movies[movie['category']].append(movie['name'])

for k,v in categories_movies.items():
    print (f' {k} : {v}')

# Write a function that takes a list of movies and computes
# the average IMDB score.
print(4)


scores=[]
for movie in movies:
    scores.append(movie['imdb'])

print('Average IMDB score is: ', round(sum(scores)/len(scores), 2))


# Write a function that takes a category and computes
# the average IMDB score (HINT: reuse the function
# from question 2.
print(5)

categories_score={}

for movie in movies:
    if movie['category'] not in categories_score:
        categories_score[movie['category']]=[]
    categories_score[movie['category']].append(movie['imdb'])

for k,v in categories_score.items():
    print(k,':', sum(v)/len(v))



