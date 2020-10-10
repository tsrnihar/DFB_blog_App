from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from blog.models import BlogPost
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = BlogPost
    template_name = "home.html"

# Create your views here.

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "detail.html"

class BlogFormView(CreateView):
    model = BlogPost
    template_name = "PostABlog.html"
    fields = "__all__"

class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = "EditABlog.html"
    fields = ['title','content']

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "DeleteABlog.html"
    success_url = reverse_lazy("blog")

