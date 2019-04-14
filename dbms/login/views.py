from django.shortcuts import render

# Create your views here.
def home(request):
    # Create your views here.

    return render(request, "login/home.html")

def login(request):

    return render(request,"userlogin/accounts.html")

def view_profile(request):
    args = {'user': request.user}
    print(request.user)
    return render(request, 'userlogin/profile.html', args)


