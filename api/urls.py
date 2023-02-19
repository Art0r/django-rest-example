from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import AccountViewSet, UserViewSet

router = DefaultRouter()
router.register(prefix='account', viewset=AccountViewSet, basename='account')
router.register(prefix='user', viewset=UserViewSet, basename='user')

urlpatterns = [
    
] + router.urls
