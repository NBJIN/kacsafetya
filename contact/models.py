from django.db import models

from datetime import datetime


class Contact(models.Model):
    fname = models.CharField(max_length=60, null=False, blank=False)
    lname = models.CharField(max_length=60, null=False, blank=False)
    company = models.CharField(max_length=200, null=False, blank=False)
    telephone = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    course_title = models.CharField(max_length=250)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.fname
