from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _



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
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/',  blank=True,)
    
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
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_feminine', args=[self.pk])  
              
class ProductChildish(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_childish', args=[self.pk])  
    
class ProductRefriGerator(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_refrigerator', args=[self.pk])  
              
class ProductWashing(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_washing', args=[self.pk])

class ProductCooking(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_cooking', args=[self.pk])    
                           
class ProductLaptop(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_laptop', args=[self.pk])   

class ProductHeadphone(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_headphone', args=[self.pk])      

class ProductOffice(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True)
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
        return reverse('product_detail_office', args=[self.pk])  

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

    
    def get_absolute_url(self):
        return reverse('product_detail_blog', args=[self.pk])  

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
        if Product:
           return reverse('product_detail', args=[self.product.id])
# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#     date_added = models.DateTimeField(auto_now_add=True)
 
#     def __str__(self):
#         return f'{self.quantity} x {self.product.name}'
    # def get_absolute_url(self):
    #     return reverse('product_detail_childish', args=[self.product.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail_washing', args=[self.product.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail_cooking', args=[self.product.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail_laptop', args=[self.product.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail_headphone', args=[self.product.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail_refriGerator', args=[self.product.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail_office', args=[self.product.id])
    
    # def get_absolute_url(self):
    #     return reverse('product_detail_blog', args=[self.product.id])