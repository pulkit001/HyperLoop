# Generated by Django 3.2.5 on 2021-08-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]