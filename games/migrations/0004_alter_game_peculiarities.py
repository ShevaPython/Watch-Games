# Generated by Django 4.2.4 on 2023-09-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_twitch_stream_alter_game_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='peculiarities',
            field=models.ManyToManyField(blank=True, related_name='games', to='games.peculiarities'),
        ),
    ]