# Generated by Django 5.0.3 on 2024-05-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.CharField(default='June 6, 2017', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]