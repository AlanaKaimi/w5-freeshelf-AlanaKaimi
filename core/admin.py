from django.contrib import admin
from core.models import Book, Author, Category

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name']
    inlines = [BooksInline]

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_category')
    # inlines = [BooksInstanceInline] <-- Not sure if I need this here