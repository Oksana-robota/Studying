from django import forms
from .models import Purchase
from user.models import User
from book.models import Book


class PurchaseForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User.objects.all())
    book_id = forms.ModelChoiceField(queryset=Book.objects.all())
    date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'style': 'width 100px', 'class': 'form-control'}))

    class Meta:
        model = Purchase
        fields = ('user_id', 'book_id', 'date', )
