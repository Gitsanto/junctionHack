from django.conf.urls import url
from poop import views

# App namespacing for poop application
app_name = 'poop'
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^predictcoin/$', views.predictcoin, name='predictcoin'),
]
