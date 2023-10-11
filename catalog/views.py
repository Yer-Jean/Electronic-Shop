from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category, Version
from utils.json_saver import write_to_json_file


class IndexView(TemplateView):
    # template_name = 'catalog/index.html'
    template_name = 'catalog/product_list.html'
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
        context_data['title'] = f'Category {category_item.name}'
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        version_item = Version.objects.filter(product=self.kwargs.get('pk'))
        # Можно вернуть только последнюю версию
        # if version_item:
        #     version_item = version_item.last()
        context_data['product_pk'] = product_item.pk
        context_data['version_item'] = version_item
        context_data['title'] = f'{product_item.name}'

        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Add product',
        'sub_title': ''
    }

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product_pk'] = product_item.pk
        context_data['title'] = f'Edit - {product_item.name}'

        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


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
