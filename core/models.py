from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

# Create a Book Model

class Book(models.Model):
    """Model representing a book"""
    # Admins can add, edit, and delete books.
    # Books should be in order with the most recently added at the top.
    
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    category = models.ManyToManyFiels('Category', help_text='Select a category for this book')
    # Book URLs should be unique
    URL = 

    slug =

    date_added = models.DateField(null=True, blank=True)

    # Optional: 
    # Add an optional image for books.
    # Allow users to change the order of books, ordering by title or by reverse order of being added.

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def display_category(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_category.short_description = 'Category'

class Category(models.Model):
    """Model representing a book category"""
    name = models.CharField(max_length=200, help_text='Enter a book category (e.g. Science Fiction, etc.)')

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', arg=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

# class Comments()