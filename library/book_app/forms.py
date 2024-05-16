from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_publishing': forms.NumberInput(attrs={'class': 'form-control'}),
            'publishing_house': forms.Select(attrs={'class': 'form-control'}),
            'number_of_pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
