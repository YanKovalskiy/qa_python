from main import BooksCollector
import pytest


class TestBooksCollector:

    @pytest.fixture()
    def collector(self):
        return BooksCollector()

    @pytest.fixture()
    def date_for_get_books_with_specific(self, collector):
        book_name = 'Рассказы о Шерлоке Холмсе'
        book_genre = 'Детективы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        book_genre = 'Фантастика'

        book_name = 'Двадцать тысяч лье под водой'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        book_name = 'Человек-амфибия'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)


    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_identical_books(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name',
        ('',
         'Круглосуточный книжный мистера Пенумбры!!')  # 41 символ
    )
    def test_add_new_book_incorrect_length_book_name(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'book_name, book_genre, expected_result',
        (
                ('Двадцать тысяч лье под водой', 'Фантастика', 'Фантастика'),
                ('Двадцать тысяч лье под водой', 'Мелодрама', ''),
        )
    )
    def test_set_book_genre_add_genre_to_existing_book(self, collector, book_name, book_genre, expected_result):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == expected_result

    @pytest.mark.parametrize(
        'book_genre',
        (
                'Фантастика', 'Мелодрама'
        )
    )
    def test_set_book_genre_add_genre_to_not_existing_book(self, collector, book_genre):
        book_name = 'Двадцать тысяч лье под водой'
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) is None

    def test_get_book_genre_existing_book_book_genre(self, collector):
        book_name = 'Двадцать тысяч лье под водой'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    @pytest.mark.parametrize(
        'book_genre, expected_result',
        (
                ('Фантастика', 2),
                ('Детективы', 1),
                ('Мелодрама', 0),
        )
    )
    def test_get_books_with_specific_genre_any_genre_book_list(self, collector,
                                                                          date_for_get_books_with_specific,
                                                                          book_genre, expected_result):

        assert len(collector.get_books_with_specific_genre(book_genre)) == expected_result
