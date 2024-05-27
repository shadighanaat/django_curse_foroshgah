from django.urls import path

from .views import ProductListView, ProductDetailView, ProductListMenView,  ProductListFeminineView, CommentCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('men/', ProductListMenView.as_view(), name='product_list_men'),
    path('feminine/', ProductListFeminineView.as_view(), name='product_list_feminine'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
]