from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from .models import Blog
from django.shortcuts import redirect


def home(request):
    blogs = Blog.objects
    return render(request, 'polls/home.html', {'blogs' : blogs})


def new(request):
    return render(request, 'polls/new.html')


def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('polls:home')