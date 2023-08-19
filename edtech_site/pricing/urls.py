from django.urls import path ,include
from django.conf import settings #add this
from .views import (
    List_Article,
    Article_Details,
    Payment_Success,
    Payment_Failed,
    Article_checkout,
    CartView,
    AddArticleToCart,
    )
app_name = "pricing"
urlpatterns = [
path('blog_list/', List_Article.as_view(), name='blog_list'),
path('blog_details/<int:pk>/', Article_Details.as_view(), name='blog_details'),
path('checkout/<int:pk>/', Article_checkout.as_view(), name='checkout'),
path('payment_success/', Payment_Success.as_view(), name='payment_success'),
path('payment_failed/', Payment_Failed.as_view(), name='payment_failed'),
path('cart/', CartView.as_view(), name='cart'),
path('cart_item/<int:pk>/', AddArticleToCart.as_view(), name='add_cart'),
]