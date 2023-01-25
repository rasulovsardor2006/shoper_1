from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Product(models.Model):
    class ChoiceSize(models.TextChoices):
        XS = 'xs'
        X = 'x'
        M = 'm'
        L = 'l'
        XL = 'xl'

    class ChoiceColor(models.TextChoices):
        BLACK = 'Black'
        WHITE = 'White'
        RED = 'Red'
        BLUE = 'Blue'
        GREEN = 'Green'

    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=155)
    review = models.IntegerField(default=1, null=True, blank=True)
    price = models.FloatField()
    text = models.TextField()
    choice = models.CharField(max_length=55, choices=ChoiceSize.choices, default=ChoiceSize.XL)
    color = models.CharField(max_length=25, choices=ChoiceColor.choices, default=ChoiceColor.WHITE)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)


class UserManager(BaseUserManager):

    def create_user(self,email, password=None,  **kwargs):
        if not email:
            raise ValueError('email not found')
        user = self.model(email=email,  **kwargs)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self,email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=155, unique=False)
    phone_number = models.CharField(max_length=13, validators=[integer_validator])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
