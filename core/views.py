from django.shortcuts import render, get_object_or_404, redirect
from core.models import Book, Category, Favorite
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    """View function for home page of site"""
    books = Book.objects.all()
    categories = Category.objects.all()
    favorites = Favorite.objects.all()

    context = {
        'categories': categories,
        'books': books,
        'favorites': favorites,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookDetailView(generic.DetailView):
    model = Book



class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['category_list'] = Category.objects.all()
        return context


@require_http_methods(['POST'])
@login_required
def book_favorite_view(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    next = request.POST.get('next', '/')

    favorite, created = request.user.favorite_set.get_or_create(book=book)

    # # I liked this better but having an issue with it, trying the other option
    # if book in request.user.favorite_books(self.favorite):
    #     request.user.favorite_set.get(book=book).delete()
    # else:
    #     request.user.favorite_set.create(book=book)

    if created:
        messages.success(request, f"You have favorited {book.title}.")
    else:
        messages.info(request, f"You have unfavorited {book.title}.")
        favorite.delete()

    return HttpResponseRedirect(next)

def my_favorites_view(request):
    favorites = Favorite.objects.all()
    book_list = Book.objects.all()

    context = {
        'favorites': favorites,
        'book_list': book_list,
    }
    return render(request, 'core/book_favorite.html', context=context)