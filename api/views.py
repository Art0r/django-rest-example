from rest_framework import viewsets
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, response, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from core.models import Account
from django.contrib.auth.models import User
from .serializers import AccountSerializer, UserSerializer
from django.contrib.auth.hashers import make_password
from .permissions import IsOwnerOrReadOnly, IsUser
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (IsUser,)
        
    def perform_create(self, serializer: Serializer):
        serializer.save(
            password=make_password(self.request.data["password"])
        )
    
    def perform_update(self, serializer: Serializer):
        serializer.save(
            password=make_password(self.request.data["password"])
        )
        

# basicamente um CRUD em 4 linhas, impressionante
class AccountViewSet(viewsets.ModelViewSet):
    # o - antes do campo em order_by significa ordem decrescente
    queryset = Account.objects.all().order_by('-created')
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    def perform_create(self, serializer: Serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer()

        # acc = Account.objects.get(pk=kwargs["pk"], owner=request.user)
        acc = get_object_or_404(Account, pk=kwargs['pk'], owner=request.user)
        
        return Response(AccountSerializer(acc).data)
    
    def list(self, request, *args, **kwargs):
        accs = Account.objects.filter(owner=request.user).all()
        serializer = self.get_serializer(
            self.paginate_queryset(accs), 
            many=True)
        
        return self.get_paginated_response(serializer.data)