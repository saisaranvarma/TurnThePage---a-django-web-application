from django import forms

from .models import Book,Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name']

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Book name..'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'author name..'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Book price..'})
        }