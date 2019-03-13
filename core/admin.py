from django.contrib import admin
from core.models import Book, Category
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        # 'category', <--- having trouble with this one
        'description',
        'date_added',
    )
    exclude = ('slug',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    exclude = ('slug',)
