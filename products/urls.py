from django.urls import path
from products import views

urlpatterns = [
    path('products', views.products_list, name= 'products'),
    path('products/create', views.ContactFormView.as_view(), name= 'create'),
    path('products/p', views.add_to_cart, name="add-to-cart"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name= "logout"),
    path('register', views.register_view, name="register")
    # path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]