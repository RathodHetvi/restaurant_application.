
from django.db import models
from django.urls import reverse


class Cuision(models.Model):    
    cuisine_type = models.TextField(blank=True,null=False)
   
    def __str__(self) -> str:
        return self.cuisine_type

class Rslist(models.Model):
    
    name   = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)#description
    cuision = models.ManyToManyField(Cuision)
    type = models.CharField(max_length=10, choices=(('veg','veg'), ('non-veg','non-veg')), default="1")
    rating = models.FloatField()
    contact =models.CharField(max_length=10)
    

    def __str__(self) -> str:
        return self.name


class Menulist(models.Model):  
    menu = models.ForeignKey(Rslist,on_delete=models.CASCADE,related_name="sub")#belong which res
    item = models.CharField(max_length=120)#item name
    description = models.TextField(blank=True, null=True)
    ven = models.TextField(max_length=10, choices=(('veg','veg'), ('non-veg','non-veg')), default="1")
    cuision_type = models.ForeignKey(Cuision,on_delete=models.CASCADE,related_name="cuision",default="1")
    price = models.IntegerField()

    
    def __str__(self) -> str:
        return self.item







   