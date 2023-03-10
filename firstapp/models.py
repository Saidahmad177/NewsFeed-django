from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=NewsBase.Status.published)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class NewsBase(models.Model):

    class Status(models.TextChoices):
        draft = 'DF', 'Draft'
        published = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='firstapp/images', default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.draft
                              )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('detail_page', args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email


class AllUser(models.Model):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)


class Comments(models.Model):
    news = models.ForeignKey(NewsBase, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']
