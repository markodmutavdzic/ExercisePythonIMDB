from movies import movies


# Write a function that takes a single movie and
# returns True if its IMDB score is above 5.5
# 1

def movie_score_above_55(movie_name):
    for movie in movies:
        if movie['name'] == movie_name:
            return movie['imdb'] > 5.5
    return "No such movie"


# Write a function that returns a sublist of movies
# with an IMDB score above 5.5.
# 2

def list_movies_with_score_above_55():
    list_movies = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            list_movies.append(movie['name'])
    # list_movies2 = [movie['name'] for movie in movies if movie['imdb'] > 5.5]
    return list_movies


# Write a function that takes a category name and returns
# just those movies under that category.
# 3

def category_movies(category):
    category_movies_list = []
    for movie in movies:
        if movie['category'] == category:
            category_movies_list.append(movie)
    # category_movies2=[movie for movie in movies if movie['category'] == category]
    if not category_movies_list:
        return "No such category"
    return category_movies_list


# Write a function that takes a list of movies and computes
# the average IMDB score.
# 4

def average_score(list_of_movies):
    score = 0
    for movie in list_of_movies:
        score += movie['imdb']
    avg_score = round(score/len(list_of_movies), 2)
    return avg_score


# Write a function that takes a category and computes
# the average IMDB score (HINT: reuse the function
# from question 3.
# 5

def category_average_score(category):
    category_movies_list = category_movies(category)
    if category_movies_list == "No such category":
        return "No such category"
    else:
        score = 0
        for movie in category_movies_list:
            score += movie['imdb']
        avg_score = round(score / len(category_movies_list), 2)
        return avg_score







