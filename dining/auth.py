__author__ = 'geash'

from models import User as CustomUser
from django.contrib.auth.backends import RemoteUserBackend


#class CustomAuth(object):
#
#    def authenticate(self, username=None, password=None):
#        try:
#            user = CustomUser.objects.get(identifier=username)
#            if user.check_password(password):
#                return user
#        except CustomUser.DoesNotExist:
#            return None
#
#    def get_user(self, user_id):
#        try:
#            user = CustomUser.objects.get(pk=user_id)
#            if user.is_active:
#                return user
#            return None
#        except CustomUser.DoesNotExist:
#            return None

#class CustomAuth(RemoteUserBackend):
#    def clean_username(self, username):
#        # remove @REALM from username
#        return username.split("@")[0]