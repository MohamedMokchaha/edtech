from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ShopView(LoginRequiredMixin,TemplateView):
    login_url = '/signup/'
    template_name = 'shop/products.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get product price list 
        context['products'] = Article.objects.all()
        return context

class ProductDetailView(LoginRequiredMixin,DetailView):
    login_url = '/signup/'
    model = Product
    template_name = 'shop/product_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


