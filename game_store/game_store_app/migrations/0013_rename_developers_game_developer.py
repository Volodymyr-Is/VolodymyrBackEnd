# Generated by Django 5.0.3 on 2024-05-04 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_store_app', '0012_remove_game_developers_game_developers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='developers',
            new_name='developer',
        ),
    ]