from django.db import models


class Courses(models.Model):

    class Meta:
        verbose_name_plural = "Courses"
    details = models.CharField(max_length=5000)
