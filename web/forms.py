from django import forms
from .models import UserModel
from django.core.exceptions import ValidationError
from .models import BlogModel, Comment

class BlogModelForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        exclude = ('created_at', 'updated_at', 'user', 'view_click')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('created_at', 'post')

class AccountForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'user_image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))

    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput())
    email = forms.EmailField(max_length=75, widget=forms.TextInput())
    password = forms.CharField(max_length=16, widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords do not same')
        else:
            return self.cleaned_data['confirm_password']

