from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todoapp.urls')),
    path('comments/', include('comments.urls')),

    path('accounts/', include('accounts.urls')),
    path('account/', include('allauth.urls')),
    path('account/', include('rest_auth.urls')),
    path('account/registration/', include('rest_auth.registration.urls')),
    path('accounts_social/', include('accounts_social.urls')),
    path('', include('django.contrib.auth.urls')),
]