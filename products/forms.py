from django import forms
from .models import Cart


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = '__all__'

    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    #     pass