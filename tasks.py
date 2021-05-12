from movies import movies

# Write a function that takes a single movie and
# returns True if its IMDB score is above 5.5


def movie_score_above_55(single_movie):
    return single_movie["imdb"] > 5.5

    # list_of_movies = []
    # for movie in movies:
    #     if movie['imdb'] > 5.5:
    #         movie_above = movie['name'], True
    #         list_of_movies.append(movie_above)
    # return list_of_movies


# Write a function that returns a sublist of movies
# with an IMDB score above 5.5.

def high_score_movies():
    return [movie['name'] for movie in movies if movie_score_above_55(movie)]

# def high_score_movies_collection():
#     list_of_high_score_movies = []
#     for movie in movies:
#         if movie_score_above_55(movie):
#             list_of_high_score_movies.append(movie)
#     return list_of_highs_core_movies


# def list_movies_with_score_above_55():
#     list_movies = []
#     for movie in movies:
#         if movie['imdb'] > 5.5:
#             list_movies.append(movie['name'])
#     return list_movies

# Write a function that takes a category name and returns
# just those movies under that category.

# kako ovu funkciju uraditi elegantnije
def category_movies():
    categories_movies = {}
    for movie in movies:
        if movie['category'] not in categories_movies:
            categories_movies[movie['category']] = []
        categories_movies[movie['category']].append(movie['name'])
    return categories_movies




# Write a function that takes a list of movies and computes
# the average IMDB score.

def average_score():
    scores = [movie["imdb"] for movie in movies]
    avg_score = (round(sum(scores) / len(scores), 2))
    return f'Average IMDB score is: {avg_score} '

    # for movie in movies:
    #     scores.append(movie['imdb'])

# Write a function that takes a category and computes
# the average IMDB score (HINT: reuse the function
# from question 2.

# def category_avg_score():

# kako ovu funkciju uraditi elegantnije
def category_average_score():
    categories_score = {}
    categories_avg_score = {}
    for movie in movies:
        if movie['category'] not in categories_score:
            categories_score[movie['category']] = []
        categories_score[movie['category']].append(movie['imdb'])
        for k, v in categories_score.items():
            categories_avg_score.update({k: sum(v) / len(v)})
    return categories_avg_score
