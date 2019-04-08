from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from userlogin.models import Profile




class UserRegisterForm(UserCreationForm):

    #username = forms.CharField(label='Your name',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})
    address=forms.CharField(min_length=1,max_length=100,required=True,widget=forms.TextInput())
    city = forms.CharField(min_length=1, max_length=100, required=True, widget=forms.TextInput())
    country=forms.CharField(min_length=1, max_length=100, required=True, widget=forms.TextInput())
    pincode=forms.CharField(label='zip')
    phone_number=forms.CharField(min_length=10,max_length=10,required=True,widget=forms.TextInput())
    picture=forms.ImageField( required=False )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):

    credits=forms.CharField(required=False)

    class Meta:
        model=Profile
        fields=['phone_number','credits' ,'picture','address','city','country','pincode','usertype' ]

    def save(self, user=None):
        user_profile=super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user=user
        user_profile.save()
        return user_profile


