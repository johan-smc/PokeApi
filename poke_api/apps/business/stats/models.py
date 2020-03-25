from django.db import models


class Stat(models.Model):
    name = models.CharField(max_length=100)
