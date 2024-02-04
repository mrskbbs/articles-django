from django.http import HttpResponse
from django.shortcuts import render

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
