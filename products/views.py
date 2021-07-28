from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import AddToCartForm
from .models import Product, ProductImage, Cart


def products_list(request):

    context = {
        'products': Product.objects.all(),
        'products_images': ProductImage.objects.all(),
    }
    # print(Product.objects.filter(s__xl='XL'))
    return render(request, "home-page.html", context)


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