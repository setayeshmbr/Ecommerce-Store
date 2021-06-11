from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView, ListView

from store.models import Product, Category


class ProductList(ListView):
    queryset = Product.products.all()
    template_name = 'store/home.html'


class ProductDetail(DetailView):
    template_name = 'store/products/product_detial.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug, in_stock=True)


class CategoryList(ListView):
    template_name = 'store/products/category_products_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.all(), slug=slug)
        return category.products.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
