from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth 
# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email  = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username take ")
                messages.Info(request, "username taken")
                return redirect("/")
            elif User.objects.filter(email=email).exists():
                print("Email exists")
                return redirect("/")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User created")
                return redirect(request, 'login')
                
        else:
            print("Password do not match")
            messages.Info(request, "password do not atch")
            return redirect("/")
    else:
        return render(request, "register.html")



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.Info(request, "Invalid credentials ")
            return redirect(request, 'login.html')
            
    else:
        return render(request, 'login')

