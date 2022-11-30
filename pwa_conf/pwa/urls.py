from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'novo-ponto', views.nponto),
    url(r'monitoramento', views.monit),
    url(r'informacoes', views.inf),
    url(r'dashboard', views.dash),
    url(r'configuracoes', views.conf),
    url(r'comparativo', views.comp),
    url(r'camera', views.camera),
    url(r'ajuda', views.ajuda),
    url(r'index', views.index),
    url(r'home', views.home),
    url(r'entrar', views.entrar),
    url(r'', views.index)

] + static(settings.STATIC_URL)
