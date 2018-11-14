from django.core.serializers import json
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Anime
from .models import Genre, Episode
import json


class AnimeListView(ListView):
    def get_queryset(self):
        return Anime.objects.all().order_by('-views')

    def get_context_data(self, *, object_list=None, **kwargs):
        qs = Genre.objects.all()
        context = super(AnimeListView, self).get_context_data(**kwargs)
        context['genre_list'] = qs
        return context


class AnimeDetailView(DetailView):
    def get_queryset(self):
        return Anime.objects.all()


class EpisodeDetailView(DetailView):
    template_name = 'anime/episode_detail.html'

    def get_object(self, queryset=None):
        qs = Episode.objects.filter(anime__slug=self.kwargs.get('anime'),
                                    slug__iexact=self.kwargs.get('episode')).first()
        return qs


class LatestAnimeView(ListView):
    template_name = 'anime/anime_latest.html'
    paginate_by = 10

    def get_queryset(self):
        return Anime.objects.order_by('-updated')

    def get_context_data(self, *, object_list=None, **kwargs):
        qs = Genre.objects.all()
        context = super(LatestAnimeView, self).get_context_data(**kwargs)
        context['genre_list'] = qs
        return context


class DirectoryAnimeView(ListView):
    template_name = 'anime/anime_latest.html'
    paginate_by = 10

    def get_queryset(self):
        qs = Anime.objects.filter(genre__name=self.kwargs.get('cat')).order_by('-views')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        qs = Genre.objects.all()
        context = super(DirectoryAnimeView, self).get_context_data(**kwargs)
        context['directory'] = self.kwargs.get('cat').upper()
        context['genre_list'] = qs
        return context


class HotAnimeView(ListView):
    template_name = 'anime/anime_latest.html'
    paginate_by = 10

    def get_queryset(self):
        return Anime.objects.filter(hot=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        qs = Genre.objects.all()
        context = super(HotAnimeView, self).get_context_data(**kwargs)
        context['genre_list'] = qs
        return context


def autocomplete(request):
    if request.is_ajax():
        queryset = Anime.objects.filter(name__istartswith=request.GET.get('q', ''))
        results = []
        for item in queryset:
            anime_json = {
                'id': item.id,
                'label': item.name,
                'value': item.slug
            }
            results.append(anime_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    return HttpResponse(data, 'application/json')
