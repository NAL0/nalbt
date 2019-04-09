#from django.conf.urls import url
from . import views
from django.urls import path

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^mission', views.index2, name='index2'),
#]

urlpatterns = [
    path('', views.index, name='index'),
    path('sdgs/', views.index2, name='index2'),
    path('con/', views.index3, name='index3'),
    path('speech/', views.index4, name='index4'),
    path('anthem/', views.index5, name='index5'),
    ]
