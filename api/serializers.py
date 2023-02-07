from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField
from core.models import Account
from django.contrib.auth.models import User

class AccountSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Account
        fields = ['email', 'password', 'updated', 'owner'] # __all__ para todos os campos

class UserSerializer(ModelSerializer):
    accounts = PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'accounts']