from django.urls import path
from products import views

urlpatterns = [
    path('products', views.products_list, name= 'products'),
    path('products/create', views.ContactFormView.as_view(), name= 'create'),
    # path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]