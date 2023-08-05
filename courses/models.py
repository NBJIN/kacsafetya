from django.db import models


class Location(models.Model):
    location_choices = (
        ('online', 'online'),
        ('classroom', 'classroom'),
    )

    class Meta:
        verbose_name_plural = "Location"

    name = models.CharField(max_length=30, choices=location_choices)

    def __str__(self):
        return self.name


class Group_By(models.Model):
    group_by_choices = (
        ('health', 'health'),
        ('safety', 'safety'),
    )

    class Meta:
        verbose_name_plural = "Group By"

    name = models.CharField(max_length=30, choices=group_by_choices)

    def __str__(self):
        return self.name


class Courses(models.Model):
    class Meta:
        verbose_name_plural = "Courses"

    title = models.CharField(max_length=250)
    location = models.ForeignKey(
        'Location',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    details = models.CharField(max_length=5000)
    image = models.ImageField(null=True, blank=True)
    group_by = models.ForeignKey(
        'Group_By',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    fee = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    date_of_course = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(max_length=1500, null=True, blank=True)

    def __str__(self):
        return self.title
