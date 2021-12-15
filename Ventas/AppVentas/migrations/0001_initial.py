# Generated by Django 3.2.5 on 2021-12-15 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blancos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=30)),
                ('plazas', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cocinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=30)),
                ('canti_hornallas', models.IntegerField()),
                ('con_horno', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Electrodomesticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=60)),
                ('modelo', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=30)),
                ('voltage', models.IntegerField()),
            ],
        ),
    ]
