from django.shortcuts import render

from utils.json_saver import write_to_json_file


def index(request):
    context = {
        # 'object_list': Category.objects.all(),  # вывод всех объектов
        'title': 'Easy shopping with Dream',
        'sub_title': 'Explore our gadgets catalog'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        # 'object_list': Category.objects.all(),  # вывод всех объектов
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
