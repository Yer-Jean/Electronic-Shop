from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Category
from utils.json_saver import write_to_json_file


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Easy shopping with Dream',
        'sub_title': 'Explore our gadgets catalog',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:6]
        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Dream shop - Categories',
        'sub_title': ''
    }


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    # Переопределяем экстра-контекст, так как у нас подставляются динамические данные
    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Category {category_item.name} products'

        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product_pk'] = product_item.pk
        context_data['title'] = f'{product_item.name}'

        return context_data


def contacts(request):
    context = {
        'title': 'Our Contacts',
        'sub_title': ''
    }
    data = []
    if request.method == 'POST':
        data.append({'name': request.POST.get('name'),
                     'email': request.POST.get('email'),
                     'message': request.POST.get('message')})
        write_to_json_file('messages.json', data)
    return render(request, 'catalog/contacts.html', context)
