# Generated by Django 4.2.8 on 2023-12-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_category_app', '0004_alter_main_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main_img'),
        ),
    ]
