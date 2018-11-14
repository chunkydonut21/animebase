from django.urls import path

from anime.views import AnimeListView, AnimeDetailView, EpisodeDetailView, LatestAnimeView, DirectoryAnimeView, \
    HotAnimeView, autocomplete

app_name = 'anime'

urlpatterns = [
    path('', AnimeListView.as_view(), name='list'),
    path('search/', autocomplete, name='search'),
    path('latest/', LatestAnimeView.as_view(), name='latest'),
    path('hot/', HotAnimeView.as_view(), name='hot'),
    path('directory/<cat>/', DirectoryAnimeView.as_view(), name='directory'),
    path('<slug>/', AnimeDetailView.as_view(), name='detail'),
    path('<anime>/<episode>/', EpisodeDetailView.as_view(), name='episode_detail'),
]
