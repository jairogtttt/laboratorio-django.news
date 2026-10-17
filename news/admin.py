from django.contrib import admin
from .models import Category, Author, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_at')
    list_filter = ('categories', 'published_at', 'author')
    search_fields = ('title', 'summary', 'body')
    prepopulated_fields = {'slug': ('title',)}