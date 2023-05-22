# Generated by Django 3.2 on 2023-05-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lname',
        ),
        migrations.AddField(
            model_name='contact',
            name='fullname',
            field=models.CharField(default='', max_length=150),
        ),
    ]