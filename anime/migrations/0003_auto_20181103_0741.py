# Generated by Django 2.1.3 on 2018-11-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_auto_20181103_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, upload_to='thumbnails/'),
        ),
    ]