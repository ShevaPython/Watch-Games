# Generated by Django 4.2.4 on 2023-09-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_gametop30twitchstream_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PremierMatches',
        ),
        migrations.AddField(
            model_name='gametop30twitchstream',
            name='premiermatches',
            field=models.TextField(blank=True, null=True),
        ),
    ]