from django.contrib import admin

from .models import Author, Book, UserBook, BooksInUse

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('author_name', 'author_surname', 'author_middle_name')
    list_display = ('author_name', 'author_middle_name', 'author_surname')


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'barcode', 'publishing_house')
    raw_id_fields = ('author',)
    list_display = ('barcode', 'author', 'title', 'publishing_house')


class UserBookAdmin(admin.ModelAdmin):
    search_fields = ('user_book_name', 'user_book_surname', 'parallel_number', 'letter')
    list_display = ('user_book_name', 'user_book_surname', 'parallel_number', 'letter')


class BooksInUseAdmin(admin.ModelAdmin):
    search_fields = ('book', 'status', 'book_owner', 'date_of_receiving')
    raw_id_fields = ('book_owner', 'book')
    list_display = ('book', 'status', 'date_of_receiving')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(UserBook, UserBookAdmin)
admin.site.register(BooksInUse, BooksInUseAdmin)
