from django.contrib import admin
from .models import Product, Comment, Category


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['body', 'author', 'stars', 'active']
    extra = 1
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'body', 'author', 'stars', 'active']
