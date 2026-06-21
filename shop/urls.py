from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.homePage, name="home"),
    path('list', views.listproduct, name="all_product_view"),
    path('<int:id>', views.productView, name="product_detail"),
    path('cart/add', views.addToCart, name="add_cart"),
    path('cart/view', views.cartView, name="cart_view"),
    path('cart/decrease', views.decrease, name="decrease"),
    path('purchase', views.purchase, name="purchase"),
    path('pastpurchase', views.PastPurchases, name='pstprc'),
    path('profile', views.viewProfile, name='profile')
]