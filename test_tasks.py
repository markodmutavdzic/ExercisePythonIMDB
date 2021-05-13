
import pytest
import tasks


@pytest.fixture()
def list_of_movies():
    return ["Hitman","Usual Suspects","Dark Knight"]

def test_true_movie_score_above_55():
    assert tasks.movie_score_above_55("Detective") == True


def test_false_movie_score_above_55():
    assert tasks.movie_score_above_55("Exam") == False


def test_no_entry_movie_score_above_55():
    with pytest.raises(TypeError):
        assert tasks.movie_score_above_55()


def test_invalid_entry_movie_score_above_55():
    assert tasks.movie_score_above_55(123) == 'No such movie'


def test_unknown_entry_movie_score_above_55():
    assert tasks.movie_score_above_55("123") == 'No such movie'


def test_list_movies_with_score_above_55():
    assert tasks.list_movies_with_score_above_55() == ['Usual Suspects', 'Hitman', 'Dark Knight',
                                                        'The Help', 'The Choice', 'Colonia', 'Love', 'Joking muck',
                                                        'What is the name', 'Detective', 'We Two']


def test_correct_input_category_movies():
    assert tasks.category_movies("Comedy") == [{'name': 'Joking muck', 'imdb': 7.2, 'category': 'Comedy'}]


def test_no_entry_category_movies():
    with pytest.raises(TypeError):
        assert tasks.category_movies()


def test_incorrect_input_category_movies():
    assert tasks.category_movies("Comedy123") == 'No such category'


def test_no_input_average_score():
    with pytest.raises(TypeError):
        assert tasks.average_score()


def test_valid_input_average_score(list_of_movies):  # mogao sam i bez fiksture, mada bolje da vezbam
    assert tasks.average_score(list_of_movies) == 7.43


def test_invalid_input_average_score():
    assert tasks.average_score(["Hitma","Usual Suspects","Dark Knight"]) == "No movie(s):['Hitma']"


def test_unknown_input_average_score():
    with pytest.raises(TypeError):
        assert tasks.average_score(123)


def test_no_input_category_average_score():
    with pytest.raises(TypeError):
        assert tasks.category_average_score()

def test_valid_input_category_average_score():
    assert tasks.category_average_score("Action") == 6.3

def test_invalid_input_category_average_score():
    assert tasks.category_average_score(123) == 'No such category'