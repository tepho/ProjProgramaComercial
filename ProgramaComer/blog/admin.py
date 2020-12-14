from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("tittle","slug", "author", "created","updated")
    prepopulated_fields = {"slug":("tittle",)}
# Register your models here.
