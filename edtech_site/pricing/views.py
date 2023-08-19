import stripe
from typing import Any, Dict
from .models import *

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from shop.models import (
    Article,
    CartItem,
    Cart,
    Gallery,
    ArticleTag,
    ProductTag,
    Product,
    Price
    )
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import F , Sum

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
class List_Article(LoginRequiredMixin,ListView):
    template_name = './shop/blog_list.html'
    login_url = '/signup/'
    queryset = Article.objects.all()
    context_object_name = 'articles'
    
# class Detail(CreateView)
class Article_Details(LoginRequiredMixin,DetailView):
    template_name = './shop/blog_details.html'
    login_url = '/signup/'
    queryset = Article.objects.all()
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.objects.filter(tags__in=self.object.tags.all()).exclude(id=self.object.id)
        context['price'] = Price.objects.filter(article=self.object).first()
        return context
    
class Article_checkout(LoginRequiredMixin,DetailView):
    login_url = '/signup/'
    """
    This view will be used to display the checkout page
    """
    def post(self, request, *args, **kwargs)-> HttpResponse:
        """
        This method will be used to create a new payment history
        """
        price = Price.objects.get(id=self.kwargs['pk'])
        print(price.id)
        print(f"{settings.BACKEND_DOMAIN}/{price.article.thumbnail.thumbnail.url}")
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'unit_amount': int(price.price * 100),

                    'currency': 'usd',
                    'product_data': {
                        'name': price.article.name,
                        'description': price.article.desc,
                        'images': [
                            
                            f"{settings.BACKEND_DOMAIN}/{price.article.thumbnail.thumbnail.url}"
                            ],
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            metadata={
                'article_id': price.article.id,
            },
            success_url=f'{settings.BACKEND_DOMAIN}/payment_success/',
            cancel_url=f'{settings.BACKEND_DOMAIN}/payment_failed/',
            
        )
        return redirect(checkout_session.url)
        
    
class Payment_Success(TemplateView):
    template_name = './shop/payment_success.html'

class Payment_Failed(TemplateView):
    template_name = './shop/payment_failed.html'
    
    

class CartView(LoginRequiredMixin,ListView):
    """
    cart item view
  
    """
    template_name = './shop/cart_checkout.html'
    context_object_name = 'cart_items'
    login_url = '/signup/'

    def get_queryset(self):
        list_q = []
        item_list = CartItem.objects.filter(cart__user__id=self.request.user.id).values('object_id','quantity','cart__user__id')
        for item in item_list:
            list_q.append(
                {
                    'article_name':Article.objects.get(id=item['object_id']).name,
                    'price':Price.objects.get(article__id=item['object_id']).price,
                    'quantity':item['quantity'],
                }
                )
            
        return list_q
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tot = 0
        quantity = 0
        prices = CartItem.objects.filter(cart__user__id=self.request.user.id)
        for price in prices:
            prc = Price.objects.get(article=price.content_object)
            tot += (prc.price)
            quantity += price.quantity
            
        context['total'] = tot
        context['quantity'] = quantity
        
        return context
    

class AddArticleToCart(LoginRequiredMixin,CreateView):
    login_url = '/signup/'
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        price = Price.objects.get(id=self.kwargs['pk'])
        data = request.POST.get('type')
        if data == 'add_article':
            user_id = request.user.id
            product_instance = Article.objects.get(id=price.article.id)
            content_type = ContentType.objects.get_for_model(product_instance.__class__)
            product = content_type.get_object_for_this_type(id=price.article.id)
            cart,created = Cart.objects.get_or_create(user=request.user)  
            cart_item,created = CartItem.objects.get_or_create(content_type=content_type,object_id=product.id,cart=cart)
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart')
        
        elif data =='add_product':
            user_id = request.user.id
            product_instance = Product.objects.get(id=price.product.id)
            content_type = ContentType.objects.get_for_model(product_instance.__class__)
            product = content_type.get_object_for_this_type(id=price.product.id)
            cart,created = Cart.objects.get_or_create(user=request.user)  
            cart_item,created = CartItem.objects.get_or_create(content_type=content_type,object_id=product.id,cart=cart)
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart')
        else:
            
            return redirect('cart')
            
       
         
        
class RemoveFromCart(LoginRequiredMixin,DeleteView):
    login_url = '/signup/'
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        price = Price.objects.get(id=self.kwargs['pk'])
        user_id = request.user.id
        product_instance = Article.objects.get(id=price.article.id)
        content_type = ContentType.objects.get_for_model(product_instance.__class__)
        product = content_type.get_object_for_this_type(id=price.article.id)
        cart,created = Cart.objects.get_or_create(user=request.user)  
        cart_item= CartItem.objects.get(content_object=product_instance,cart=cart)
        cart_item.delete()
        return redirect('cart')

class UpdateCart(LoginRequiredMixin,UpdateView):
    login_url = '/signup/'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        price = Price.objects.get(id=self.kwargs['pk'])
        user_id = request.user.id
        product_instance = Article.objects.get(id=price.article.id)
        content_type = ContentType.objects.get_for_model(product_instance.__class__)
        product = content_type.get_object_for_this_type(id=price.article.id)
        cart,created = Cart.objects.get_or_create(user=request.user)  
        cart_item= CartItem.objects.get(content_object=product_instance,cart=cart)
        cart_item.quantity = request.POST.get('quantity')
        cart_item.save()
        return redirect('cart')


class CheckoutView(LoginRequiredMixin,CreateView):
    login_url = '/signup/'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        price = Price.objects.get(id=self.kwargs['pk'])
        user_id = request.user.id
        product_instance = Article.objects.get(id=price.article.id)
        content_type = ContentType.objects.get_for_model(product_instance.__class__)
        product = content_type.get_object_for_this_type(id=price.article.id)
        cart,created = Cart.objects.get_or_create(user=request.user)  
        cart_item= CartItem.objects.get(content_object=product_instance,cart=cart)
        cart_item.quantity = request.POST.get('quantity')
        cart_item.save()
        return redirect('cart')

class ProductView(LoginRequiredMixin,ListView):
    template_name = './shop/product.html'
    login_url = '/signup/'
    context_object_name = 'product'
    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price'] = Price.objects.filter(article=self.kwargs['pk']).first()
        return context
        
        