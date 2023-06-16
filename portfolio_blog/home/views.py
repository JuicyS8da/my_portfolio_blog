from django.shortcuts import render
from django.views.generic import ListView, DetailView
from home.models import *

def index(request):

    context = {
        'posts': Post.objects.filter(is_published=True)[:2],
        'works': Work.objects.filter(is_published=True)[:3],
        'resume': Resume.objects.all().last(),
        'about': About.objects.all().last(),
        'title': 'Homepage',
    }

    return render(request, 'home/index.html', context)

class Blog(ListView):
    model = Post
    template_name = 'home/blog.html'
    context_object_name = 'posts'
    paginate_by = 4
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class Works(ListView):
    model = Work
    template_name = 'home/works.html'
    context_object_name = 'works'
    paginate_by = 4
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Works'
        return context

    def get_queryset(self):
        return Work.objects.filter(is_published=True)

class ShowPost(DetailView):
    model = Post
    template_name = 'home/blog_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


class ShowWork(DetailView):
    model = Work
    template_name = 'home/blog_post.html'
    slug_url_kwarg = 'work_slug'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context

class ShowPostCategory(ListView):
    model = Post
    template_name = 'home/blog.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

class ShowWorkCategory(ListView):
    model = Work
    template_name = 'home/works.html'
    context_object_name = 'works'
    paginate_by = 4

    def get_queryset(self):
        return Work.objects.filter(tags__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Work'
        return context