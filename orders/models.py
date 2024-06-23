from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Is Paid?'), default=False)

    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    phone_number = models.CharField(_('Phone Number'), max_length=15)
    address = models.CharField(_('Address'), max_length=700)

    order_notes = models.CharField(_('Order Notes'), max_length=700, blank=True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)

    datetime_created = models.DateTimeField(_('Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', blank=True, null=True,)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productmen = models.ForeignKey('products.ProductMen', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productfeminine = models.ForeignKey('products.ProductFeminine', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productchildish = models.ForeignKey('products.ProductChildish', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productrefriGerator = models.ForeignKey('products.ProductRefriGerator', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productwashing = models.ForeignKey('products.ProductWashing', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productcooking = models.ForeignKey('products.ProductCooking', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productlaptop = models.ForeignKey('products.ProductLaptop', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productheadphone = models.ForeignKey('products.ProductHeadphone', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    productoffice = models.ForeignKey('products.ProductOffice', on_delete=models.CASCADE, related_name='order_items', blank=True, null=True,)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})'

