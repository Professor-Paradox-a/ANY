from django.db import models

# Create your models here.
class Person(models.Model):
    name =  models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/',blank=True)
    email = models.EmailField(max_length=40,blank = True)
    
    def __str__(self):
        return self.name

class Resources(models.Model):
    resource_name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images',blank= True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='resources')
    
    def __str__(self):
        return self.resource_name

