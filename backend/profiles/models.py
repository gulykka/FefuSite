from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class ProfileManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(_('Введите номер телефона'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)


class Profile(AbstractUser):
    username = None
    email = None
    first_name = None
    last_name = None
    phone_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=False)
    building = models.CharField(max_length=30, blank=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'building']

    objects = ProfileManager()

    def __str__(self):
        return self.phone_number


class Publication(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(verbose_name='Текст публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(upload_to='publication/%Y/%m/%d/', blank=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    building = models.ForeignKey('Building', on_delete=models.PROTECT, null=True, verbose_name='Корпус')
    CUSTOMER = 'Клиент'
    MASTER = 'Мастер'
    character = models.CharField(max_length=8, choices=[(CUSTOMER, 'Клиент'), (MASTER, 'Мастер')], default=CUSTOMER,
                                 verbose_name='Роль', )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Building(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'
        ordering = ['title']
