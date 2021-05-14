
import pytest
import movies
import tasks

@pytest.fixture()
def small_movie_list():
    small_movie_list_data = [{
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
        },
        {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
        }, ]
    return small_movie_list_data


def test_true_movie_score_above_55():
    assert tasks.movie_score_above_55("Detective") == True


def test_false_movie_score_above_55():
    assert tasks.movie_score_above_55("Exam") == False


def test_unknown_input_movie_score_above_55():
    assert tasks.movie_score_above_55("123") == 'No such movie'


def test_list_movies_with_score_above_55():
    list_of_movies=['Usual Suspects', 'Hitman', 'Dark Knight',
                    'The Help', 'The Choice', 'Colonia', 'Love', 'Joking muck',
                    'What is the name', 'Detective', 'We Two']
    assert tasks.list_movies_with_score_above_55() == list_of_movies


def test_correct_input_category_movies():
    assert tasks.category_movies("Comedy") == [{'name': 'Joking muck', 'imdb': 7.2, 'category': 'Comedy'}]


def test_unknown_input_category_movies():
    assert tasks.category_movies("Comedy123") == 'No such category'


def test_average_score():
    assert tasks.average_score(movies.movies) == 6.49


def test_small_list_average_score(small_movie_list):
    assert tasks.average_score(small_movie_list) == 7.43


def test_valid_input_category_average_score():
    assert tasks.category_average_score("Action") == 6.3


def test_unknown_input_category_average_score():
    assert tasks.category_average_score("123") == 'No such category'
