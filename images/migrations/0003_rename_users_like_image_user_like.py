# Generated by Django 4.2.4 on 2023-10-10 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_rename_user_like_image_users_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='users_like',
            new_name='user_like',
        ),
    ]
