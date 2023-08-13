from itertools import product

from django.shortcuts import render
from django.views import View

from catalog.models import Product
from django.shortcuts import get_object_or_404, render

class IndexView(View):
    template_name = 'catalog/index.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})

class ProductDetailView(View):
    template_name = 'catalog/product.html'
    model = Product




    # def get(self, request, product_id):
    #     product = get_object_or_404(Product, pk=product_id)
    #     return render(request, self.template_name, {'product': product})
#
# def product(request, pk):
#     '''
#     Контролер для страницы товара интернет-магазина
#     :return: HTTP-ответ с отображением шаблона "product.html"
#     '''
#     product = get_object_or_404(Product, id=pk)
#     return render(request, 'catalog/product.html', {'object': product})

def contacts(request):
    if request.method == 'POST':
        data = {}
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data['user_1'] = (name, phone, message)
        print(data)
    return render(request, 'catalog/contacts.html')
