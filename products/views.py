from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Product, ProductImage, Cart, Category, CartItem
from .forms import AddToCartForm


def products_list(request):
    cart_form = AddToCartForm(request.POST or None)

    context = {
        'products': Product.objects.prefetch_related("productimage_set").all(),
        'products_images': ProductImage.objects.all(),
        'categories': Category.objects.all(),
        'add_to_cart_form': cart_form,
        'cart': Cart.objects.all()
    }
    return render(request, "home-page.html", context)

def add_to_cart(response):
    if response.method == 'POST':
        print(response.POST)
        quantity = response.POST['quantity']
        product = Product.objects.get(id= response.POST['product_id'])
        cart = Cart.objects.get(id= response.POST.user.id)
        # if cart not none then done else we need to create a new cart for this user
        cart_item = CartItem(size= response.POST['size'], product= product, cart= cart, quantity= quantity)
        cart_item.save()
    return HttpResponse("success")


class ContactFormView(FormView):

    template_name = 'AddToCart.html'
    form_class = AddToCartForm
    success_url = '/products/create'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial={'quantity': 4})
        return render(request, self.template_name, {'form': form})
