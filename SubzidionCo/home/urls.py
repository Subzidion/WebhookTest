from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^movies/$', views.MovieView.as_view(), name='movies'),
    url(r'^GitHub/$', views.githubWebhook, name='github'),
]
