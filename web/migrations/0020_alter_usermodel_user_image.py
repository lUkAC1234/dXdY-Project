# Generated by Django 4.1.2 on 2022-11-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(blank=True, default='avatar2.jpg', null=True, upload_to='media/'),
        ),
    ]
