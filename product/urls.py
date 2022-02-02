from django.urls import path 
from . import views

app_name = 'products'
urlpatterns = [
    path('product/', views.Productlistview.as_view(), name='product_list'),
    path('product/<int:id>/', views.Productdetailview.as_view(), name='product_detail')
]