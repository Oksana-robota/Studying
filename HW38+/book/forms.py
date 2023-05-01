from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    year = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'style': 'width 100px', 'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 100px', 'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'price', )