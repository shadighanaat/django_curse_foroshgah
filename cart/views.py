from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _

from .cart import Cart
from .forms import AddToCartProductForm

def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
    })


# @require_POST
# def add_to_cart_view(request, product_id, page_id):
#     cart = request.session.get('cart', {})
#     product_key = f"{product_id}_{page_id}"
#     if product_key in cart:
#         cart[product_key]['quantity'] += 1 
#     else:
#         product = get_object_or_404(Product, id=product_id, page_id=page_id)
#         cart[product_key] = {'title':product.title, 'price': product.price, 'quantity' : 1 }    
#         request.session['cart'] = cart
#         messages.success(request, _('Product successfully added to cart'))
#     return redirect('cart:cart_detail')
    
@require_POST
def add_to_cart_view(request, product_id, page_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id, page_id=page_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart:cart_detail')
    

    # product = get_object_or_404(Product, id=product_id)
   
    # return redirect('cart:cart_detail')

def remove_from_cart(request, product_id, page_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id, page_id=page_id)

    cart.remove(product)

    return redirect('cart:cart_detail')

@require_POST
def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _('All products successfully removed from your cart'))
    else:
        messages.warning(request, _('Your cart is already empty'))

    return redirect('product_list')

