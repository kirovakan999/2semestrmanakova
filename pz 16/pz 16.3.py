# Для задачи из блока 1 создать две функции, save_def и load_def,
# которые позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.
import pickle

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def read_book_info(self):
        return f"Название: {self.title} \nАвтор: {self.author} \nКоличество страниц: {self.num_pages}"

def save_def(books):
    with open('books_data.bin', 'wb') as file:
        pickle.dump(books, file)

def load_def():
    with open('books_data.bin', 'rb') as file:
        return pickle.load(file)

book1 = Book('Мастер и Маргарита', 'Михаил Булгаков', 384)
book2 = Book('Евгений Онегин', 'Александр Пушкин', 224)
book3 = Book('Муму', 'Иван Тургенев', 220)

books_list = [book1, book2, book3]
save_def(books_list)

loaded_books = load_def()

for book in loaded_books:
    print(book.read_book_info())