from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse
from core.models import Movie, AGE_LIMITS
from core.forms import MovieForm
from django.urls import reverse_lazy
import logging
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


logging.basicConfig(
    filename='log.txt', 
    filemode='w',
    level=logging.INFO,
    )

LOGGER = logging.getLogger(__name__)

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class MovieCreateView(StaffRequiredMixin, LoginRequiredMixin, CreateView):
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

class MovieUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name='form.html'
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    def test_func(self):
        super().test_func()
        return self.request.user.is_superuser

class MovieDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name='delete.html'
    model = Movie
    success_url = reverse_lazy('core:movie_list')

    def test_func(self):
        super().test_func()
        return self.request.user.is_superuser

class MovieListView(ListView):
    template_name='movie_list.html'
    model = Movie

class MovieDetailView(DetailView):
    template_name='movie_detail.html'
    model = Movie

# class IndexView(MovieListView):
#     template_name='index.html'