from django.db import models
from django.urls import reverse

class Rslist(models.Model):
    
    name   = models.CharField(max_length=120)
    content = models.TextField()
  
    
    
    def get_absolute_url(self):
        return reverse("rslist:rslist-detail", kwargs={"id": self.id})

    def __str__(self) -> str:
        return self.name

  


class Menulist(models.Model):
    item = models.CharField(max_length=120)
    price = models.IntegerField()
    menu = models.ForeignKey(Rslist,on_delete=models.CASCADE)
   

    # def  get_absolute_url(self):
    #     return reverse("menulist:menulist-detail",kwargs={"menu_id": self.id})
    
    def __str__(self) -> str:
        return self.item

# class Cuision(models.Model):
#     type = models.CharField(max_length=120)




   