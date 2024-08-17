from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import reverse
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

class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        Add the specified product to the cart if it exists
        """
        product_key = str(product.id)
       

        if product_key not in self.cart:
            self.cart[product_key] = {'quantity': 0}

        if replace_current_quantity:
            self.cart[product_key]['quantity'] = quantity
        else:
            self.cart[product_key]['quantity'] += quantity

        messages.success(self.request, _('Product successfully added to cart'))

        self.save()

    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_key = str(product.id)

        if product_key in self.cart:
            del self.cart[product_key]
            messages.success(self.request, _('Product successfully removed from cart'))
            self.save()


    def save(self):
        """
        Mark session as modified to save changes
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
       
        
        products = Product.objects.filter(id__in=product_ids) 
         
       
        cart = self.cart.copy()
    

        for product in products:
              cart[str(product.id)(product.page_id)]['product_obj'] = product
              # for item in cart.values():
              #   item['total_price'] = cart[str(product.id)(product.page_id)]['product_obj'].price * item['quantity']
              #   yield item
        for item in cart.values():
              item['total_price'] =item['price'] * item['quantity']
              yield item
              
        # productmen = ProductMen.objects.filter(id__in=product_ids)    
        # cart = self.cart.copy()
        # if productmen:
          
        #   for product in productmen:
        #     cart[str(product.id)]['product_obj'] = product
            
        productfeminine = ProductFeminine.objects.filter(id__in=product_ids) 
        cart = self.cart.copy()
        if productfeminine:
          
          for product in productfeminine:
            cart[str(product.id)]['product_obj'] = product
            # for item in cart.values():
            #   item['total_price'] = cart[str(product.id)]['product_obj'].price * item['quantity']
            #   yield item
            for item in cart.values():
              item['total_price'] = cart[str(product.id)]['product_obj'].price * item['quantity']
              yield item    
               
         
        productchildish = ProductChildish.objects.filter(id__in=product_ids)    
        cart = self.cart.copy()
        if productchildish:
          
          for product in productchildish:
            cart[str(product.id)]['product_obj'] = product
          for item in cart.values():
            item['total_price'] = cart[str(product.id)]['product_obj'].price * item['quantity']
            yield item

        productlaptop = ProductLaptop.objects.filter(id__in=product_ids)    
        cart = self.cart.copy()
        if productlaptop:
          
          for product in productlaptop:
            cart[str(product.id)]['product'] = product
          for item in cart.values():
            item['total_price'] = cart[str(product.id)]['product_obj'].price * item['quantity']
            yield item

        # productrefriGerator = ProductRefriGerator.objects.filter(id__in=product_ids)    
        # cart = self.cart.copy()
        # if productrefriGerator:
          
        #   for product in productrefriGerator:
        #     cart[str(product.id)]['product_obj'] = product   

        # productwashing = ProductWashing.objects.filter(id__in=product_ids)    
        # cart = self.cart.copy()
        # if productwashing:
          
        #   for product in productwashing:
        #     cart[str(product.id)]['product_obj'] = product 

        productcooking = ProductCooking.objects.filter(id__in=product_ids)    
        cart = self.cart.copy()
        if productcooking:
          
          for product in productcooking:
            cart[str(product.id)]['product_obj'] = product   
          for item in cart.values():
            item['total_price'] = cart[str(product.id)]['product_obj'].price * item['quantity']
            yield item  

        productoffice = ProductOffice.objects.filter(id__in=product_ids)    
        cart = self.cart.copy()
        if productoffice:
          
          for product in productoffice:
            cart[str(product.id)]['product_obj'] = product    

        productheadphone = ProductHeadphone.objects.filter(id__in=product_ids)    
        cart = self.cart.copy()
        if productheadphone:
          
          for product in productheadphone:
            cart[str(product.id)]['product_obj'] = product        

          for item in cart.values():
            item['total_price'] = cart[str(product.id)]['product_obj'].price * item['quantity']
            yield item      
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        
        return sum(item['quantity'] * item['price'] for item in self.cart.values())
    
    def is_empty(self):
        if self.cart:
            return False
        return True
    
       
