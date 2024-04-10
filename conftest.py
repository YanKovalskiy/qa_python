from main import BooksCollector
import pytest


def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture()
def collector():
    return BooksCollector()


@pytest.fixture()
def date_books(collector):
    book = {
        'Рассказы о Шерлоке Холмсе': 'Детективы',
        'Двадцать тысяч лье под водой': 'Фантастика',
        'Человек-амфибия': 'Фантастика',
        'Хребты безумия': 'Ужасы',
    }

    for book_name, book_genre in book.items():
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
