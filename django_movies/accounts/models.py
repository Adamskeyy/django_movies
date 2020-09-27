from django.db.models import CASCADE, Model, OneToOneField, IntegerField
from django.contrib.auth.models import User

class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    shoeSize = IntegerField(null=True, blank=True)
