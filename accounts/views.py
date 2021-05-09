from django.shortcuts import render,redirect
from .models import UsersAccounts
from .forms import CreateUserLogForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request,'home.html')
    pass

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # login(request, user)
            print("User Found")
            return redirect('home')
        else:
            print("User Not Found")
            return redirect('login')
            pass
            # messages.error(request, "Username Or Password is incorrect!!",
            #                extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'login.html')


    user=UsersAccounts.objects.all()
    return render(request,'login.html')
    pass

def signup(request):
    
    if request.method=="POST":
        form=CreateUserLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=CreateUserLogForm()
    
    return render(request,'signup.html')
    pass

# def logout(request):
#     logout(request)
#     return render(request,'home')