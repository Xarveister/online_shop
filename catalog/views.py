from django.shortcuts import render


def index(request):
    return render(request, 'catalog\index.html')


def contacts(request):
    if request.method == 'POST':
        data = {}
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data['user_1'] = (name, phone, message)
        print(data)
    return render(request, 'catalog/contacts.html')
