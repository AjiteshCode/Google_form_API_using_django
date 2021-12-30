from django.db import models
from . import dirs



class FileLoader(models.Model):
    form_name = models.CharField(max_length=100,default="")
    csv_file = models.FileField(upload_to=dirs.upload_csv_files)



class FormName(models.Model):
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class GoogleForm(models.Model):
    name = models.CharField(max_length=100,blank=True,default="")
    type = models.CharField(max_length=25,blank=True,default="")
    options = models.CharField(max_length=100,blank=True,default="")
    mandatory = models.BooleanField(max_length=10,blank=False)
    form_name = models.ForeignKey(FormName,related_name='entries',blank=True,null=False,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name
