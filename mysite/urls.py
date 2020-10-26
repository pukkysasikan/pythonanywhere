from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from myweb import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Logout', auth_views.LogoutView.as_view(), name='logout'),
    path('Login', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('food', views.food, name='food'),
    path('article/<int:id>', views.article, name='article'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
