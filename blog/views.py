from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from pytils.translit import slugify

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Dream shop - Blog',
        'sub_title': ''
    }


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blog:articles')
    extra_context = {
        'title': 'Dream shop - Blog',
        'sub_title': 'Add article'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            # slugify импортируем из pytils - поддержка русского языка - нужно установить
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')
