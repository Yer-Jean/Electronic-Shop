from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from pytils.translit import slugify

from blog.models import Article
from utils.utils import send_greeting_email


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Dream shop - Blog',
        'sub_title': ''
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        # queryset = queryset.order_by('-created_at')
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1  # Увеличиваем счетчик просмотров
        self.object.save()

        # Если количество просмотров статьи стало 100, то отправляем
        # поздравительное письмо
        if self.object.views_count == 100:
            send_greeting_email(self.object)

        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'image',)
    extra_context = {
        'title': 'Dream shop - Blog',
        'sub_title': 'Add article'
    }

    def get_success_url(self):
        return reverse('blog:article', args=[self.object.slug])

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            # slugify импортируем из pytils - поддержка русского языка - нужно установить
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'image', 'is_published')
    extra_context = {
        'title': 'Dream shop - Blog',
        'sub_title': 'Edit article'
    }

    def get_success_url(self):
        return reverse('blog:article', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog'] = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        return context_data

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
