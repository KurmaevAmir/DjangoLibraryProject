from django.db import models


# Create your models here.


class Author(models.Model):
    """Авторы книг"""


    class Meta:
        db_table = "authors"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


    author_name = models.TextField(verbose_name="Имя автора")
    author_surname = models.TextField(verbose_name="Фамилия автора")
    author_middle_name = models.TextField(verbose_name="Отчество автора", blank=True, null=True)


    def __str__(self):
        return f'{self.author_surname} {self.author_name} {self.author_middle_name}'


class Book(models.Model):
    """Книги"""


    class Meta:
        db_table = "books"
        verbose_name = "Описание книги"
        verbose_name_plural = "Книги"


    title = models.TextField(verbose_name="Название произведения")
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, verbose_name="Автор",
                               blank=True, null=True)
    number_of_pages = models.IntegerField(verbose_name="Количество страниц")
    barcode = models.TextField(verbose_name="Штрих-код")
    publication_date = models.DateField(verbose_name="Дата издания")
    publishing_house = models.TextField(verbose_name="Издательство")


    def __str__(self):
        return f'{self.author}-{self.title} {self.barcode}'


class UserBook(models.Model):
    """Пользователь книги"""


    class Meta:
        db_table = "user_book"
        verbose_name = "Пользователь книги"
        verbose_name_plural = "Пользователи книги"


    user_book_name = models.TextField(verbose_name="Имя пользователя")
    user_book_surname = models.TextField(verbose_name="Фамилия пользователя")
    parallel_number = models.IntegerField(verbose_name="Класс")
    letter = models.CharField(max_length=1, verbose_name="Литера класса")
    user_book_email = models.EmailField(verbose_name="Почта пользователя")


    def __str__(self):
        return f'{self.user_book_name} {self.user_book_surname} {self.parallel_number}{self.letter}'


class BooksInUse(models.Model):
    """Книги, находящиеся в пользовании"""


    class Meta:
        db_table = "books_in_use"
        verbose_name = "Книга в использовании"
        verbose_name_plural = "Книги в использовании"

    statuses = (("waiting for issuance", "ожидание выдачи"),
                ("issued", "выдана"),
                ("received", "получена"))


    book = models.ForeignKey(Book, on_delete=models.RESTRICT, verbose_name="Книга")
    book_owner = models.ForeignKey(UserBook, on_delete=models.RESTRICT,
                                   verbose_name="Владелец книги")
    status = models.TextField(verbose_name="Статус книги", choices=statuses)
    date_of_issue = models.DateTimeField(verbose_name="Дата выдачи")
    date_of_receiving = models.DateTimeField(verbose_name="Дата получения", blank=True, null=True)


    def __str__(self):
        return f'Произведение: {self.book} Носитель: {self.book_owner} Статус: {self.status}'
