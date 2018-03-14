from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render_to_response

def index (request):
    return render_to_response('app/index.html')
# Create your models here.

import os
def content_file_name(instance, filename):
    extension = filename.split('.')[-1]
    filename = "%s_%s_%s.%s" % (instance.post_id, instance.post_title, instance.post_publish, extension)
    valid_extensions = ["bmp","jpg"]
    #print(extension)
#    if not extension in valid_extensions:
#        print(extension)
    #    return render_to_response('blog_post/image_not_allowed_to_upload.html')
#    else:
    return "%s_%s_%s/%s" %(instance.post_id, instance.post_title,instance.post_publish, filename)

class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    post_title= models.CharField(max_length=500)
    post_slug = models.SlugField(max_length=500)
    post_author = models.ForeignKey(User, related_name = "blog_posts",on_delete=models.CASCADE)
    post_body = models.TextField()
    post_publish = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(upload_to=content_file_name, null = True, blank = True)

    #class Meta:
    #    ordering = ("-post_publish",)
    def __str__(self):
        return self.post_title
