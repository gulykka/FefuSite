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
    building = models.CharField(max_length=30, blank=False, default="")

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


class Service(models.Model):
    STATUS = (
        ('sent', 'sent'),
        ('approved', 'approved'),
        ('declined', 'declined')
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey('Publication', on_delete=models.PROTECT, null=True, verbose_name='Пост')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUS, default='sent')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.pk)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


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
