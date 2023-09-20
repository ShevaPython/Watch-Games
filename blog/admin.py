from django.contrib import admin
from .models import Post, Tag, Commend


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'autor', 'status', 'created', 'updated', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    raw_id_fields = ['autor']
    ordering = ['status', 'publish']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Commend)
class CommendAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    search_fields = ['name', 'email', 'body']
    list_filter = ['name', 'email', 'body']
