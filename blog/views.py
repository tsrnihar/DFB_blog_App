from django.shortcuts import render
from django.views.generic import ListView,DetailView
from blog.models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = "home.html"

# Create your views here.

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "detail.html"

