from django.contrib.auth import backends
from django.contrib.auth.backends import BaseBackend
from firstapp.models import AllUser


class UFModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = AllUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except AllUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return AllUser.objects.get(pk=user_id)
        except AllUser.DoesNotExist:
            return None
