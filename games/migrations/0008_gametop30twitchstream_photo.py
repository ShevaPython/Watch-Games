# Generated by Django 4.2.4 on 2023-09-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_rename_gametop100_gametop30twitchstream_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gametop30twitchstream',
            name='photo',
            field=models.TextField(db_index=True, default='https://w.forfun.com/fetch/f5/f53d0a93243e09cb47b41dac9d46a42e.jpeg'),
        ),
    ]
