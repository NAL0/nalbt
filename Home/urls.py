#from django.conf.urls import url
from . import views
from django.urls import path

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^mission', views.index2, name='index2'),
#]

urlpatterns = [
    path('', views.index, name='index'),
    path('mission/', views.index2, name='index2'),
    path('constitution/', views.index3, name='index3'),
    ]
