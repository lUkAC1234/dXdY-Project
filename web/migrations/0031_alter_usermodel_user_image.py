# Generated by Django 4.1.2 on 2022-11-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_alter_usermodel_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(default='user.jpg', upload_to='users/'),
        ),
    ]
