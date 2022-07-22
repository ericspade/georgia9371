from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, reverse, redirect
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers

from .filters import NewsFilter
from .forms import NewsForm, ArticleForm
from .models import Post, PostCategory, Category


class NewsList(ListView):
    model = Post
    ordering = ['-time_in']
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10
    queryset = Post.objects.filter(type=0).distinct()

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesList(ListView):
    model = Post
    ordering = ['-time_in']
    template_name = 'articles.html'
    context_object_name = 'news'
    paginate_by = 10
    queryset = Post.objects.filter(type=1).distinct()

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'news'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'newsapp.add_post'
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.type = 0
        news.save()
        return super(NewsCreate, self).form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'newsapp.add_post'
    form_class = ArticleForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.type = 1
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'newsapp.change_post'
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'newsapp.change_post'
    form_class = ArticleForm
    model = Post
    template_name = 'article_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'newsapp.delete_post'
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'newsapp.delete_post'
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('news')


def subscribe(request):
    user = request.user
    print(user)
    category = Category.objects.get(id=request.POST['id_cat'])
    print(category)
    if category.subscribers.filter(id=user.id).exists():
        category.subscribers.remove(user)
    else:
        category.subscribers.add(user)
    return redirect('/')
