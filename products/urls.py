from django.urls import path

from products.api_endpoints import *
from products.api_endpoints.CategoryCreate.views import *
from products.api_endpoints.CategoryDelete.views import *
from products.api_endpoints.CategoryUpdate.views import *
from products.api_endpoints.CategoryList.views   import *
from products.api_endpoints.ColorCreate.views import *
from products.api_endpoints.ColorUpdate.views import *
from products.api_endpoints.ColorDelete.views import *
from products.api_endpoints.ColorList.views import *
from products.api_endpoints.SizeList.views import *
from products.api_endpoints.SizeCreate.views import *
from products.api_endpoints.SizeDelete.views import *
from products.api_endpoints.SizeUpdate.views import *
from products.api_endpoints.BrandCreate.views import *
from products.api_endpoints.BrandUpdate.views import *
from products.api_endpoints.BrandList.views import *



urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name="product-list1"),
    path('list2/', ProductListAPIView2.as_view(), name="product-list2"),
    path('list3/', ProductListAPIView3.as_view(), name="product-list3"),

    path('categories/', CategoryListAPIView.as_view(), name="category-list"),
    path('categories/create/', CategoryCreateAPIView.as_view(), name= 'category-create'),
    path('categories/<str:slug>/', CategoryRetrieveAPIView.as_view(), name="category-detail"),
    path('categories/<str:slug>/update/', CategoryUpdateAPIView.as_view(), name= 'category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name='category-delete'),
    
    path('colors/create/', ColorCreateAPIView.as_view(), name="color-list"),
    path('colors/<str:slug>/', ColorRetrieveAPIView.as_view(), name="color-detail"),
    path('colors/<str:slug>/update/', ColorUpdateAPIView.as_view(), name="color-update"),
    path('colors/<int:pk>/delete/', ColorDeleteAPIView.as_view(), name='color-delete'),

    path('sizes/', SizeListAPIView.as_view(), name="size-list"),
    path('sizes/create/', SizeCreateAPIView.as_view(), name="size-create"),
    path('sizes/<int:pk>/', SizeRetrieveAPIView.as_view(), name="size-detail"),
    path('sizes/<int:pk>/delete/', SizeDeleteAPIView.as_view(), name='size-delete'),
    path('sizes/<int:pk>/update/', SizeUpdateAPIView.as_view(), name='size-update'),

    
    path('brands/', BrandListAPIView.as_view(), name="brand-list"),
    path('brands/create/', BrandCreateAPIView.as_view(), name="brand-list"),
    path('brands/<int:pk>/', BrandRetrieveAPIView.as_view(), name="brand-detail"),
    path('brands/<int:pk>/update', BrandUpdateAPIView.as_view(), name="brand-detail"),
]


