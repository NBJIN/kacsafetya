from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group_By(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Courses(models.Model):
    class Meta:
        verbose_name_plural = "Courses"

    title = models.CharField(max_length=250)
    location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL)
    fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    details = models.CharField(max_length=5000)
    image = models.ImageField(null=True, blank=True)
    date_of_course = models.DateTimeField(auto_now_add=True)
    group_by = models.ForeignKey('Group_By', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
