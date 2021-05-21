from django.db import models


# Create your models here.

class ImageUpload(models.Model):
    picture = models.ImageField()
    caption = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
