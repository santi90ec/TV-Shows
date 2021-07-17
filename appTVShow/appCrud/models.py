from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['title'])<4:
            errors["title"] = "Titulo debe contener al menos 3 caracteres"
        if len(postData['network'])<3:
            errors["network"] = "Network debe contener al menos 2 caracteres"
        if len(postData['desc'])<11:
            errors["desc"]="Descripcion al menos 10 caracteres"
        return errors
class Show(models.Model):
    title=models.CharField(max_length=100)
    network=models.CharField(max_length=100)
    releaseDate=models.DateField(auto_now_add=True)
    updateDate=models.DateField(auto_now_add=True,null=True)
    description=models.TextField(null=True)
    objects=ShowManager()
# Create your models here
