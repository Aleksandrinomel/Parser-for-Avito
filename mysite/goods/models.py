from django.db import models

# Create your models here.

class Goods(models.Model):
    name = models.TextField(null=True)
    avito_ad_number = models.IntegerField(null=True)
    publication_date = models.DateField(null=True)
    publication_time = models.TimeField(null=True)
    photo_link = models.TextField(null=True)
    adress = models.TextField(null=True)
    price = models.TextField(null=True)
    text = models.TextField(null=True)
    category = models.TextField(null=True)
    deletion_date = models.DateField(null=True)
    recommendation_list = models.TextField(null=True)




