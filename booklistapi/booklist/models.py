from django.db import models


class Data(models.Model):
    bookName = models.CharField(max_length=50)
    read = models.BooleanField()


def __str__(self):
    return self.title

# Create your models here.
