from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [
    path('', views.index),
    path('united/', views.united),
    path('login', views.login),
    path('signup', views.signup),
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
    path('admin/', admin.site.urls),
 #   path('accounts/', include('django.contrib.auth.urls'))
]
