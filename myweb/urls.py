from django.urls import path,include
from django.contrib.auth import views as aunt_views
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('signup', views.sign_up, name='signup'),
   path('logins', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
   path('logout',views.logout, name='logout'),
   path('season',views.season, name='season'),
]