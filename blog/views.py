from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Jahir Moreno', 
        'title': 'Blog Post 1', 
        'content': 'First Post content',
        'date_posted': 'December 21, 2018'
    }, 
    {
        'author': 'Iris Nabil', 
        'title': 'Blog Post 2', 
        'content': 'Second Post content',
        'date_posted': 'December 22, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
        }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})