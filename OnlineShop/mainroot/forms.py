from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users_order, Manufact, Product


class UserSingUp(UserCreationForm):
    username = forms.CharField(max_length=40)
    password1 = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)


class UserSignIn(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


class UserOrderForm(forms.ModelForm):
    class Meta:
        model = Users_order
        fields = ['users_fio', 'phone_number', 'users_address', 'dest_type']


class FilterForm(forms.Form):
    max_price = forms.IntegerField(required=False)
    min_price = forms.IntegerField(required=False)
    title = forms.CharField(max_length=50, required=False)
    manufactor = forms.ModelChoiceField(queryset=Manufact.objects.all(), required=False)
    title = forms.CharField(max_length=50, required=False)


class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'remain_in_stock']
