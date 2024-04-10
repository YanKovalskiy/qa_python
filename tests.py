from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_identical_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name',
        ('',
         'Круглосуточный книжный мистера Пенумбры!!')  # 41 символ
    )
    def test_add_new_book_incorrect_length_book_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'book_name, book_genre, expected_result',
        (
                ('Двадцать тысяч лье под водой', 'Фантастика', 'Фантастика'),
                ('Двадцать тысяч лье под водой', 'Мелодрама', ''),
        )
    )
    def test_set_book_genre_add_genre_to_existing_book(self, book_name, book_genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == expected_result

    @pytest.mark.parametrize(
        'book_genre',
        (
                'Фантастика', 'Мелодрама'
        )
    )
    def test_set_book_genre_add_genre_to_not_existing_book(self, book_genre):
        collector = BooksCollector()
        book_name = 'Двадцать тысяч лье под водой'
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) is None
