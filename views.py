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
    context = {}
    return render(request, "portfolio.html", context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

