import os
from pathlib import Path

from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

from InstagramDjango.settings import MEDIA_DIR

UPLOAD_DIR = os.path.join(MEDIA_DIR, 'djangoImages')


class ImageUpload(models.Model):
    picture = CloudinaryField('image', folder=UPLOAD_DIR)
    caption = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
