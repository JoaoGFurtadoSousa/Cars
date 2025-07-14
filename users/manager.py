from django.contrib.auth.models import BaseUserManager
from .models import Users


class Users(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        try:
            search_for_email_in_table_users = Users.objects.get(email = email)
            if search_for_email_in_table_users:
                raise Response({'message':'Email already exists'},status = 403)
        except Users.DoesNotExist:
            email_in_standard = self.normalize_email(email)
            user = self._db