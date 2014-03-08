from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User





class Member(models.Model):
   Dining_member = models.ForeignKey(User)
   cell = models.CharField(max_length=254)
   contact = models.IntegerField(default=0)
   security_money = models.IntegerField(default=0)


class Meal(models.Model):
    dining_user = models.ForeignKey(User)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    guest = models.BooleanField(default=False)
    order_on = models.DateField()


class Payment(models.Model):
    member = models.ForeignKey(User)
    monthly_payment = models.IntegerField(default=0, blank=True, null=True)
    paid_on=models.DateTimeField(auto_now_add=True)









#class MyUserManager(BaseUserManager):
#    def create_user(self, email, synergy_level,
#                    password=None):
#        user = self.model(email=email,
#                          synergy_level=synergy_level)
#        # <--snip-->
#        return user
#
#    def create_superuser(self, email, synergy_level,
#                         password):
#        user = self.create_user(email, synergy_level,
#                                password=password)
#        user.is_team_player = True
#        user.save()
#        return user
#
#class User(AbstractBaseUser):
#    # user = models.OneToOneField(User)
#    username = models.CharField(max_length=254, unique=True)
#    first_name = models.CharField(max_length=30, blank=True)
#    last_name = models.CharField(max_length=30, blank=True)
#    email = models.EmailField(blank=True)
#    synergy_level = models.IntegerField()
#    is_team_player = models.BooleanField(default=False)
#
#    USERNAME_FIELD = 'username'
#    REQUIRED_FIELDS = ['email', 'synergy_level']
#
#    objects = MyUserManager()

