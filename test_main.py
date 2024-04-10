import pytest


class TestBooksCollector:

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
                                                               date_books,
                                                               book_genre, expected_result):
        assert len(collector.get_books_with_specific_genre(book_genre)) == expected_result

    def test_get_books_genre_full_list_of_books(self, collector, date_books):
        assert len(collector.get_books_genre()) == 4

    def test_get_books_for_children_list_book_without_age_rating(self, collector, date_books):
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_existing_book_add_to_favorite(self, collector, date_books):
        collector.add_book_in_favorites('Двадцать тысяч лье под водой')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_one_book_twice(self, collector, date_books):
        book_name = 'Двадцать тысяч лье под водой'
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize(
        'book_name, expected_result',
        (
                ('Двадцать тысяч лье под водой', 0),
                ('Гордость и предубеждение', 1),

        )
    )
    def test_delete_book_from_favorites(self, collector, date_books, book_name, expected_result):
        collector.add_book_in_favorites('Двадцать тысяч лье под водой')
        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == expected_result

    def test_get_list_of_favorites_books(self, collector, date_books):
        collector.add_book_in_favorites('Двадцать тысяч лье под водой')
        assert len(collector.get_list_of_favorites_books()) == 1
