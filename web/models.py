from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/', default='user.jpg')
    phone = models.CharField(max_length=20, null=True, blank=True)
    instagram_username = models.CharField(max_length=20, null=True, blank=True)
    telegram_username = models.CharField(max_length=20, null=True, blank=True)

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, default='user.jpg', upload_to='blogs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    view_click = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog',
        verbose_name_plural = 'blogs',
        ordering = ('-id', )

class Comment(models.Model):
    name = models.CharField(max_length=100)
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'