from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput())
    subject = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Your Username' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder': 'Your Password' }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={ "placeholder": "Enter username" }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={ "placeholder": 'Enter email' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder': 'Enter password' }))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={ 'placeholder': 'Confirm password' }))

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email
