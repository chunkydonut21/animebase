from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from anime.models import Anime, Episode, Genre


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['login', 'register', 'logout', 'contact', 'success', 'anime:list', 'anime:hot']

    def location(self, obj):
        return reverse(obj)


class AnimeSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Anime.objects.all()


class EpisodeSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Episode.objects.all()


class AnimeGenreMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Genre.objects.all()
