from django.urls import path

from .views import (ProductListView, 
                    ProductListMenView,
                    ProductListFeminineView,
                    ProductListChildishView,
                    ProductListRefrigeratorView,
                    ProductListWashingView,
                    ProductListCookingView,
                    ProductListLaptopView,
                    ProductListHeadphoneView,
                    ProductListOfficeView,
                    ProductDetailView,
                    ContactView,
                    CommentCreateView,
                    ProductBlogView,
                    ProductDetailBloglView,
                    ProductDeleteView,
                    ProductMenDetailView,
                    ProductFeminineDetailView,
                    ProductChildishDetailView,
                    ProductRefrigeratorDetailView,
                    ProductHeadphoneDetailView,
                    ProductCookingDetailView,
                    ProductWashingDetailView,
                    ProductlaptopDetailView,
                    ProductOfficeDetailView,
                    CommentFeminineCreateView,
                    CommentMenCreateView,
                    CommentChildishCreateView,
                    CommentCookingCreateView,
                    CommentWashingCreateView,
                    CommentLaptopCreateView,
                    CommentHeadphoneCreateView,
                    CommentRefriGeratorCreateView,
                    CommentBlogCreateView,
                    CommentOfficeCreateView,
                  
                    )

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('men/', ProductListMenView.as_view(), name='product_list_men'),
    path('men/<int:pk>/', ProductMenDetailView.as_view(), name='product_detail_men'),
    path('feminine/', ProductListFeminineView.as_view(), name='product_list_feminine'),
    path('feminine/زنان/<int:pk>/', ProductFeminineDetailView.as_view(), name='product_detail_feminine'),
    path('childish/', ProductListChildishView.as_view(), name='product_list_childish'),
    path('childish/<int:pk>/', ProductChildishDetailView.as_view(), name='product_detail_childish'),
    path('refrigerator/', ProductListRefrigeratorView.as_view(), name='product_list_refrigerator'),
    path('refrigerator/<int:pk>/', ProductRefrigeratorDetailView.as_view(), name='product_detail_refrigerator'),
    path('washing/', ProductListWashingView.as_view(), name='product_list_washing'),
    path('washing/<int:pk>/', ProductWashingDetailView.as_view(), name='product_detail_washing'),
    path('cooking/', ProductListCookingView.as_view(), name='product_list_cooking'),
    path('cooking/<int:pk>/', ProductCookingDetailView.as_view(), name='product_detail_cooking'),
    path('laptop/', ProductListLaptopView.as_view(), name='product_list_laptop'),
    path('laptop/لپ تاپ/<int:pk>/', ProductlaptopDetailView.as_view(), name='product_detail_laptop'),
    path('headphone/', ProductListHeadphoneView.as_view(), name='product_list_headphone'),
    path('headphone/<int:pk>/', ProductHeadphoneDetailView.as_view(), name='product_detail_headphone'),
    path('office/', ProductListOfficeView.as_view(), name='product_list_office'),
    path('office/<int:pk>/', ProductOfficeDetailView.as_view(), name='product_detail_office'),
    path('blog/', ProductBlogView.as_view(), name='product_list_blog'),
    path('contact/',  ContactView.as_view(), name='contact_list'),
    path('blog/<int:pk>/', ProductDetailBloglView.as_view(), name='product_detail_blog'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/feminine/<int:product_id>/', CommentFeminineCreateView.as_view(), name='comment_create_feminine'),
    path('comment/men/<int:product_id>/', CommentMenCreateView.as_view(), name='comment_create_men'),
    path('comment/office/<int:product_id>/', CommentOfficeCreateView.as_view(), name='comment_create_office'),
    path('comment/childish/<int:product_id>/', CommentChildishCreateView.as_view(), name='comment_create_childish'),
    path('comment/headphone/<int:product_id>/', CommentHeadphoneCreateView.as_view(), name='comment_create_headphone'),
    path('comment/laptop/<int:product_id>/', CommentLaptopCreateView.as_view(), name='comment_create_laptop'),
    path('comment/washing/<int:product_id>/', CommentWashingCreateView.as_view(), name='comment_create_washing'),
    path('comment/cooking/<int:product_id>/', CommentCookingCreateView.as_view(), name='comment_create_cooking'),
    path('comment/refrigerator/<int:product_id>/', CommentRefriGeratorCreateView.as_view(), name='comment_create_refrigerator'),
    path('comment/blog/<int:product_id>/', CommentBlogCreateView.as_view(), name='comment_create_blog'),
    path('delete/', ProductDeleteView.as_view(), name='404_page'),
]