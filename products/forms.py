from django import forms
from .models import Cart, Product

# iterable
GEEKS_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(AddToCartForm, self).__init__(*args, **kwargs)
    #     if self.instance and self.instance.status_field is not None:
    #         self.fields['status_field'].choices.remove((None, 'Pending'))
    #         print self.fields['status_field'].choices

    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    #     pass