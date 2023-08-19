from django.urls import path ,include
from django.conf import settings #add this
from .views import  ShopView,ProductDetailView

app_name = "shop"

urlpatterns = [
    
path('shop/', ShopView.as_view(), name='shop'),
path('shop/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]


