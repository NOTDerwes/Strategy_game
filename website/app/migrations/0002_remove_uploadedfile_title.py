# Generated by Django 4.2.5 on 2023-10-09 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='title',
        ),
    ]