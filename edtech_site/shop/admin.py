from django.contrib import admin
from .models import (
    Article , 
    Gallery , 
    ArticleTag , 
    Cart, 
    CartItem,
    Product,
    ProductTag,
    Price
)

# Register your models here.
admin.site.register(Article)
admin.site.register(Gallery)
admin.site.register(ArticleTag)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(Price) 