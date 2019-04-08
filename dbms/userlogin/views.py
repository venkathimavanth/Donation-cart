from django.shortcuts import render,redirect
from userlogin.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from userlogin.models import Profile
# Create your views here.
def index(request):
    # Create your views here.

    return render(request, "userlogin\index.html")

def signup(request):
    # Create your views here.
    if request.method=='POST':

        form=UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():

            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            new_user = form.save(commit=False)
            new_user.is_active=True
            new_user.save()
            new_user.refresh_from_db()  # load the profile instance created by the signal
            new_user.save()
            city = form.cleaned_data.get('city')
            address= form.cleaned_data.get('address')
            phone_number = form.cleaned_data.get('phone_number')
            pincode=form.cleaned_data.get('pincode')
            country = form.cleaned_data.get('country')
            picture = form.cleaned_data.get('picture')

            profile = Profile()
            profile.user=new_user
            profile.phone_number = phone_number
            profile.address = address
            profile.picture = picture
            profile.country = country
            profile.pincode=pincode
            profile.city=city
            profile.save()


            return redirect('login')
        print(form)
    else:
        form = UserRegisterForm()

    return render(request, "userlogin\signup.html",{'form':form})

