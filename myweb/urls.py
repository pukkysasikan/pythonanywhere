from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('', views.index, name='index'),
   path('fruit', views.fruit, name='fruit'),
   path('howtoeat', views.howtoeat, name='howtoeat'),
   path('howtodrink', views.howtodrink, name='howtodrink'),
   path('foodlowkcal', views.foodlowkcal, name='foodlowkcal'),
   path('foodlowkcalat', views.foodlowkcalat, name='foodlowkcalat'),
   path('login', views.login_user, name='login'),
   path('logout', views.logout_user, name='logout'),
]