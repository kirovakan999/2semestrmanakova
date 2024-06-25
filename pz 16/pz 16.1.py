# Создайте класс «Книга», который имеет атрибуты название, автор и количество страниц.
# Добавьте методы для чтения и записи книги.

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def read_book_info(self):
       return f"Название: {self.title} \nАвтор: {self.author} \nКоличество страниц: {self.num_pages}"



my_book = Book('Мастер и Маргарита', 'Михаил Булгаков', 384)
print(my_book.read_book_info())