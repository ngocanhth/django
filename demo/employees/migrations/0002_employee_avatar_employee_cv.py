# Generated by Django 4.1 on 2022-08-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(default=None, upload_to='images'),
        ),
        migrations.AddField(
            model_name='employee',
            name='cv',
            field=models.FileField(default=None, upload_to='files'),
        ),
    ]
