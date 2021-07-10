from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addition, name='add'),
    path('multi', views.multiplication, name='multi'),
    path('sub', views.substraction, name='sub'),
    path('div', views.division, name='div'),

]
