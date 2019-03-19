# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff,
                     is_superuser, **extra_fields):
        if not email:
            raise  ValueError('El email es obligatorio')
        email= self.normalize_email(email)
        user= self.model(username=username, email=email, is_active=True,
                         is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,password,False,False,**extra_fields)
    def create_superuser(self,username,email,password,**extra_fields):
        return self._create_user(username,email,password,True,True,**extra_fields)



class User(AbstractBaseUser, PermissionsMixin):


    TRABAJADOR = 'TRA'
    GERENTE = 'GER'

    USER_TYPE_CHOICES = (
        (TRABAJADOR, 'Trabajador'),
        (GERENTE, 'Gerente'),
    )

    cellphone = models.CharField('Celular', max_length=15, blank=True, null=True)
    dni = models.CharField('Dni', max_length=8, blank=False, null=True)
    email=models.EmailField(max_length=30)
    first_name=models.CharField('Nombres', max_length=100)
    last_name= models.CharField('Apellidos', max_length=100)
    username = models.CharField(max_length=30, unique=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    user_type = models.CharField('tipo de usuario', choices=USER_TYPE_CHOICES, max_length=10, blank=False,null=False,
                                default=TRABAJADOR )

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name+' '+self.last_name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'







