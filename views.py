import requests
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    about_html = open("content/about.html").read()
    context = {
    "content": about_html,
    }
    return render(request, "base.html", context)

def blog(request):
    blog_html = open("content/blog.html").read()
    context = {
    "content": blog_html,
    }
    return render(request, "base.html", context)

def portfolio(request):
    portfolio_html = open("content/portfolio.html").read()
    context = {
    "content": portfolio_html,
    }
    return render(request, "base.html", context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

