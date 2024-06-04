from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=50)

class ItemInfo(models.Model):
    iten_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to="image")