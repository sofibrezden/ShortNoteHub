from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Note


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    username = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        max_length=8, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        max_length=8, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Password'})
    )


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category']


class ShareAccessForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
