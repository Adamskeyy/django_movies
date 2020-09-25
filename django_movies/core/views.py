from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse
from core.models import Movie, AGE_LIMITS
from core.forms import MovieForm
from django.urls import reverse_lazy
import logging


logging.basicConfig(
    filename='log.txt', 
    filemode='w',
    level=logging.INFO,
    )
LOGGER = logging.getLogger(__name__)

class MovieCreateView(CreateView):
    template_name='form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        LOGGER.info(f"Succesfully added {request.__dict__['_post']['title']}")
        return result

class MovieUpdateView(UpdateView):
    template_name='form.html'
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

class MovieDeleteView(DeleteView):
    template_name='delete.html'
    model = Movie
    success_url = reverse_lazy('core:movie_list')

class MovieListView(ListView):
    template_name='movie_list.html'
    model = Movie

class MovieDetailView(DetailView):
    template_name='movie_detail.html'
    model = Movie

class IndexView(MovieListView):
    template_name='index.html'