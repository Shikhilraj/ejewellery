# Generated by Django 4.2.2 on 2023-09-12 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejewelleryapp', '0003_rename_name_admin_registermodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_registermodel',
            name='phonenumber',
        ),
    ]
