

# Create your models here.
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

   
class UserManager(BaseUserManager):
    def create_user(self, email,username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email,None, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, default =  '')
    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
       return self.email


class StockMalt(models.Model):
  
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50,null= True)
  ebc = models.IntegerField(default=2)
  producer = models.CharField(max_length=50,null= True)
  quantity = models.FloatField(default = 0)
  cost = models.FloatField(default = 0)
  user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='StockMalts')
  def __str__(self):
        return self.name+' EBC = '+str(self.ebc)

class Malt(models.Model):
  
  quantity = models.FloatField(default = 0)
  stockMalt = models.ForeignKey('StockMalt', on_delete=models.CASCADE, related_name='Malts')
  recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='Malts')

  
  

class StockHop(models.Model):
  
  name = models.CharField(max_length=50)
  pellet = models.BooleanField(default=True)
  alpha = models.FloatField(default = 0)  
  producer = models.CharField(max_length=50,null= True)
  quantity = models.FloatField(default = 0)
  cost = models.FloatField(default = 0)
  user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='StockHops')

class Hop(models.Model):
  
  quantity = models.FloatField(default = 0)
  stockHop = models.ForeignKey('StockHop', on_delete=models.CASCADE, related_name='Hops')
  boiling = models.ForeignKey('Boiling', on_delete=models.CASCADE, related_name='Hops')

  

class StockYeast(models.Model): 
  
  name = models.CharField(max_length=50)
  producer = models.CharField(max_length=50,null= True)
  quantity = models.FloatField(default = 0)
  cost = models.FloatField(default = 0)
  user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='StockYeasts')

class Yeast(models.Model): 
  
  quantity = models.FloatField(default = 0)
  stockYeast = models.ForeignKey('StockYeast', on_delete=models.CASCADE, related_name='Yeasts')
  recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='Yeasts')

  
class StockExtra(models.Model):

  name = models.CharField(max_length=50)
  producer = models.CharField(max_length=50,null= True)
  quantity = models.FloatField(default = 0)
  cost = models.FloatField(default = 0)
  user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='StockExtras')

class Extra(models.Model):

  quantity = models.FloatField(default = 0)
  stockExtra = models.ForeignKey('StockExtra', on_delete=models.CASCADE, related_name='Extras')
  boiling = models.ForeignKey('Boiling', on_delete=models.CASCADE, related_name='Extras')
  

class Recipe(models.Model):
  LAGER = 'Lager'
  PILSNER = 'Pilsner'
  WHEAT_BEER ='Wheat Beer'
  PALE_ALE ='Pale Ale'
  IPA = 'IPA'
  STOUT = 'Stout'
  PORTER ='Porter'
  BELGIAN_ALE ='Belgian Ale'
  AMBER_ALE ='Amber Ale'
  BROWN_ALE ='Brown Ale'
  BOCK ='Bock'
  KOLSCH ='Kolsch'
  SAISON ='Saison'
  GOSE ='Gose'
  LAMBIC ='Lambic'
  SOUR_ALE = 'Sour Ale'
  OTHER ='Other'

  FAMILY_CHOICES = [
     (LAGER,'Lager'),
     (PILSNER,'Pilsner'),
     (WHEAT_BEER,'Wheat Beer'),
     (PALE_ALE, 'Pale Ale'),
     (IPA, 'IPA'),
     (STOUT, 'Stout'),
     (PORTER, 'Porter'),
     (BELGIAN_ALE, 'Belgian Ale'),
     (AMBER_ALE,'Amber Ale'),
     (BROWN_ALE, 'Brown Ale'),
     (BOCK, 'Bock'),
     (KOLSCH, 'Kolsch'),
     (SAISON, 'Saison'),
     (GOSE,'Gose'),
     (LAMBIC,'Lambic'),
     (SOUR_ALE, 'Sour Ale'),
     (OTHER, 'Other')
      
  ]
  family = models.CharField(max_length=20,choices=FAMILY_CHOICES,default=LAGER,)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500,null= True)
  volume = models.FloatField(default = 0, null = True)
  alcool = models.FloatField(default = 0, null = True)
  ebc = models.FloatField(default = 0, null = True)
  ibu = models.FloatField(default = 0 , null = True)
  cost = models.FloatField(default = 0 , null = True)
  sale = models.FloatField(default = 0 , null = True)
  private = models.BooleanField(default = True)
  user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='recipes')
  yeast = models.ForeignKey('Yeast', on_delete=models.CASCADE, related_name='recipes', null = True)
  
  

class Brewing(models.Model):
  temperature = models.IntegerField(default = 52)
  time = models.IntegerField(default = 0)
  recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='Brewings')

class Boiling(models.Model):
  cool = models.BooleanField(default = False)
  time = models.IntegerField(default = 60)
  recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='Boilings')

class Fermentation(models.Model):
  temperature = models.IntegerField(default= 19)
  time = models.IntegerField(default = 21)
  recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='Fermentations')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='Likes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name ='Likes')
    created_at = models.DateTimeField(auto_now_add=True)
  
