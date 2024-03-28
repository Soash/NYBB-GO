from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz1', views.quiz1, name='quiz1'),
    path('quiz2', views.quiz2, name='quiz2'),
    path('quiz3', views.quiz3, name='quiz3'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]

handler404 = views.custom_404_page
