# Generated by Django 2.2.24 on 2022-01-04 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20220104_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='person_que',
        ),
    ]
