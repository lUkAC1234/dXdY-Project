from django import forms
from .models import UserModel
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput())
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'email', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput()
        }

        def clean_confirm_password(self):

            if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
                raise ValidationError('Passwords do not same')

            return self.cleaned_data['confirm_password']