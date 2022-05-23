from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='store_home'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
