from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include('comments.urls')),
    path('todos/', include('todoapp.urls')),
    
    path('account/', include('allauth.urls')),
    path('account/', include('rest_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts_social/', include('accounts_social.urls')),
    path('account/registration/', include('rest_auth.registration.urls')),
    path('', include('django.contrib.auth.urls')),
]
