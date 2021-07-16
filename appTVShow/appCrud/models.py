from django.db import models
class Show(models.Model):
    title=models.CharField(max_length=100)
    network=models.CharField(max_length=100)
    releaseDate=models.DateField(auto_now_add=True)
    updateDate=models.DateField(auto_now_add=True,null=True)
    description=models.TextField(null=True)
# Create your models here
