from django.shortcuts import render, redirect
from django.views import generic
from core.models import Book, Category

# Create your views here.

def index(request):
    """View finction for home page of site"""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    # The 'all()' is implied by default.    
    #! num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        #! 'num_authors': num_authors,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book


### !! Still working on code below !!
# https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
def get_redirected(queryset_or_class, lookups, validators):
    """Calls get_object_or_404 and conditionally builds redirect URL"""
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj, key):
            return obj, obj.get_absolute_url()
    return obj, None
# https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
def my_view(request, slug, id):
    book, book_url = get_redirected(Book, {'pk': id}, {'slug': slug})
    if book_url:
        return redirect(book_url)