# Generated by Django 4.2.6 on 2023-10-18 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='file_upload',
            name='img',
        ),
    ]
