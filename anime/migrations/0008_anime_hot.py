# Generated by Django 2.1.3 on 2018-11-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_episode_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='hot',
            field=models.BooleanField(default=False),
        ),
    ]
