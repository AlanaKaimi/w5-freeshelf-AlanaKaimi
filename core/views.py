from django.shortcuts import render, get_object_or_404, redirect
from core.models import Book, Category, Favorite
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):
    """View function for home page of site"""
    books = Book.objects.all()
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'books': books,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@require_http_methods(['POST'])
@login_required
def book_favorite_view(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    if book in request.user.favorite_books():
        request.user.favorite_set.get(book=book).delete()
    else:
        request.user.favorite_set.create(book=book)
    return redirect(book.get_absolute_url())