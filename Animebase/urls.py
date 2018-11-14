from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from anime.views import AnimeListView
from .views import login_page, register_page, logout_view, emailView, successView
from .sitemaps import StaticViewSitemap, AnimeSitemap, EpisodeSiteMap, AnimeGenreMap

sitemaps = {
    'static': StaticViewSitemap,
    'anime': AnimeSitemap,
    'episode': EpisodeSiteMap,
    'genre': AnimeGenreMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AnimeListView.as_view(), name='list'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_view, name='logout'),
    path('contact/', emailView, name='contact'),
    path('contact/success/', successView, name='success'),
    path('sitemap.xml/', sitemap, { 'sitemaps': sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
    path('anime/', include('anime.urls', namespace='anime')),
    path('jet/', include('jet.urls', namespace='jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
