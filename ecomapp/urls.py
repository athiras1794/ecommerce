from django.urls import path
from .import views


urlpatterns = [
   path('',views.index,name='index'),
   path('login1',views.login1,name='login1'),
   path('signup',views.signup,name='signup'),
   path('adminlogin',views.adminlogin,name='adminlogin'),
   path('admin_home',views.admin_home,name='admin_home'),
   path('user_home',views.user_home,name='user_home'),
   path('reg',views.reg,name='reg'),
   path('add_category',views.add_category,name='add_category'),
   path('addcat',views.addcat,name='addcat'),
   path('addproduct',views.addproduct,name='addproduct'),
   path('proadd',views.proadd,name='proadd'),
   path('cart',views.cart,name='cart'),
   path('showprdct',views.showprdct,name='showprdct'),
   path('logout1',views.logout1,name='logout1'),
   path('categorized_products/<int:category_id>/', views.categorized_products, name='categorized_products'),
   path('delete/<int:pk>',views.delete,name='delete'),
   path('user_details',views.user_details,name='user_details'),
   path('delete_user/<int:pk>',views.delete_user,name='delete_user'),
   path('cart_details/<int:pk>',views.cart_details,name='cart_details'),
   path('removecart/<int:pk>',views.removecart,name='removecart')



   
]