from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    biographie = models.TextField(max_length=280)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    specialite = models.CharField(max_length=20,null=False, blank=True)
    experience = models.CharField(max_length=20,null=False, blank=True)
    City =  models.CharField(max_length=20,null=False, blank=True)
    Parcour =  models.CharField(max_length=20,null=False, blank=True)
    linkedin = models.CharField(max_length=20,null=False)
    skills = models.CharField(max_length=280)
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.username
        
class Category(models.Model):
    title = models.CharField(max_length=100) 
    logo = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    top_ten_cat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    def __str__(self):
        return self.title

class language(models.Model):
    langue = models.CharField(max_length=200)
    def __str__(self):
        return self.langue

class subcat(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcat', blank = True, null=True, help_text='Select Only Sub Category')
    title = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')

    def __str__(self):
        return self.title

#############################sujet######################


   


###########cours   
class cours(models.Model):
    title = models.CharField(max_length=70)
    reqs = models.CharField(max_length=2000, blank=True,)
    likes = models.ManyToManyField(User,related_name="cour_likes",blank=True)
    image = models.ImageField(upload_to='media/image_cours')
    image_alt_name = models.CharField(max_length=200, blank=True)
    desciption = models.TextField(blank=True, null=True)
    teacher = models.CharField(max_length=20, default="admin" )
    date = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    langue = models.ForeignKey(language,on_delete=models.CASCADE)
    def num_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title

#folder function
def cour_directory_path(instance,filename):
    return "video_files/cours_{0}/{1}".format(instance.cour.id, filename)
#--videos
class VideoCours(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video=models.FileField(upload_to=cour_directory_path)
    uploaded=models.DateTimeField(auto_now_add=True)
    cour = models.ForeignKey(cours,on_delete=models.CASCADE)
    titre= models.CharField(max_length=200,blank=True)
    chapitre = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.titre
    def delete(self,*args,**kwargs):
        self.video.delete()
        super().delete(*args,**kwargs)
    
class Order(models.Model):
    course = models.ForeignKey(cours,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    ordred = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class notes(models.Model):
    chapitre = models.ForeignKey(VideoCours,on_delete=models.CASCADE)
    text_note = RichTextField(config_name ='notes',blank=True, null=True)
    student = models.ForeignKey(User,models.CASCADE)