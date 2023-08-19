from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import gettext_lazy as _
# Create your models here.
User = settings.AUTH_USER_MODEL

def get_image_filename(instance, filename)->str:
    name = instance.name
    slug = slugify(name)
    return f"image/{slug}-{filename}"

class Gallery(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(_("Description"), blank=True)
    thumbnail = models.ImageField(upload_to=get_image_filename, blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name



class ArticleTag(models.Model):
    name = models.CharField(
        max_length=100, help_text=_("Designates the name of the tag.")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class ProductTag(models.Model):
    name = models.CharField(
        max_length=100, help_text=_("Designates the name of the tag.")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(ArticleTag, blank=True)
    desc = models.TextField(_("Description"), blank=True)
    thumbnail = models.ForeignKey(
            Gallery,
            on_delete=models.CASCADE
        )
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name
    
class Price(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.article.name} {self.price}"
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(ProductTag, blank=True)
    desc = models.TextField(_("Description"), blank=True)
    thumbnail = models.ForeignKey(
            Gallery,
            on_delete=models.CASCADE
        )   
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user}'s cart"

   
class CartItem(models.Model):
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    
    
    def __str__(self) -> str:
        return f"{self.quantity} of {self.content_object.name}"
    
    def get_article(self:object)->str:
        return self.content_object.name


    
    


