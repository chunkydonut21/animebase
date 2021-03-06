# Generated by Django 2.1.3 on 2018-11-02 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('aired', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')], default='ongoing', max_length=120)),
                ('views', models.CharField(max_length=120)),
                ('url', models.URLField()),
                ('image', models.URLField()),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('url', models.URLField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.Anime')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(blank=True, to='anime.Genre'),
        ),
    ]
