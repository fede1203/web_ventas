# Generated by Django 3.2.5 on 2021-12-16 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppVentas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocinas',
            name='con_horno',
        ),
    ]