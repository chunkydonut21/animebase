from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import LoginForm, RegisterForm, ContactForm
from django.core.mail import send_mail, BadHeaderError

User = get_user_model()


def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('anime:list')
    return render(request, 'auth/login.html', { 'form': form })


def register_page(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        if new_user:
            return redirect('anime:list')


def logout_view(request):
    logout(request)

    return render(request, "auth/register.html", { "form": form })


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            from_email = form.cleaned_data.get('from_email')
            message = form.cleaned_data.get('message')
            try:
                send_mail(subject, message, from_email, ['shivammahe21@gmail.com'],  fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", { 'form': form })


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
