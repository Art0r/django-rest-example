from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User
from rest_framework.request import Request

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request: Request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user
    
class IsUser(BasePermission):
        
    def has_object_permission(self, request: Request, view, obj):
        user = User.objects.get(pk=obj.pk)
        if request.user.is_anonymous:
            return False
        return (user.username == request.user.username 
                and user.password == request.user.password)
