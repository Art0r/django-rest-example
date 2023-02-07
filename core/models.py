from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE

class Account(Model):
    email = CharField(max_length=50)
    password = CharField(max_length=200)
    owner = ForeignKey('auth.User', related_name='accounts', on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']