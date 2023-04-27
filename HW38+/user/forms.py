from django import forms
from .models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 100px', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', )

