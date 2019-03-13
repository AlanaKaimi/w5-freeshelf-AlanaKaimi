from django.shortcuts import render
from core.models import Book, Category
# Create your views here.

def index(request):
    """View function for home page of site"""

###! place holder for now: -------------->
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    context = {
        'num_books': num_books,
    }
###! <--------------------------------------
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)