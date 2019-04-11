from django.shortcuts import render,redirect
from userlogin.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from userlogin.models import Profile
from .forms import UserRegisterForm, EditProfileForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm , PasswordChangeForm
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
            profile = new_user.profile




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

def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST,instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('userlogin.login')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
        print(request.user)
    return render(request, 'userlogin/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

