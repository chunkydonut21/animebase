# Generated by Django 2.1.3 on 2018-11-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_auto_20181103_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='name',
            field=models.CharField(blank=True, max_length=120, unique=True),
        ),
    ]
