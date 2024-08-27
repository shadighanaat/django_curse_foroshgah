from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect

from .models import (Product,
                     ProductMen,
                     ProductFeminine,
                     ProductChildish, 
                     ProductRefriGerator,
                     ProductWashing, 
                     ProductCooking, 
                     ProductLaptop,  
                     ProductHeadphone, 
                     ProductOffice, 
                     ProductListblog,
                     Comment,
)
from .forms import CommentForm, CommentBlog
from cart.forms import AddToCartProductForm

class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductListMenView(generic.ListView):
    queryset = ProductMen.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'productmens'
    paginate_by = 8
   
class ProductListFeminineView(generic.ListView):
    queryset = ProductFeminine.objects.filter(active=True)
    template_name = 'products/product_list_feminine.html'
    context_object_name = 'productfeminines'
    paginate_by = 8


class ProductListChildishView(generic.ListView):
    queryset = ProductChildish.objects.filter(active=True)
    template_name = 'products/product_list_childish.html'
    context_object_name = 'productchildishs'
    paginate_by = 8


class ProductListRefrigeratorView(generic.ListView):
    queryset = ProductRefriGerator.objects.filter(active=True)
    template_name = 'products/product_list_Refrigerator.html'
    context_object_name = 'products'
    paginate_by = 8


class ProductListWashingView(generic.ListView):
    queryset = ProductWashing.objects.filter(active=True)
    template_name = 'products/product_list_washing machine.html'
    context_object_name = 'products'
    paginate_by = 8


class ProductListCookingView(generic.ListView):
    queryset = ProductCooking.objects.filter(active=True)
    template_name = 'products/product_list_cooking.html'
    context_object_name = 'products'   
    paginate_by = 8


class ProductListLaptopView(generic.ListView):
    queryset = ProductLaptop.objects.filter(active=True)
    template_name = 'products/product_list_laptop.html'
    context_object_name = 'products'    
    paginate_by = 8


class ProductListHeadphoneView(generic.ListView):
    queryset = ProductHeadphone.objects.filter(active=True)
    template_name = 'products/product_list_headphone.html'
    context_object_name = 'products'    
    paginate_by = 8


class ProductListOfficeView(generic.ListView):
    queryset = ProductOffice.objects.filter(active=True)
    template_name = 'products/product_list_office.html'
    context_object_name = 'products'    
    paginate_by = 8
            


class ProductBlogView(generic.ListView):
    queryset = ProductListblog.objects.filter(active=True)
    template_name = 'products/product_list_blog.html'
    context_object_name = 'products'

class ProductDetailBloglView(generic.DetailView):
    model = ProductListblog
    template_name = 'products/product_detail_blog.html'

    context_object_name = 'productlistblog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form_blog'] = CommentBlog()
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
      
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context
    
class ProductMenDetailView(generic.DetailView):
    model = ProductMen
    template_name = 'products/product_detail_men.html'
      
    context_object_name = 'productmen'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context    
    
class ProductFeminineDetailView(generic.DetailView):
    model = ProductFeminine
    template_name = 'products/product_detail_feminine.html'
      
    context_object_name = 'productfeminine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context

class ProductChildishDetailView(generic.DetailView):
    model = ProductChildish
    template_name = 'products/product_detail_childish.html'
      
    context_object_name = 'productchildish'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context

class ProductHeadphoneDetailView(generic.DetailView):
    model = ProductHeadphone
    template_name = 'products/product_detail_Headphone.html'
      
    context_object_name = 'productheadphone'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context

class ProductCookingDetailView(generic.DetailView):
    model = ProductCooking
    template_name = 'products/product_detail_cooking.html'
      
    context_object_name = 'productcooking'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context

class  ProductlaptopDetailView(generic.DetailView):
    model = ProductLaptop
    template_name = 'products/product_detail_Laptop.html'
      
    context_object_name = 'productlaptop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context

class ProductRefrigeratorDetailView(generic.DetailView):
    model = ProductRefriGerator
    template_name = 'products/product_detail_Refrigerator.html'
      
    context_object_name = 'productrefrigerator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context

class  ProductWashingDetailView(generic.DetailView):
    model = ProductWashing
    template_name = 'products/product_detail_Washing.html'
      
    context_object_name = 'productwashing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context  

class ProductOfficeDetailView(generic.DetailView):
    model = ProductOffice
    template_name = 'products/product_detail_office.html'
      
    context_object_name = 'productoffice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context                              
  
class ProductDeleteView(generic.ListView):
    model = Product
    template_name = 'products/404_page.html'
    success_url = reverse_lazy('product_list')


class ContactView(generic.ListView):
    model = Product
    template_name = 'products/contact_list.html'


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        if Product:
           product = get_object_or_404(Product, id=product_id)
           obj.product = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)
    
    
class CommentFeminineCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_feminine')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductFeminine, id=product_id)
        obj.productfeminine = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)
    
class CommentMenCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_men')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductMen, id=product_id)
        obj.productmen = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)   

class CommentChildishCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_childish')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductChildish, id=product_id)
        obj.productchildish = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)
    
class CommentCookingCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_cooking')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductCooking, id=product_id)
        obj.productcooking = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)


class CommentWashingCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_washing')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductWashing, id=product_id)
        obj.productwashing = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)
    
class CommentLaptopCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_laptop')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductLaptop, id=product_id)
        obj.productlaptop = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)

class CommentHeadphoneCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_headphone')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductHeadphone, id=product_id)
        obj.productheadphone = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)

class CommentRefriGeratorCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_refriGerator')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductRefriGerator, id=product_id)
        obj.productrefriGerator = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)

class CommentBlogCreateView(generic.CreateView):
    model = Comment
    form_class = CommentBlog

    def get_success_url(self):
        return reverse('product_list_blog')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductListblog, id=product_id)
        obj.productlistblog = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)


class CommentOfficeCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list_office')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product= get_object_or_404(ProductOffice, id=product_id)
        obj.productoffice = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)

def submit_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
       
        messages.success(request, _('messages successfully created'))
    return redirect('contact_list') 

def search_view(request):
    query = request.GET.get('query', '').lower()
    if 'خانه' in query or 'home' in query:
        return redirect(reverse('product_list'))
    elif 'مردانه' in query or 'men' in query:
        return redirect(reverse('product_list_men'))
    elif 'زنانه' in query or 'feminine' in query:
        return redirect(reverse('product_list_feminine'))
    elif 'بچگانه' in query or 'childish' in query:
        return redirect(reverse('product_list_childish'))
    elif 'پخت و پز' in query or 'cooking' in query:
        return redirect(reverse('product_list_cooking'))
    elif 'اداری' in query or 'office' in query:
        return redirect(reverse('product_list_office'))
    elif 'لپ‌تاپ' in query or 'laptop' in query:
        return redirect(reverse('product_list_laptop'))
    elif 'هدفون' in query or 'headphone' in query:
        return redirect(reverse('product_list_headphone'))
    elif 'یخچال' in query or 'refrigerator' in query:
        return redirect(reverse('product_list_refrigerator'))
    elif 'لباسشویی' in query or 'washing' in query:
        return redirect(reverse('product_list_washing'))
    elif 'وبلاگ' in query or 'blog' in query:
        return redirect(reverse('product_list_blog'))
    else:
        return redirect(reverse('product_list'))    