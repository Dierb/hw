from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.

class Productlistview(ListView):
    queryset = models.Product.objects.filter().order_by('-id')
    template_name = 'product_list.html'

    def get_queryset(self):
        return models.Product.objects.filter().order_by('-id')

class Productdetailview(DetailView):
    template_name = 'product_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=product_id)