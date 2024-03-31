from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz1/', views.quiz1, name='quiz1'),
    path('quiz2/', views.quiz2, name='quiz2'),
    path('quiz3/', views.quiz3, name='quiz3'),
    path('quiz4/', views.quiz4, name='quiz4'),
    path('quiz5/', views.quiz5, name='quiz5'),
    path('update_score/', views.update_score, name='update_score'),
    path('accounts/login/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]

handler404 = views.custom_404_page
