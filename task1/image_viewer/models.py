from django.db import models

# Create your models here.

class Album_Details(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description =models.TextField(default=" ")

class Images(models.Model):
    id1 = models.ForeignKey(Album_Details,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'Media/image_viewer/')
