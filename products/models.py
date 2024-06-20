from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)
    top_product = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.title


class Discount(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{str(self.discount)} | {self.description}'

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)
    
class ProductMen(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, ) 

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail_men', args=[self.pk])

class ProductFeminine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])  
              
class ProductChildish(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )
       
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])  
    
class ProductRefriGerator(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])  
              
class ProductWashing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

class ProductCooking(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])                           
class ProductLaptop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])   

class ProductHeadphone(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])      

class ProductOffice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])  
    
class ProductListblog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    

class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)



class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Very Good')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productlistblog = models.ForeignKey(ProductListblog, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productmen = models.ForeignKey(ProductMen, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productfeminine = models.ForeignKey(ProductFeminine, on_delete=models.CASCADE, related_name='comments',blank=True, null= True, )
    productchildish = models.ForeignKey(ProductChildish, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productrefrigerator = models.ForeignKey(ProductRefriGerator, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productWashing = models.ForeignKey(ProductWashing, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productcooking = models.ForeignKey(ProductCooking, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productlaptop = models.ForeignKey(ProductLaptop, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productheadphone = models.ForeignKey(ProductHeadphone, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    productoffice = models.ForeignKey(ProductOffice, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, )
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='comment author',
                               )
    body = models.TextField(verbose_name=_('comment text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('what is your score?'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])

    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productlist.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productmen.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productfeminine.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productrefrigerator.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productoffice.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productlaptop.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productchildish.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productcooking.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productWashing.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.productheadphone.id])
