from django.contrib import admin
from core.models import Book, Category

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_category')
    # inlines = [BooksInstanceInline] <-- Not sure if I need this here