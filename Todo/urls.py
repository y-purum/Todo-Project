from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('todo/', include('todoapp.urls')),
    path('account/', include('rest_auth.urls')),
    path('account/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts_social/', include('accounts_social.urls')),
    path('comments/', include('comments.urls')),
]