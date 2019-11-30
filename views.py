import requests
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    context = {}
    return render(request, "about.html", context)

def blog(request):
    context = {}
    return render(request, "blog.html", context)

def portfolio(request):
    response = requests.get('https://api.github.com/users/DSMindich/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, "portfolio.html", context)



