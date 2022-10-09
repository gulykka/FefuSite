from django.db import models


class Profile(models.Model):
    number = models.CharField(max_length=12, verbose_name='Номер телефона', blank=True)
    building = models.ForeignKey('Building', on_delete=models.PROTECT, null=True, verbose_name='Корпус')
    username = models.CharField(max_length=30, verbose_name='Имя')
    photo = models.ImageField(upload_to='photos_user/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-username']


class Publication(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(verbose_name='Текст публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(upload_to='publication/%Y/%m/%d/', blank=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
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
