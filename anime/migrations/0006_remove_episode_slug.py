# Generated by Django 2.1.3 on 2018-11-03 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_episode_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='slug',
        ),
    ]