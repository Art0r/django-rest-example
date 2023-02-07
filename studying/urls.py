from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
