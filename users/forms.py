from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'focus:outline-none', 'placeholder': 'demo@gmail.com'}))
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'focus:outline-none', 'placeholder': 'user123'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'focus:outline-none'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'focus:outline-none'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        print('初始化', commit)
        user = super(NewUserForm, self).save(commit=False)
        print('变更后', commit)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
