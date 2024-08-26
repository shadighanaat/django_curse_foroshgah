from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.utils.translation import gettext as _

from cart.cart import Cart
from .forms import OrderForm

from .models import OrderItem
from products.models import (Product,
                            ProductMen,
                            ProductFeminine, 
                            ProductChildish, 
                            ProductCooking, 
                            ProductHeadphone, 
                            ProductLaptop, 
                            ProductOffice, 
                            ProductRefriGerator, 
                            ProductWashing,
)

@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('You can not proceed to checkout page because your cart is empty.'))
        return redirect('product_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST, )

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            def get_product_model(product_type):
              if product_type == 'product':
                return Product
              elif product_type == 'productmen':
                  return ProductMen
              elif product_type == 'productfeminine':
                 return ProductFeminine
              elif product_type == 'productchildish':
                  return ProductChildish
              elif product_type == 'productcooking':
                  return ProductCooking
              elif product_type == 'productheadphone':
                  return ProductHeadphone
              elif product_type == 'productlaptop':
                  return ProductLaptop
              elif product_type == 'productoffice':
                  return ProductOffice
              elif product_type == 'productrefrigerator':
                  return ProductRefriGerator
              elif product_type == 'productwashing':
                  return ProductWashing
              else:
                  raise ValueError(f"Unknown product type: {product_type}")
            
            for item in cart:
                product_id = item['id']
                page_id = item['page_id']
                product_type = item.get('product_type')
               
                product_model = get_product_model(product_type)
            
                product = get_object_or_404(product_model , id=product_id, page_id=page_id)
               
                OrderItem.objects.create(
                    order=order_obj,
                 
                    product = product,
                    quantity=item['quantity'],
                    price=item['price'],
                )

            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')

    return render(request, 'orders/order_create.html', {
        'form': order_form,
    })
