# Generated by Django 4.2.8 on 2023-12-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_games_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sub_category'),
        ),
    ]