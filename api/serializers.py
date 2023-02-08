from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, \
    ReadOnlyField, CharField
from core.models import Account
from django.contrib.auth.models import User

class AccountSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Account
        fields = ('id', 'email', 'password', 'updated', 'owner') # __all__ para todos os campos

class UserSerializer(ModelSerializer):
    # accounts = PrimaryKeyRelatedField(many=True, queryset=Account.objects.all(), required=False)
    password = CharField(required=True, write_only=True, label='Senha')
    username = CharField(required=True, label='Nome de Usuário')
    first_name = CharField(required=True, label='Primeiro Nome')
    last_name = CharField(required=True, label='Sobrenome')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        #fields = '__all__'