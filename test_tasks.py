
import pytest
import tasks


@pytest.fixture()
def movies_for_test():
    return [{
            "name": "Colonia",
            "imdb": 7.4,
            "category": "Romance"
        },
        {
            "name": "Love",
            "imdb": 6.0,
            "category": "Romance"
        },
        {
            "name": "Bride Wars",
            "imdb": 5.4,
            "category": "Romance"
        }, ]


def test_true_movie_score_above_55(movies_for_test):
    assert tasks.movie_score_above_55(movies_for_test[0]) == True


def test_false_movie_score_above_55(movies_for_test):
    assert tasks.movie_score_above_55(movies_for_test[2]) == False


def test_high_score_movies(movies_for_test):
    assert tasks.high_score_movies(movies_for_test) == ['Colonia', 'Love']


def test_category_movie(movies_for_test):
    assert tasks.category_movies(movies_for_test) == {'Romance':['Colonia','Love','Bride Wars']}


def test_average_score(movies_for_test):
    assert tasks.average_score(movies_for_test) == 'Average IMDB score is: 6.27'


def test_category_average_score(movies_for_test):
    assert tasks.category_average_score(movies_for_test) == {'Romance': 6.27}