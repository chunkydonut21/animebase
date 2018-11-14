from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import getAnimeInformantion
from django.urls import reverse
from ast import literal_eval

STATUS_CHOICES = (
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed')
)


class Genre(models.Model):
    name = models.CharField(max_length=120, blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime:directory', kwargs={ 'cat': self.name })


class Anime(models.Model):
    name = models.CharField(max_length=120, blank=True)
    aired = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Ongoing', blank=True)
    views = models.IntegerField(null=True, blank=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to="thumbnails/", blank=True)
    slug = models.SlugField(unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    description = models.TextField(blank=True)
    hot = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime:detail', kwargs={ 'slug': self.slug })

    def get_views(self):
        return "{:,}".format(self.views)


class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, unique=True)
    url = models.URLField(max_length=120, blank=True)
    title = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime:episode_detail', kwargs={ 'anime': self.anime.slug, 'episode': self.slug })


def pre_save_anime_receiver(sender, instance, *args, **kwargs):
    if not instance.name:
        getAnimeInformantion(instance.url)

        file = open('info.txt')
        data = literal_eval(file.read())

        instance.name = data.get('name')
        instance.aired = data.get('aired')
        instance.slug = data.get('slug')

        instance.status = data.get('status').strip().lower()
        views = data.get('views')
        views = int(views.replace(',', ''))
        instance.views = views
        instance.description = data.get('description')


pre_save.connect(pre_save_anime_receiver, sender=Anime)


def post_save_anime_receiver(sender, instance, *args, **kwargs):
    file = open('info.txt')
    file_data = file.read()

    if file_data:
        data = literal_eval(file_data)
        for item in data.get('episodeList'):
            qs = instance.episode_set.filter(name=item.get('name'))
            if qs.count() == 0:
                instance.episode_set.create(name=item.get('name'), url=item.get('url'), title=item.get('title'), slug=item.get('slug'))

        for item in data.get('genre'):
            try:
                qs = Genre.objects.get(name=item)
            except Genre.DoesNotExist:
                qs = None
            if qs is None:
                instance.genre.create(name=item)

        open('info.txt', 'w').close()


post_save.connect(post_save_anime_receiver, sender=Anime)

# image, genres
