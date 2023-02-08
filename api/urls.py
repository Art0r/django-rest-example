from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, UserRetrieveView, UserCreateView

router = DefaultRouter()
router.register(r'account', AccountViewSet, basename='account')
#router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    re_path(r'^user\/$', UserCreateView.as_view()),
    re_path(r'^user\/(?P<pk>[0-9])\/$', UserRetrieveView.as_view()),
    path(r'', include(router.urls))
]
