# Generated by Django 2.2.24 on 2021-12-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20211123_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='cat_s_papirosoy.jpg', upload_to='avatars/%Y/%n/%d/'),
        ),
    ]
