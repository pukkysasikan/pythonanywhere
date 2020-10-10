from django.urls import path
from . import views

urlpatterns = [
   path('index', views.index, name='index'),
   path('fruit', views.fruit, name='fruit'),
   path('foodlowkcal', views.foodlowkcal, name='foodlowkcal'),
   path('foodlowkcalat', views.foodlowkcalat, name='foodlowkcalat'),
   path('login', views.login_user, name='login'),
   path('logout', views.logout_user, name='logout'),
]