from django.urls import path

from .views import (cart_detail_view, 
                    clear_cart, 
                    add_to_cart_men_view,
                    add_to_cart_laptop_view,
                    add_to_cart_feminine_view,
                    add_to_cart_childish_view,
                    add_to_cart_headphone_view,
                    add_to_cart_washing_view,
                    add_to_cart_cooking_view,
                    add_to_cart_refrigerator_view,
                    add_to_cart_office_view,
                    add_to_cart_view,
                    remove_from_cart,
                    add_to_cart_quantity_view,
)

app_name = 'cart'

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/<page_id>', add_to_cart_view, name='cart_add'),
    path('add/men/<int:product_id>/<page_id>', add_to_cart_men_view, name='cart_add_men'),
    path('add/feminine/<int:product_id>/<page_id>', add_to_cart_feminine_view, name='cart_add_feminine'),
    path('add/childish/<int:product_id>/<page_id>', add_to_cart_childish_view, name='cart_add_childish'),
    path('add/laptop/<int:product_id>/<page_id>', add_to_cart_laptop_view, name='cart_add_laptop'),
    path('add/headphone/<int:product_id>/<page_id>', add_to_cart_headphone_view, name='cart_add_headphone'),
    path('add/washing/<int:product_id>/<page_id>', add_to_cart_washing_view, name='cart_add_washing'),
    path('add/cooking/<int:product_id>/<page_id>', add_to_cart_cooking_view, name='cart_add_cooking'),
    path('add/refrigerator/<int:product_id>/<page_id>', add_to_cart_refrigerator_view, name='cart_add_refrigerator'),
    path('add/office/<int:product_id>/<page_id>', add_to_cart_office_view, name='cart_add_office'),
    path('remove/<int:product_id>/<page_id>', remove_from_cart, name='cart_remove'),
    path('clear/', clear_cart, name='cart_clear'),
    path('add-to-cart/<int:product_id>/<int:page_id>/<str:product_type>/', add_to_cart_quantity_view, name='cart_add_quantity')
   ]