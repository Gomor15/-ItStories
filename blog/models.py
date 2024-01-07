from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Stories(models.Model):
    POSITION_CHOICES = [
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior '),

    ]
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    working = models.CharField(max_length=20, choices=POSITION_CHOICES)
    photo = models.ImageField(upload_to='images/', blank=True, null=True, default='default.png')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    programming_language = models.ForeignKey('Language', on_delete=models.PROTECT, verbose_name="Языки програмирования")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
        ordering = ['id']


class Language(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    name = models.CharField(max_length=100, db_index=True, verbose_name="Язык")

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']