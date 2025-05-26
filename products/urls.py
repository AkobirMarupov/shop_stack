from django.urls import path

from products.api_endpoints import *

from products.api_endpoints.CategoryCRUD.CategoryCreate.views import *
from products.api_endpoints.CategoryCRUD.CategoryDelete.views import *
from products.api_endpoints.CategoryCRUD.CategoryUpdate.views import *
from products.api_endpoints.CategoryCRUD.CategoryList.views   import *
from products.api_endpoints.ColorCRUD.ColorCreate.views import *
from products.api_endpoints.ColorCRUD.ColorUpdate.views import *
from products.api_endpoints.ColorCRUD.ColorDelete.views import *
from products.api_endpoints.ColorCRUD.ColorList.views import *
from products.api_endpoints.SizeCRUD.SizeList.views import *
from products.api_endpoints.SizeCRUD.SizeCreate.views import *
from products.api_endpoints.SizeCRUD.SizeDelete.views import *
from products.api_endpoints.SizeCRUD.SizeUpdate.views import *
from products.api_endpoints.BrandCRUD.BrandCreate.views import *
from products.api_endpoints.BrandCRUD.BrandUpdate.views import *
from products.api_endpoints.BrandCRUD.BrandList.views import *
from products.api_endpoints.BrandCRUD.BrandDelete.views import *
from products.api_endpoints.VariantCRUD.VariantCreate.views import *
from products.api_endpoints.VariantCRUD.VariantUpdate.views import *
from products.api_endpoints.ProductCRUD.ProductCreate.views import *
from products.api_endpoints.ProductCRUD.ProductUpdate.views import *
from products.api_endpoints.ProductCRUD.ProductGetList.views import *
from products.api_endpoints.ProductCRUD.ProductDelete.views import *
from products.api_endpoints.VariantCRUD.VariantDelete.views import *
from products.api_endpoints.VariantCRUD.VariantList.views import *



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
    path('brands/<int:pk>/delete/', BrandDeleteAPIView.as_view(), name='brand-delete'),

    path('variants/', ProductVarianrListAPIView.as_view(), name="variant-list"),
    path('variants/create/', ProductVariantCreateAPIView.as_view(), name="variant-create"),
    path('variants/<int:pk>/', ProductVariantRetrieveAPIView.as_view(), name="variant-detail"),
    path('variants/<int:pk>/update/', ProductVariantUpdateAPIView.as_view(), name="variant-update"),
    path('variants/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name="variant-delete"),

    path('products/', ProductListGetAPIView.as_view(), name="product-list"),
    path('products/create/', ProductCreateAPIView.as_view(), name="product-create"),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name="product-detail"),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name="product-update"),
    path('products/<int:pk>/delete/', ProductVariantDeleteAPIView.as_view(), name="product-delete"),
]


