from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):

    post_title= models.CharField(max_length=500)
    post_slug = models.SlugField(max_length=500)
    post_author = models.ForeignKey(User, related_name = "blog_posts",on_delete=models.CASCADE)
    post_body = models.TextField()
    post_publish = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(null = True, blank = True)

    #class Meta:
    #    ordering = ("-post_publish",)
    def __str__(self):
        return self.post_title
