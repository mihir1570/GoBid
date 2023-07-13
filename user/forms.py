from django import forms
from user.models import User,Seller

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "username":forms.TextInput(attrs={'class':'form-control','id':'uname','name':'uname','placeholder':'Enter Username','autocomplete':'off'}),
            "full_name":forms.TextInput(attrs={'class':'form-control','id':'fname','name':'fname','placeholder':'Enter Full Name'}),
            "email":forms.TextInput(attrs={'class':'form-control','id':'email','name':'email','placeholder':'Enter Email'}),
            "password":forms.PasswordInput(attrs={'class':'form-control','id':'pass1','name':'pass1','placeholder':'Enter Password','autocomplete':'off'}),
            "confirm_password":forms.PasswordInput(attrs={'class':'form-control','id':'pass2','name':'pass2','placeholder':'Enter Confirm Password'}),
        }

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"