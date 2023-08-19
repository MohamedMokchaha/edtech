from django.contrib import admin
from .models import Offer , Candidate
from django import forms
from django.forms import inlineformset_factory

# Register your models here.



class OfferAdmin(admin.ModelAdmin):
    list_display = ["name","desc","advantages","type","thumbnail"]
    list_filter = ["name","desc","advantages","type","thumbnail"]
    
    class Meta:
        model = Offer
        fields = "__all__"
    
         
admin.site.register(Offer, OfferAdmin)
admin.site.register(Candidate)