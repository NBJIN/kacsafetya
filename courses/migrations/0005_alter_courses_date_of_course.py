# Generated by Django 3.2 on 2023-08-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20230723_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='date_of_course',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
