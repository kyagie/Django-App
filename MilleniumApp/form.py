from django import forms
from MilleniumApp.models import Buyer

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = "__all__"