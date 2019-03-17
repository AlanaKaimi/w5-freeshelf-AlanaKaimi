from django import forms
from core.models import Book, Category

class FilterCategory(forms.Form):
    categories = forms.ChoiceField(
        label="Categories",
        widget=forms.widgets.RadioSelect,
        choices=((None, "All Categories"),) + Book.Category_Choices,
        required=False
        )

    def search(self):
        if not self.is_valid():
            return None
        
        data = self.cleaned_data
        books = Book.objects.all()
        if data['categories']:
            books = books.filter(categories=data['categories'])
        return books
