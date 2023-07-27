from django.db import models


class Mailchimp(models.Model):
    """
    Display details of customer signups to mailchimp
    """
    fullname = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        default=''
    )
    company = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.fullname
