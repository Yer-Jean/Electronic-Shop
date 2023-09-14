import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Очищаем таблицы от ранее внесенных данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Считываем начальные данные для заполнения БД
        with open('data.json') as f:
            data = json.load(f)

        products = []
        categories = []
        for item in data:
            if item['model'] == 'catalog.category':
                categories.append(Category(
                    id=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description']))
            elif item['model'] == 'catalog.product':
                products.append(Product(
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    image=item['fields']['image'],
                    category_id=item['fields']['category'],
                    price=item['fields']['price']))
        Category.objects.bulk_create(categories)
        Product.objects.bulk_create(products)
