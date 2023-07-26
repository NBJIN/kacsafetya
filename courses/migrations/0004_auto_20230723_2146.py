# Generated by Django 3.2 on 2023-07-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_by',
            name='name',
            field=models.CharField(choices=[('health', 'health'), ('safety', 'safety')], max_length=30),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(choices=[('online', 'online'), ('classroom', 'classroom')], max_length=30),
        ),
    ]