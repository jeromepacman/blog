from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


User=get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField()
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})


class Comment(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


