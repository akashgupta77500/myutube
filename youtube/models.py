
from django.db import models


class Video(models.Model):
    caption = models.CharField(null=True,max_length=100)
    video=models.FileField(null=True)
    thumbnail=models.FileField(null=True)
    type=models.CharField(null=True,max_length=100)
    creationdate = models.DateField(null=True)

    def __str__(self):
        return self.caption
