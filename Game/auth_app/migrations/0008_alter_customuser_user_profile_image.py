# Generated by Django 4.2.8 on 2023-12-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0007_alter_customuser_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_profile_image',
            field=models.ImageField(default=0, upload_to='profile'),
            preserve_default=False,
        ),
    ]
