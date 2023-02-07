from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from core.models import Account
from .serializers import AccountSerializer, UserSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# basicamente um CRUD em 4 linhas, impressionante
class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer: Serializer):
        serializer.save(owner=self.request.user)
