from movies import movies


# Write a function that takes a single movie and
# returns True if its IMDB score is above 5.5


def movie_score_above_55(movie_name):
    for movie in movies:
        if movie['name'] == movie_name:
            return movie['imdb'] > 5.5
    return "No such movie"


# Write a function that returns a sublist of movies
# with an IMDB score above 5.5.


def list_movies_with_score_above_55():
    list_movies = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            list_movies.append(movie['name'])
    # list_movies2 = [movie['name'] for movie in movies if movie['imdb'] > 5.5]
    return list_movies


# Write a function that takes a category name and returns
# just those movies under that category.


def category_movies(category):
    category_movies = []  # pricali smo da bude set ali mi je lakse bilo da koristim listu
    for movie in movies:
        if movie['category'] == category:
            category_movies.append(movie)
    # category_movies2=[movie for movie in movies if movie['category'] == category]
    if not category_movies:
        return "No such category"
    return category_movies


# Write a function that takes a list of movies and computes
# the average IMDB score.

def average_score(list_of_movies):
    scores = []
    dict_movies = [movie['name'] for movie in movies]
    unknown_movies = []
    for input_movie in list_of_movies:
        if input_movie not in dict_movies:
            unknown_movies.append(input_movie)
        else:
            for movie in movies:
                if movie['name'] == input_movie:
                    scores.append(movie['imdb'])
    if not unknown_movies:
        avg_score = round(sum(scores) / len(scores), 2)
        return avg_score
    return f"No movie(s):{unknown_movies}"


# Write a function that takes a category and computes
# the average IMDB score (HINT: reuse the function
# from question 3.

def category_average_score(category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    if not category_movies:
        return "No such category"
    else:
        scores = []
        for movie in category_movies:
            scores.append(movie["imdb"])
        avg_score = round(sum(scores) / len(scores), 2)
        return avg_score







