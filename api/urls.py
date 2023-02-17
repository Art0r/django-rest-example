from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import AccountViewSet, UserRetrieveView, UserCreateView

router = DefaultRouter()
router.register(prefix=r'account', viewset=AccountViewSet, basename='account')

urlpatterns = [
    re_path(r'^user\/$', UserCreateView.as_view(), name='user-create'),
    re_path(r'^user\/<pk>[a-z0-9]+\/$', UserRetrieveView.as_view(), name='user-retrieve'),
] + router.urls
