# Generated by Django 3.0.3 on 2020-02-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20200227_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]