from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, name, email, phone, password=None, **extra_fields):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have a name')
        user = self.model(name=name, email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class Consumer(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
