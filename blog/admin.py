from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("post_title" , "post_publish" , "post_author", "post_id")
    list_filter = ("post_title" , "post_publish" , "post_author", "post_id")
    prepopulated_fields = {"post_slug": ("post_title",)}
    search_fields= ("post_title","post_body")
    ordering = ["-post_publish",]
    #raw_id_fields=("post_author",)

admin.site.register(Post,PostAdmin)
