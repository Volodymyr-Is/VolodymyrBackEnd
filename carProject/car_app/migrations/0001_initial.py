# Generated by Django 5.0.2 on 2024-03-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('price', models.IntegerField()),
                ('distanceTraveled', models.IntegerField()),
                ('maxSpeed', models.IntegerField()),
            ],
        ),
    ]
