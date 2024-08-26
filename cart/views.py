from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import (Product,ProductMen, ProductFeminine, ProductChildish, ProductLaptop,
ProductCooking, ProductOffice, ProductRefriGerator, ProductHeadphone, ProductWashing)
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
        'cart': cart
    })
  
@require_POST
def add_to_cart_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        product = get_object_or_404(Product, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':product.title, 'price': product.price, 'quantity' : quantity, 'image' : product.image.url, 'id' : product.id, 'page_id' : product.page_id ,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'product',}    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')


@require_POST
def add_to_cart_men_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productmen = get_object_or_404(ProductMen, id=product_id, page_id=page_id) 
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
 
        cart[product_key] = {'title': productmen.title , 'price': productmen.price, 'quantity' : quantity, 'image' : productmen.image.url, 'id' : productmen.id, 'page_id' : productmen.page_id,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productmen',}  
        
        request.session['cart'] = cart
        
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')

@require_POST
def add_to_cart_feminine_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productfeminine = get_object_or_404(ProductFeminine, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productfeminine.title, 'price': productfeminine.price, 'quantity' : quantity, 'image' : productfeminine.image.url ,'id' : productfeminine.id, 'page_id' : productfeminine.page_id, 'replace_current_quantity' :  replace_current_quantity, 'product_type' : 'productfeminine',}    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')

@require_POST
def add_to_cart_childish_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productchildish = get_object_or_404(ProductChildish, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productchildish.title, 'price': productchildish.price, 'quantity' : quantity, 'image' : productchildish.image.url, 'id' : productchildish.id, 'page_id' : productchildish.page_id ,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productchildish',}    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')

@require_POST
def add_to_cart_laptop_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productlaptop = get_object_or_404(ProductLaptop, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productlaptop.title, 'price': productlaptop.price, 'quantity' : quantity, 'image' : productlaptop.image.url, 'id' : productlaptop.id, 'page_id' : productlaptop.page_id, 'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productlaptop',
                             }    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')  
    
@require_POST          
def add_to_cart_cooking_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productcooking = get_object_or_404(ProductCooking, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productcooking.title, 'price': productcooking.price, 'quantity' : quantity, 'image' : productcooking.image.url, 'id' : productcooking.id, 'page_id' : productcooking.page_id ,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productcooking',}    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')   
     
@require_POST    
def add_to_cart_office_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productoffice = get_object_or_404(ProductOffice, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productoffice.title, 'price': productoffice.price, 'quantity' : quantity , 'image' : productoffice.image.url, 'id' : productoffice.id, 'page_id' : productoffice.page_id,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productoffice', }    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')   

@require_POST         
def add_to_cart_refrigerator_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productrefrigerator = get_object_or_404(ProductRefriGerator, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productrefrigerator.title, 'price': productrefrigerator.price, 'quantity' : quantity , 'image' : productrefrigerator.image.url, 'id' : productrefrigerator.id, 'page_id' : productrefrigerator.page_id,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productrefrigerator', }    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail') 
 
@require_POST  
def add_to_cart_headphone_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productheadphone = get_object_or_404(ProductHeadphone, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productheadphone.title, 'price': productheadphone.price, 'quantity' : quantity , 'image' : productheadphone.image.url, 'id' : productheadphone.id, 'page_id' : productheadphone.page_id ,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productheadphone',}    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail') 

@require_POST           
def add_to_cart_washing_view(request, product_id, page_id):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    if product_key in cart:
        cart[product_key]['quantity'] += 1 
    else:
        productwashing = get_object_or_404(ProductWashing, id=product_id, page_id=page_id)
        form = AddToCartProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_current_quantity = cleaned_data['inplace']
        cart[product_key] = {'title':productwashing.title, 'price': productwashing.price, 'quantity' : quantity , 'image' : productwashing.image.url ,'id' : productwashing.id, 'page_id' :productwashing.page_id,'replace_current_quantity' :  replace_current_quantity, 'product_type': 'productwashing',}    
        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    return redirect('cart:cart_detail')  

@require_POST 
def remove_from_cart(request, product_id, page_id):
   
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    
    if product_key in cart:
        del cart[product_key]
        messages.success(request, _('Product successfully removed from cart'))
    else:
        messages.error(request, _('Product not found in cart'))

    request.session['cart'] = cart

    return redirect('cart:cart_detail')


@require_POST
def add_to_cart_quantity_view(request, product_id, page_id, product_type):
    cart = request.session.get('cart', {})
    product_key = f"{product_id}_{page_id}"
    
    if product_type == "productlaptop":
        product = get_object_or_404(ProductLaptop, id=product_id, page_id=page_id)
    elif product_type == "productmen":
        product = get_object_or_404(ProductMen, id=product_id, page_id=page_id)
    elif product_type == "productfeminine":
        product = get_object_or_404(ProductFeminine, id=product_id, page_id=page_id)
    elif product_type == "productchildish":
        product = get_object_or_404(ProductChildish, id=product_id, page_id=page_id)
    elif product_type == "productwashing":
        product = get_object_or_404(ProductWashing, id=product_id, page_id=page_id)
    elif product_type == "productcooking":
        product = get_object_or_404(ProductCooking, id=product_id, page_id=page_id)
    elif product_type == "product":
        product = get_object_or_404(Product, id=product_id, page_id=page_id)
    elif product_type == "productheadphone":
        product = get_object_or_404(ProductHeadphone, id=product_id, page_id=page_id)
    elif product_type == "productoffice":
        product = get_object_or_404(ProductOffice, id=product_id, page_id=page_id)
    elif product_type == "productrefrigerator":
        product = get_object_or_404(ProductRefriGerator, id=product_id, page_id=page_id)
    else:
        messages.error(request, _('Invalid product type'))
        return redirect('cart:cart_detail')

    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        replace_current_quantity = cleaned_data['inplace']

        if product_key in cart:
            if replace_current_quantity:
                cart[product_key]['quantity'] = quantity
            else:
                cart[product_key]['quantity'] += quantity
        else:
            cart[product_key] = {
                'title': product.title, 
                'price': product.price, 
                'quantity': quantity, 
                'image': product.image.url, 
                'id': product.id, 
                'page_id': product.page_id, 
                'replace_current_quantity': replace_current_quantity, 
                'product_type': product_type
            }

        request.session['cart'] = cart
        messages.success(request, _('Product successfully added to cart'))
    else:
        messages.error(request, _('Failed to add product to cart'))
    
    return redirect('cart:cart_detail')

@require_POST
def clear_cart(request):
    cart = request.session.get('cart', {})
    del request.session['cart']
    if len(cart):
        cart.clear()
        messages.success(request, _('All products successfully removed from your cart'))
    else:
        messages.warning(request, _('Your cart is already empty'))

    return redirect('product_list')
