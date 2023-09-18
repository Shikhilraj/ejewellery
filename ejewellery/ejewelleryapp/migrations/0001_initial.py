# Generated by Django 4.2.2 on 2023-08-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='c_registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('pincode', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
