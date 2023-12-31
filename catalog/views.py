from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from django.shortcuts import get_object_or_404, render

from catalog.services import get_cached_categories


class IndexView(ListView):
    template_name = 'catalog/index.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class ProductDetailView(View):
    template_name = 'catalog/product.html'
    model = Product

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(request, self.template_name, {'product': product})


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров'
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data()
        context_data['cached_categories'] = get_cached_categories()
        return context_data


def contacts(request):
    if request.method == 'POST':
        data = {}
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data['user_1'] = (name, phone, message)
        print(data)
    return render(request, 'catalog/contacts.html')


class ProductCreateView(LoginRequiredMixin, CreateView):
    '''
    Класс для создания нового продукта в интернет-магазине
    '''
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    permission_required = 'catalog.change_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''
    Класс для удаления продукта
    '''
    model = Product
    success_url = reverse_lazy('catalog:index')
    permission_required = 'catalog.delete_product'
