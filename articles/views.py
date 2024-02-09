import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Article
from .forms import LoginForm, RegisterForm

# Create your views here.
def frontpage(request):
    context = {
        "trending": Article.objects.filter(published__gte = timezone.now() - datetime.timedelta(days=1), published__lte = timezone.now())
    }
    return render(request, 'articles/frontpage.html', context = context)

def article(request, article_pk):
    context = {
        "article": Article.objects.get(url = article_pk),
    }
    return render(request, 'articles/article.html', context=context)

def profile(request, username):
    context = {
        "user": User.objects.get(username = username),
        "posts": Article.objects.filter(author = User.objects.get(username = username))
    }
    return render(request, 'articles/profile.html', context=context)

def articleEditor(request):
    return render(request, 'articles/editor.html')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            form.save()

            user = authenticate(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password1']
            )
            login(request, user)
            
            return redirect('articles:frontpage')
    return render(request, 'articles/signup.html')

def log_in(request):
    if request.POST:
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user: 
            login(request, user)
            return redirect('articles:frontpage')
            
    return render(request, 'articles/login.html')

def log_out(request):
    logout(request)
    return redirect('articles:frontpage')