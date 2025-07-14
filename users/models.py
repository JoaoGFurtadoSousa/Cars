from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import UsuariosManager

class Users(AbstractBaseUser,PermissionsMixin):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
     
    objects = UsuariosManager()

    USERNAME_FIELD = 'email'

    
