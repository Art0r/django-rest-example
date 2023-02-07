from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
# from .views import AccountListCreateView, AccountDetailView, UserListView, UserDetailView
from .views import AccountViewSet, UserViewSet
from core.views import api_root

router = DefaultRouter()
router.register(r'account', AccountViewSet, basename='account')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path(r'api/', include(router.urls))
]
