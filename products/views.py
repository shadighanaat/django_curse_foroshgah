from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages


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
                     ProductList,
                     Comment,
)
from .forms import CommentForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductListMenView(generic.ListView):
    queryset = ProductMen.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'


class ProductListFeminineView(generic.ListView):
    queryset = ProductFeminine.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'


class ProductListChildishView(generic.ListView):
    queryset = ProductChildish.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'


class ProductListRefrigeratorView(generic.ListView):
    queryset = ProductRefriGerator.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'


class ProductListWashingView(generic.ListView):
    queryset = ProductWashing.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'


class ProductListCookingView(generic.ListView):
    queryset = ProductCooking.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'    


class ProductListLaptopView(generic.ListView):
    queryset = ProductLaptop.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'    


class ProductListHeadphoneView(generic.ListView):
    queryset = ProductHeadphone.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'    


class ProductListOfficeView(generic.ListView):
    queryset = ProductOffice.objects.filter(active=True)
    template_name = 'products/product_list_men.html'
    context_object_name = 'products'    
            

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)


