from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # re_path(r'admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
