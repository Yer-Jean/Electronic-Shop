from django.shortcuts import render

from utils.json_saver import write_to_json_file


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    data = []
    if request.method == 'POST':
        data.append({'name': request.POST.get('name'),
                     'email': request.POST.get('email'),
                     'message': request.POST.get('message')})
        write_to_json_file('messages.json', data)
    return render(request, 'catalog/contacts.html')
