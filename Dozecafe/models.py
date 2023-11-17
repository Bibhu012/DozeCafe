from django.db import models



# Create your models here.
class coffee_section_2(models.Model):
    #name : str
    name = models.CharField(max_length=50)
    #img : str
    img = models.ImageField(upload_to ='pics')
    #desc : str
    desc = models.TextField()
    #price : int
    price = models.IntegerField()
    #offer : bool
    offer = models.BooleanField(default=False)