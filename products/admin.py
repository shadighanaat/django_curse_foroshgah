from django.contrib import admin
from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['body', 'author', 'stars', 'active']
    extra = 0
  
@admin.display(ordering='category__title')
def product_category(self, product):
    return product.category.title

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'body', 'author', 'stars', 'active']
