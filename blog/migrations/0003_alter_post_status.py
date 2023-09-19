# Generated by Django 4.2.4 on 2023-09-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_slag_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
    ]