# Generated by Django 2.1.3 on 2018-11-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_remove_episode_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]