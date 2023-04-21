from django.db import models


class Courses(models.Model):
    details = models.CharField(max_length=5000)
