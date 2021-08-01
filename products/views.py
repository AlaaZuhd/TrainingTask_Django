
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Product, ProductImage, Cart, Category, CartItem
from .forms import AddToCartForm


def products_list(request):
    # cart_form = AddToCartForm(request.POST or None)
    context = {
        'products': Product.objects.prefetch_related("productimage_set").all(),
        # 'products_images': ProductImage.objects.all(),
        'categories': Category.objects.all(),
        # 'add_to_cart_form': cart_form,
        # 'cart': Cart.objects.all()
    }
    return render(request, "home-page.html", context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def add_to_cart(response):
    if response.method == 'POST':
        print(response.POST)
        quantity = response.POST['quantity']
        product = Product.objects.get(id= response.POST['product_id'])
        try:
            cart = Cart.objects.get(id=response.user.id)
            cart_ = cart
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user= response.user)
            cart_ = cart
        print(cart_)
        cart_item = CartItem.objects.create(size= response.POST['size'],
                                            product= product,
                                            cart= cart_,
                                            quantity= quantity)
        cart_item.save()
    return redirect("home")


def add_category_view(response):
    if response.method == 'POST':
        category_name = response.POST['new-category-item']
        print(category_name)
        get_category = Category.objects.filter(name= category_name)
        print(get_category)
        if(get_category):
            return HttpResponse("Error, category is already exist")
        new_category = Category.objects.create(name= category_name)
        new_category.save()
        print("yes")
        return redirect("home")
    return HttpResponse("error")


def add_product_view(response):
    if response.method == 'POST':
        product_name = response.POST['product-name']
        product_price = response.POST['product-price']
        product_description = response.POST['product-description']
        product_category = response.POST['product-category']
        product_images = response.POST['product-images']
        # product_sizes = response.POST['product-sizes']
        number_of_sizes = response.POST['number-of-sizes']
        sizes_list = []
        product_sizes = '{'
        for i in range(0, int(number_of_sizes)):
            print(response.POST['product-sizes'+str(i+1)])
            sizes_list.append(response.POST['product-sizes'+str(i+1)])
            product_sizes += '"' + response.POST['product-sizes'+str(i+1)] + '":"' + response.POST['product-sizes'+str(i+1)] + '"'
            if i != int(number_of_sizes)-1:
                product_sizes += ', '
            else:
                product_sizes += '}'

        category = Category.objects.filter(name=product_category)
        new_product = Product.objects.create(name=product_name,
                                             description=product_description,
                                             category=category[0],
                                             price=product_price,
                                             sizes=json.loads(product_sizes))
        new_product.save()
        i = 0
        for image in product_images:
            n = product_name + str(i)
            new_image = ProductImage.objects.create(name=n, image=image, default=False, product=new_product)
            new_image.save()
        return redirect("home")
    return HttpResponse("Error")


# class ContactFormView(FormView):
#
#     template_name = 'AddToCart.html'
#     form_class = AddToCartForm
#     success_url = '/products/create'
#
#     # def form_valid(self, form):
#     #     # This method is called when valid form data has been POSTed.
#     #     # It should return an HttpResponse.
#     #     form.send_email()
#     #     return super().form_valid(form)
#
#     def get(self, request, *args, **kwargs):
#
#         form = self.form_class(initial={'quantity': 4})
#         return render(request, self.template_name, {'form': form})
