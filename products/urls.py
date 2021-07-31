from django.urls import path
from products import views

urlpatterns = [
    path('ECW', views.products_list, name='home'),
    path('products', views.products_list, name= 'products'),
    path('products/create', views.ContactFormView.as_view(), name= 'create'),
    path('products/addToCart', views.add_to_cart, name="add-to-cart"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name= "logout"),
    path('register', views.register_view, name="register"),
    path('products/addCategory', views.add_category_view, name="add-category"),
    path('products/addProduct', views.add_product_view, name="add-product")
    # path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]