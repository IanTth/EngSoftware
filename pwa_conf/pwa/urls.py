from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'', views.index),
    url(r'entrar', views.entrar)

] + static(settings.STATIC_URL)