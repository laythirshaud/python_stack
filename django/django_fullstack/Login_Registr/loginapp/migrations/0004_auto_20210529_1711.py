# Generated by Django 2.2.4 on 2021-05-29 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20210529_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lasst_name',
            new_name='last_name',
        ),
    ]