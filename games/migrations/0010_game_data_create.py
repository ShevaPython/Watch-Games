# Generated by Django 4.2.4 on 2023-09-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_delete_premiermatches_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='data_create',
            field=models.CharField(default='absent', max_length=100, verbose_name='Дата выхода'),
        ),
    ]
