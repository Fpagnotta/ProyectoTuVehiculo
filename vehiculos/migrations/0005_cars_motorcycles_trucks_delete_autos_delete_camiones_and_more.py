# Generated by Django 4.0.5 on 2022-06-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_alter_autos_transmision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('year', models.FloatField()),
                ('transmision', models.BooleanField(blank=True)),
                ('sku', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
        migrations.CreateModel(
            name='Motorcycles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('year', models.FloatField()),
                ('type', models.CharField(max_length=20)),
                ('sku', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'motorcyle',
                'verbose_name_plural': 'motorcycles',
            },
        ),
        migrations.CreateModel(
            name='Trucks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('year', models.FloatField()),
                ('capacity', models.CharField(max_length=30)),
                ('sku', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'truck',
                'verbose_name_plural': 'trucks',
            },
        ),
        migrations.DeleteModel(
            name='Autos',
        ),
        migrations.DeleteModel(
            name='Camiones',
        ),
        migrations.DeleteModel(
            name='Motos',
        ),
    ]
