from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class ImageUpload(models.Model):
    picture = CloudinaryField('image')
    caption = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
