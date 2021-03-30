from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.urls import path


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts_auth/', include('rest_auth.urls')),
    path('accounts_allauth/', include('allauth.urls')),
    path('accounts_social/', include('accounts_social.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls')),

    path('comments/', include('comments.urls')),
    path('todos/', include('todoapp.urls')),
]
