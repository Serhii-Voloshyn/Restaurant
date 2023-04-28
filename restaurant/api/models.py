from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class EmployeeUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to have is_staff being True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have is_superuser being True')

        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )


class Employee(AbstractUser):

    def update_password(self, new_password):
        self.set_password(new_password)
        self.save()

    def __str__(self):
        return self.email


class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Menu(models.Model):
    date = models.DateField()
    restaurant = models.ForeignKey(
        Restaurant,
        related_name='restaurant',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.restaurant.name + ' ' + str(self.date)


class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    weight = models.IntegerField()
    menu = models.ForeignKey(
        Menu,
        related_name='menu_items',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Vote(models.Model):
    score = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    menu = models.ForeignKey(
        Menu,
        related_name='menu',
        on_delete=models.CASCADE
    )
    employee = models.ForeignKey(
        Employee,
        related_name='employee',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return str(self.menu) + ' ' + str(self.employee)
