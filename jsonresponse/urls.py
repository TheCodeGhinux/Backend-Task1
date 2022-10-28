from django.contrib import admin
from django.urls import path, include
from base import urls as base_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('jsonresponse/', include(base_urls)),
]