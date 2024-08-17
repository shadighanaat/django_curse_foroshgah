from django.contrib import admin
from .models import (Product, Comment, Category,
                      ProductMen, 
                      ProductFeminine,
                      ProductChildish, 
                      ProductRefriGerator, 
                      ProductWashing, 
                      ProductLaptop, 
                      ProductHeadphone, 
                      ProductOffice,
                      ProductCooking, 
                      ProductListblog,
                      CartItem,
                     
                     
                     
                      
)



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

@admin.register(ProductMen)
class ProductMenAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active' ]
    inlines = [
        CommentInline
    ]

@admin.register(ProductFeminine)
class ProductFeminineAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active' ]
    inlines = [
        CommentInline
    ]    

@admin.register(ProductChildish)
class ProductChildishAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]            

@admin.register(ProductRefriGerator)
class ProductRefrigeatorAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]    


@admin.register(ProductWashing)
class ProductWashigAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]    

@admin.register(ProductLaptop)
class ProductLaptopAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]    

@admin.register(ProductHeadphone)
class ProductHeadphoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]        

@admin.register(ProductOffice)
class ProductOfficeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]     

@admin.register(ProductCooking)
class ProductcookingeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentInline
    ]     

@admin.register(ProductListblog)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ['title',]
    inlines = [
        CommentInline
    ]         

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'body', 'author', 'stars', 'active']


admin.site.register(CartItem)
