from django.db import models
from shop.models import Gallery

# Create your models here.
class Offer(models.Model):
    choices = (
        
        ("demandeur","demandeur"),
        ("salarie","salarie"),
        ("travailleur","travailleur"),
        ("Etudiant","Etudiant"),
        ("Alternance", "Alternance"),

    )
    name = models.CharField(max_length=200,blank=True,null=True)
    pole = models.CharField(max_length=200,blank=True,null=True)
    desc = models.TextField(blank=True)
    advantages = models.TextField(blank=True)
    type = models.CharField(max_length=200,choices=choices)
    thumbnail = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

class Candidate(models.Model):
    
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    study_level = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    diploma = models.CharField(max_length=200)    
    
    def __str__(self) -> str:
        return self.name