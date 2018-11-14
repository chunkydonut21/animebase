from django.contrib import admin
from .models import Genre
from .models import Anime
from .models import Episode

admin.site.register(Genre)
admin.site.register(Anime)
admin.site.register(Episode)