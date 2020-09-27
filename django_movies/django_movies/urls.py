from django.contrib import admin
from django.urls import path, include
from core.views import MovieCreateView, MovieUpdateView, MovieDeleteView
from .views import IndexView

app_name='app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('core/', include('core.urls', namespace="core")),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
