from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signin',views.signin,name='signin'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('product_detail/<int:pk>',views.productdetail,name='productdetail'),
    path('cart/<int:pk>',views.add_to_cart,name='cart'),
    path('cart_to',views.cart,name='cart_to'),
    path('plus_cart',views.plus_cart,name='plus_cart'),
    path('minus_cart',views.minus_cart,name='minus_cart'),
    path('remove_cart',views.remove_cart,name='remove_cart'),
    path('clear_cart',views.clear_cart,name='clear_cart'),
    path('add_product',views.add_product,name='add_product'),
    path('add_category',views.add_category,name='add_category'),
    path('payment',views.payment,name='payment'),
]
