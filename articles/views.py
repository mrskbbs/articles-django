from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def frontpage(request):
    context = {
        "range3": range(0,3),
        "range10": range(0, 20),
    }
    return render(request, 'articles/frontpage.html', context = context)

def article(request):
    context = {
        "range3": range(0,3),
        "range10": range(0, 20),
    }
    return render(request, 'articles/article.html', context=context)

def profile(request):
    context = {
        "range3": range(0,3),
        "range10": range(0, 20),
    }
    return render(request, 'articles/profile.html', context=context)

def articleEditor(request):
    return render(request, 'articles/editor.html')

def auth(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            user = authenticate(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password1']
            )
            # user = User.objects.create_user(
            #     username = form.cleaned_data['username'],
            #     email = form.cleaned_data['email'],
            #     first_name = form.cleaned_data['first_name'],
            #     last_name = form.cle['last_name'],
            #     password = form.cleaned_data['password1']
            # )
            # user.save()
            login(request, user)
            return redirect('articles:frontpage')
    return render(request, 'articles/auth.html')

def log(request):
    if request.POST:
        # login user on error leave
        return redirect('articles:frontpage')
    else:    
        return render(request, 'articles/login.html')