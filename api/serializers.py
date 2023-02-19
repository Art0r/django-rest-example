from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, \
    ReadOnlyField, CharField
from core.models import Account
from django.contrib.auth.models import User

class AccountSerializer(ModelSerializer):
    # owner = ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Account
        fields = ('id', 'email', 'password', 'created', 'updated')

class UserSerializer(ModelSerializer):
    accounts = PrimaryKeyRelatedField(many=True, queryset=Account.objects.all(), 
                                      required=False)
    password = CharField(required=True, write_only=True)
    username = CharField(required=True)
    first_name = CharField(required=True)
    last_name = CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'accounts')