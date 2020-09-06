from django.contrib import admin
from core.models import Movie, Genre
from django.urls import path

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
