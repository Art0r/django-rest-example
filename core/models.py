from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
import uuid

# class User(User):
#     USERNAME_FIELD = 'email'
    
#     class Meta:
#         ordering = ['id']


class Account(models.Model):
    id = models.UUIDField(name='id', primary_key=True, 
                          default=uuid.uuid4, editable=False)
    email = models.CharField(name='email', max_length=50)
    password = models.CharField(name='password', max_length=200)
    owner = models.ForeignKey(name='owner', to='auth.User', 
                              related_name='accounts', on_delete=models.CASCADE)
    created = models.DateTimeField(name='created', auto_now_add=True, editable=False)
    updated = models.DateTimeField(name='updated', auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
        
    def __str__(self):
        return self.email