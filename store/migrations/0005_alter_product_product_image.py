# Generated by Django 4.0.6 on 2022-07-21 15:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Product Image'),
        ),
    ]
