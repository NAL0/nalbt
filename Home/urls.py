#from django.conf.urls import url
from . import views
from django.urls import path, include

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
    path('plan/', views.index6, name='index6'),
    path('init/', include('Yakisizwe.urls')),
    path('sdgs/01/', views.index7, name='index7'),
    path('sdgs/02/', views.index8, name='index8'),
    path('sdgs/03/', views.index9, name='index9'),
    path('sdgs/04/', views.index10, name='index10'),
    path('sdgs/05/', views.index11, name='index11'),
    path('sdgs/06/', views.index12, name='index12'),
    path('sdgs/07/', views.index13, name='index13'),
    path('sdgs/08/', views.index14, name='index14'),
    path('sdgs/09/', views.index15, name='index15'),
    path('sdgs/10/', views.index16, name='index16'),
    path('sdgs/11/', views.index17, name='index17'),
    path('sdgs/12/', views.index18, name='index18'),
    path('sdgs/13/', views.index19, name='index19'),
    path('sdgs/14/', views.index20, name='index20'),
    path('sdgs/15/', views.index21, name='index21'),
    path('sdgs/16/', views.index22, name='index22'),
    path('sdgs/17/', views.index23, name='index23'),
    path('sdgs/18/', views.index24, name='index24'),
    ]
