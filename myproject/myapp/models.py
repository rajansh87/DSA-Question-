from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    userId = models.IntegerField()

class Apartment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    apartmentId = models.IntegerField()
    rent = models.IntegerField()
    rooms = models.IntegerField()
    date = models.dateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apartments')