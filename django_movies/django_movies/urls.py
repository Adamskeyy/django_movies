from django.contrib import admin
from django.urls import path
from core.models import Genre, Movie
from core.views import hello, movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', movies, name="index")
]
