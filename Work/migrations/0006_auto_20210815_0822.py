# Generated by Django 3.2.5 on 2021-08-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0005_material_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='short',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='short',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
