from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields =       ['order',  
                    'product',  
                    'content_type',
                    'object_id',
                    'quantity', 
                    'price', 
                    ]
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid', ]

    # inlines = [
    #     OrderItemInline,
    # ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order',  
                    'product',  
                    'content_type',
                    'object_id',
                    'quantity', 
                    'price', 
                    ]

