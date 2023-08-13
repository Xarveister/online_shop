from django.shortcuts import render
from django.views import View

from catalog.models import Product
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    products_list = Product.objects.all()

    context = {
        'object_list': products_list,
        'title': 'Главная страница'
    }
    return render(request, 'catalog\index.html', context)


def product(request, pk):
    '''
    Контролер для страницы товара интернет-магазина
    :return: HTTP-ответ с отображением шаблона "product.html"
    '''
    product = get_object_or_404(Product, id=pk)
    return render(request, 'catalog/product.html', {'object': product})

def contacts(request):
    if request.method == 'POST':
        data = {}
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data['user_1'] = (name, phone, message)
        print(data)
    return render(request, 'catalog/contacts.html')
