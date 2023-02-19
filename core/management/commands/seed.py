from faker import Faker
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from core.models import Account
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help="Seeding database"
    
    def handle(self, *args, **options):

        faker = Faker()

        for i in range(2):
            
            username = faker.user_name()
            first_name = faker.first_name()
            last_name = faker.last_name()
            email = faker.email()
            password = make_password('0deioSenhas')
            
            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            
        for i in range(3):
            user = User.objects.all().first()
            
            email = faker.email()
            password='0deioSenhas'
            owner=user
            
            account = Account(
                email=email,
                password=password,
                owner=user
            )
            account.save()
            
        for i in range(3):
            user = User.objects.all().last()
            
            email = faker.email()
            password='0deioSenhas'
            owner=user
            
            account = Account(
                email=email,
                password=password,
                owner=user
            )
            account.save()