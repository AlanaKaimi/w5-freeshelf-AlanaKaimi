from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
    # path('<slug:slug>,<int:id>/', views.BookDetailView.as_view(), name='book'), 
    #! path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail,'),
    path('books/', views.BookListView.as_view(), name='books'),

]