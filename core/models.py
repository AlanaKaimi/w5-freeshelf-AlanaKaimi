from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=200)

    description = models.TextField(max_length=1000)

    category = models.ManyToManyField('Category', blank=True)

### ! Not working the way I want it to ---------------->
    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])

    display_category.short_description = 'Category'
###! <-------------------------------------------------

    url = models.URLField(max_length=250)

    slug = models.SlugField(unique=True)

    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
# From lecture 3-12 on Slugs
    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        # If the slug is already set, stop here
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        # while we can find a record already in the DB with the slug we're trying to use
        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    

class Category(models.Model):
    """Model representing a book genre."""
    
    name = models.CharField(max_length=200, help_text='Enter a Category (e.g. Python)')
    
    slug = models.SlugField(unique=True)

    def set_slug(self):
        # If the slug is already set, stop here
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        # while we can find a record already in the DB with the slug we're trying to use
        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

    def __str__(self):
        """String for representing the Model object."""
        return self.name

