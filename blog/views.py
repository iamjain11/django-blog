from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Vivek',
        'title':'Blog Post 1',
        'content':'my first blog',
        'date_posted':'Augest 27, 2019'
    },
    {
        'author':'Amar',
        'title':'Blog Post 2',
        'content':'my second blog',
        'date_posted':'Augest 29, 2019'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

