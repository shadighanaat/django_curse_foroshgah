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
                    CommentCreateView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('men/', ProductListMenView.as_view(), name='product_list_men'),
    path('feminine/', ProductListFeminineView.as_view(), name='product_list_feminine'),
    path('childish/', ProductListChildishView.as_view(), name='product_list_childish'),
    path('refrigerator/', ProductListRefrigeratorView.as_view(), name='product_list_refrigerator'),
    path('washing/', ProductListWashingView.as_view(), name='product_list_washing'),
    path('cooking/', ProductListCookingView.as_view(), name='product_list_cooking'),
    path('laptop/', ProductListLaptopView.as_view(), name='product_list_laptop'),
    path('headphone/', ProductListHeadphoneView.as_view(), name='product_list_headphone'),
    path('office/', ProductListOfficeView.as_view(), name='product_list_office'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
]