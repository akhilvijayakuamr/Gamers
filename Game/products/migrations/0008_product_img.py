# Generated by Django 4.2.8 on 2023-12-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_product_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=0, upload_to='prod'),
            preserve_default=False,
        ),
    ]
