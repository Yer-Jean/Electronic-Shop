from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
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
        self.object.views_count += 1  # Увеличиваем счетчик просмотров
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        article_item = Article.objects.get(pk=self.kwargs.get('pk'))
        context_data['article_pk'] = article_item.pk
        context_data['title'] = f'{article_item.title}'

        return context_data


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


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'image', 'is_published')
    success_url = reverse_lazy('blog:articles')
    # Переопределяем страницу в случае успешного обновления

    def get_success_url(self):
        return reverse('blog:article', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog'] = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        return context_data

    # def form_valid(self, form):
    #     obj = form.save()
    #     # send_order_email(obj)
    #     # send_order_email(self.kwargs.get('pk'))
    #     return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')
